# LightweightCodeRequirements

**Framework**: LightweightCodeRequirements  
**Kind**: module

Test the identity of executable code on disk and in running processes.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+

#### Overview

Code that is cryptographically signed carries tamper-proof statements about its identity in its code signature. Construct tests to distinguish different code files using the lightweight code requirement domain-specific language (DSL). Use the tests to distinguish code files on disk, running processes, and processes that the operating system launches. Code files on disk include:

- Executable binaries
- Dynamic or static libraries
- Frameworks
- Loadable bundles

#### Define Tests of Signed Code Properties

The keywords you use to test code properties in the lightweight code requirement DSL are:

For code signed by an organization or individual other than Apple, the code’s identity is specified by its `SigningIdentifier`, `TeamIdentifier`, and `ValidationCategory`.

#### Combine Tests Into Requirements

The lightweight code requirement DSL provides operators that you use to build up complex requirements from individual tests. For example, the operators to construct on-disk code requirements are:

[`ProcessCodeRequirement`](processcoderequirement.md) and [`LaunchCodeRequirement`](launchcoderequirement.md) provide similar operators for building process code requirements and launch requirements.

The `anyOf(requirement:)` and `allOf(requirement:)` operators simplify their inputs as follows:

- An operator with a single constraint as its argument replaces itself with the direct evaluation of the given constraint.
- If any of the arguments to an `anyOf(requirement:)` operator are themselves `anyOf(requirement:)` operators, the arguments to both are merged into a single set of constraints evaluated by the top-level `anyOf(requirement:)` operator.
- If any of the arguments to an `allOf(requirement:)` operator are themselves `allOf(requirement:)` operators, the arguments to both are merged into a single set of constraints evaluated by the top-level `allOf(requirement:)` operator.

Both `allOf(requirement:)` and `anyOf(requirement:)` throw an error if the simplification results in the same constraint appearing twice in the arguments for one operator, for example, if an `anyOf(requirement:)` operator contains two tests of [`InfoPlistHash`](infoplisthash.md) constraints. The exception to this simplification rule is that multiple [`EntitlementsQuery`](entitlementsquery.md) tests can appear in the arguments for one operator.

#### Test Whether a Running Process Satisfies a Lightweight Code Requirement

