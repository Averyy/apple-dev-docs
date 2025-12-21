# LaunchCodeRequirement

**Framework**: LightweightCodeRequirements  
**Kind**: struct

A lightweight code requirement that you use to evaluate the executable for a launching process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
struct LaunchCodeRequirement
```

#### Overview

If you set a `LaunchCodeRequirement` object for a launching process and the executable doesn’t satisfy the requirement, the operating system doesn’t run the process and creates a crash report instead. [`LaunchCodeRequirement`](launchcoderequirement.md) objects can only be built using constraints that conform to the [`LaunchConstraint`](launchconstraint.md) protocol. Note that [`LaunchCodeRequirement`](launchcoderequirement.md) are applied to processes. If a launch requests execution of ‘#!’ script, the launch constraint will be applied to the interpreter. For example a script with the following ‘#!’ will apply a launch constraint to bash.

```bash
#! /bin/bash
```

if the ‘#!’ is instead:

```bash
 #! /usr/bin/env python
```

Then the launch constraint is applied to env.

## Topics

### Initializers
- [init(ProcessCodeRequirement) throws](launchcoderequirement/init(_:)-5fh0u.md)
  Convert a [`ProcessCodeRequirement`](processcoderequirement.md) to a [`LaunchCodeRequirement`](launchcoderequirement.md) if possible.
- [init(OnDiskCodeRequirement) throws](launchcoderequirement/init(_:)-6hixy.md)
  Convert a [`OnDiskCodeRequirement`](ondiskcoderequirement.md) to a [`LaunchCodeRequirement`](launchcoderequirement.md) if possible.
- [init(from: any Decoder) throws](launchcoderequirement/init(from:).md)
  Create a new instance by decoding from the given decoder
### Instance Methods
- [func encode(to: any Encoder) throws](launchcoderequirement/encode(to:).md)
  Encodes this value into the given encoder
### Type Methods
- [static func allOf(requirement: () -> [any LaunchConstraint]) throws -> LaunchCodeRequirement](launchcoderequirement/allof(requirement:).md)
  Create a [`LaunchCodeRequirement`](launchcoderequirement.md) that requires matching all of the provided constraints.
- [static func anyOf(requirement: () -> [any LaunchConstraint]) throws -> LaunchCodeRequirement](launchcoderequirement/anyof(requirement:).md)
  Create a [`LaunchCodeRequirement`](launchcoderequirement.md) that requires matching any of the provided constraints.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func SecCodeCheckValidityWithProcessRequirement(code: SecCode, flags: SecCSFlags, requirement: ProcessCodeRequirement) -> ValidationResult](seccodecheckvaliditywithprocessrequirement(code:flags:requirement:).md)
  Checks whether the code associated with a running process satisfies a lightweight code requirement.
- [var launchRequirement: LaunchCodeRequirement?](../Foundation/Process/launchRequirement.md)
- [func allOf(requirement: () -> [any LaunchConstraint]) -> any LaunchConstraint](allof(requirement:)-4gf5f.md)
  Creates a constraint that requires a launching process’s executable to satisfy all of the provided constraints.
- [func anyOf(requirement: () -> [any LaunchConstraint]) -> any LaunchConstraint](anyof(requirement:)-6nicx.md)
  Creates a constraint that requires a launching process’s executable to satisfy any of the provided constraints.
- [protocol LaunchConstraint](launchconstraint.md)
  A protocol to which a lightweight code requirement constraint conforms if you can use it in launch code requirements.
- [struct LaunchConstraintBuilder](launchconstraintbuilder.md)
  A custom parameter attribute that constructs launch constraints from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/launchcoderequirement)*