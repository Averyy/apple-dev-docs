# ProcessCodeSigningFlags.ValueSet

**Framework**: LightweightCodeRequirements  
**Kind**: struct

Code signing flags that can be set on a process

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
struct ValueSet
```

## Topics

### Initializers
- [init(rawValue: Int64)](processcodesigningflags/valueset/init(rawvalue:).md)
  Creates a new option set from the given raw value.
### Instance Properties
- [let rawValue: Int64](processcodesigningflags/valueset/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [ProcessCodeSigningFlags.ValueSet.ArrayLiteralElement](processcodesigningflags/valueset/arrayliteralelement.md)
  The type of the elements of an array literal.
- [ProcessCodeSigningFlags.ValueSet.Element](processcodesigningflags/valueset/element.md)
  The element type of the option set.
- [ProcessCodeSigningFlags.ValueSet.RawValue](processcodesigningflags/valueset/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let isAdhocSigned: ProcessCodeSigningFlags.ValueSet](processcodesigningflags/valueset/isadhocsigned.md)
  The code is adhoc signed i.e. it contains a code directory and page hashes but no CMS signature.
- [static let isCertificateExpirationEnforced: ProcessCodeSigningFlags.ValueSet](processcodesigningflags/valueset/iscertificateexpirationenforced.md)
  Flag indicating that the signature on this code should be treated as invalid if the certificate it was signed with expired.
- [static let isCodeSignatureRequiredForAllExecutableCode: ProcessCodeSigningFlags.ValueSet](processcodesigningflags/valueset/iscodesignaturerequiredforallexecutablecode.md)
  Flag indicating that the process should not allow code to execute from memory if that memory is not associated with a code signature.
- [static let isDebuggable: ProcessCodeSigningFlags.ValueSet](processcodesigningflags/valueset/isdebuggable.md)
  Flag indicating that the process is debuggable by authorized debuggers.
- [static let isDebugged: ProcessCodeSigningFlags.ValueSet](processcodesigningflags/valueset/isdebugged.md)
  Flag indicating that the process has been attached by a debugger.
- [static let isDynamicLinkerPolicyHardened: ProcessCodeSigningFlags.ValueSet](processcodesigningflags/valueset/isdynamiclinkerpolicyhardened.md)
  Flag indicating that the process should get hardened dynamic linker policies.
- [static let isDynamicallyValid: ProcessCodeSigningFlags.ValueSet](processcodesigningflags/valueset/isdynamicallyvalid.md)
  Flag indicating that no code signing validation errors have been found for the process.
- [static let isHardenedRuntimeEnforced: ProcessCodeSigningFlags.ValueSet](processcodesigningflags/valueset/ishardenedruntimeenforced.md)
  Flag indicating that the process has enabled the Hardened Runtime
- [static let isLibraryValidationRequired: ProcessCodeSigningFlags.ValueSet](processcodesigningflags/valueset/islibraryvalidationrequired.md)
  Flag indicating that the process should enforce Library Validation.
- [static let isPlatformSigned: ProcessCodeSigningFlags.ValueSet](processcodesigningflags/valueset/isplatformsigned.md)
  Flag indicating that the binary has been identified as a platform binary (Apple Signed).
- [static let isSigned: ProcessCodeSigningFlags.ValueSet](processcodesigningflags/valueset/issigned.md)
  Flag indicating that the process is signed.
- [static let isSignedByLinker: ProcessCodeSigningFlags.ValueSet](processcodesigningflags/valueset/issignedbylinker.md)
  Flag indicating that the code was signed by the linker and not an invocation of codesign.
- [static let signalsBusErrorOnCodeSigningFailure: ProcessCodeSigningFlags.ValueSet](processcodesigningflags/valueset/signalsbuserroroncodesigningfailure.md)
  Code signing failures on page-in should be rejected as SIGBUS errors.
- [static let terminatesOnCodeSigningFailure: ProcessCodeSigningFlags.ValueSet](processcodesigningflags/valueset/terminatesoncodesigningfailure.md)
  Code signing failures on page in should cause the process to be terminated.
### Default Implementations
- [Equatable Implementations](processcodesigningflags/valueset/equatable-implementations.md)
- [OptionSet Implementations](processcodesigningflags/valueset/optionset-implementations.md)
- [RawRepresentable Implementations](processcodesigningflags/valueset/rawrepresentable-implementations.md)
- [SetAlgebra Implementations](processcodesigningflags/valueset/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/processcodesigningflags/valueset)*