Create a [`ProcessCodeRequirement`](processcoderequirement.md) using the DSL and pass it to [`SecTaskValidateForRequirement(task:requirement:)`](sectaskvalidateforrequirement(task:requirement:).md), along with a [`SecTask`](https://developer.apple.com/documentation/Security/SecTask) representing the running process. If the task’s code satisfies the lightweight code requirement, then the function returns `true`; otherwise, it returns `false`.

#### Test Whether Code on Disk Satisfies a Lightweight Code Requirement

Create an [`OnDiskCodeRequirement`](ondiskcoderequirement.md) using the DSL and pass it to [`SecStaticCodeCheckValidityWithOnDiskRequirement(code:flags:requirement:)`](secstaticcodecheckvaliditywithondiskrequirement(code:flags:requirement:).md) or [`SecCodeCheckValidityWithOnDiskRequirement(code:flags:requirement:)`](seccodecheckvaliditywithondiskrequirement(code:flags:requirement:).md), depending on whether you construct a [`SecStaticCode`](https://developer.apple.com/documentation/Security/SecStaticCode) or [`SecCode`](https://developer.apple.com/documentation/Security/SecCode) to represent the code. Both functions return a [`ValidationResult`](validationresult.md) indicating whether the code has a valid signature, whether it satisfies the requirement, and any error that occurred.

#### Restrict the Executables You Launch As New Processes

Create a [`LaunchCodeRequirement`](launchcoderequirement.md) using the DSL and set it as the [`launchRequirement`](https://developer.apple.com/documentation/foundation/process/4322522-launchrequirement) on a [`Process`](https://developer.apple.com/documentation/Foundation/Process) instance, before you call [`run()`](https://developer.apple.com/documentation/foundation/process/2890105-run). If the executable specified in the process’s [`executableURL`](https://developer.apple.com/documentation/foundation/process/2890106-executableurl) satisfies the launch requirement, the kernel launches the process; otherwise, `run()` throws an error. You can also encode your requirements as launch constraints in property list files that you embed in your executable’s code signature to restrict which processes can launch your executable and which dynamic libraries your process can load. For more information, see [`Applying launch environment and library constraints`](https://developer.apple.com/documentation/Security/applying-launch-environment-and-library-constraints).

## Topics

### Checking code requirements for running processes
- [func SecTaskValidateForRequirement(task: SecTask, requirement: ProcessCodeRequirement) throws -> Bool](sectaskvalidateforrequirement(task:requirement:).md)
  Tests whether a task’s executable satisfies a lightweight code requirement.
- [struct ProcessCodeRequirement](processcoderequirement.md)
  A lightweight code requirement that you use to evaluate a running process.
- [func allOf(requirement: () -> [any ProcessConstraint]) -> any ProcessConstraint](allof(requirement:)-4k3ay.md)
  Creates a constraint that requires a running process’s executable to satisfy all of the provided constraints.
- [func anyOf(requirement: () -> [any ProcessConstraint]) -> any ProcessConstraint](anyof(requirement:)-vwhn.md)
  Creates a constraint that requires a running process’s executable to satisfy any of the provided constraints.
- [protocol ProcessConstraint](processconstraint.md)
  A protocol to which a lightweight code requirement constraint conforms if you can use it in process code requirements.
- [struct ProcessCodeSigningFlags](processcodesigningflags.md)
  A constraint that matches the current code-signing flags of a process.
- [struct ProcessConstraintBuilder](processconstraintbuilder.md)
  A custom parameter attribute that constructs process constraints from closures.
- [struct TeamIdentifierMatchesCurrentProcess](teamidentifiermatchescurrentprocess.md)
  A constraint that matches if a process has the same team identifier as the calling process.
### Checking code requirements for launching processes
- [func SecCodeCheckValidityWithProcessRequirement(code: SecCode, flags: SecCSFlags, requirement: ProcessCodeRequirement) -> ValidationResult](seccodecheckvaliditywithprocessrequirement(code:flags:requirement:).md)
  Checks whether the code associated with a running process satisfies a lightweight code requirement.
- [var launchRequirement: LaunchCodeRequirement?](../foundation/process/4322522-launchrequirement.md)
- [struct LaunchCodeRequirement](launchcoderequirement.md)
  A lightweight code requirement that you use to evaluate the executable for a launching process.
- [func allOf(requirement: () -> [any LaunchConstraint]) -> any LaunchConstraint](allof(requirement:)-4gf5f.md)
  Creates a constraint that requires a launching process’s executable to satisfy all of the provided constraints.
- [func anyOf(requirement: () -> [any LaunchConstraint]) -> any LaunchConstraint](anyof(requirement:)-6nicx.md)
  Creates a constraint that requires a launching process’s executable to satisfy any of the provided constraints.
- [protocol LaunchConstraint](launchconstraint.md)
  A protocol to which a lightweight code requirement constraint conforms if you can use it in launch code requirements.
- [struct LaunchConstraintBuilder](launchconstraintbuilder.md)
  A custom parameter attribute that constructs launch constraints from closures.
### Checking code requirements for code files on disk
- [func SecStaticCodeCheckValidityWithOnDiskRequirement(code: SecStaticCode, flags: SecCSFlags, requirement: OnDiskCodeRequirement) -> ValidationResult](secstaticcodecheckvaliditywithondiskrequirement(code:flags:requirement:).md)
  Checks whether static code on disk satisfies a lightweight code requirement.
- [func SecCodeCheckValidityWithOnDiskRequirement(code: SecCode, flags: SecCSFlags, requirement: OnDiskCodeRequirement) -> ValidationResult](seccodecheckvaliditywithondiskrequirement(code:flags:requirement:).md)
  Checks whether code on disk satisfies a lightweight code requirement.
- [struct ValidationResult](validationresult.md)
  A structure that represents the result of testing a lightweight code requirement.
- [struct OnDiskCodeRequirement](ondiskcoderequirement.md)
  A lightweight code requirement that you use to evaluate a code file on disk.
- [func allOf(requirement: () -> [any OnDiskConstraint]) -> any OnDiskConstraint](allof(requirement:)-2ocwl.md)
  Creates a constraint that requires code on disk to satisfy all of the provided constraints.
- [func anyOf(requirement: () -> [any OnDiskConstraint]) -> any OnDiskConstraint](anyof(requirement:)-71pff.md)
  Creates a constraint that requires code on disk to satisfy any of the provided constraints.
- [protocol OnDiskConstraint](ondiskconstraint.md)
  A protocol to which a lightweight code requirement constraint conforms if you can use it in on-disk code requirements.
- [struct OnDiskCodeSigningFlags](ondiskcodesigningflags.md)
  A constraint that tests the code-signing flags of a code file on disk.
- [struct OnDiskConstraintBuilder](ondiskconstraintbuilder.md)
  A custom parameter attribute that constructs on-disk constraints from closures.
### Testing properties of executable code
- [struct CodeDirectoryHash](codedirectoryhash.md)
  A constraint that matches the hash of a code directory of a code file or of a running or launching process.
- [class EntitlementsQuery](entitlementsquery.md)
  A constraint that tests values in the entitlements dictionary associated with a process or code file.
- [struct InfoPlistHash](infoplisthash.md)
  A constraint that tests the specified hash against the Information property list hash stored in the code signature of the process or code file.
- [struct IsInitProcess](isinitprocess.md)
  A constraint that tests whether a process is the operating system’s initial process.
- [struct IsMainBinary](ismainbinary.md)
  A constraint that tests whether a code file is a main binary.
- [struct IsSIPProtected](issipprotected.md)
  A constraint that tests whether a code file or process is on a volume protected by System Integrity Protection (SIP).
- [struct PlatformType](platformtype.md)
  A constraint that tests whether a code file or running process targets a given platform.
- [struct SigningIdentifier](signingidentifier.md)
  A constraint that tests whether the provided signing identifier matches the signature attached to the code.
- [struct TeamIdentifier](teamidentifier.md)
  A constraint that tests whether the provided team identifier matches the team identified in the code signature.
- [struct ValidationCategory](validationcategory.md)
  A constraint that tests whether a code file or running process is signed in a way that conforms to the specified validation category.
### Handling errors
- [enum ConstraintError](constrainterror.md)
  Error types that can be thrown from lightweight code requirement routines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/LightweightCodeRequirements)*