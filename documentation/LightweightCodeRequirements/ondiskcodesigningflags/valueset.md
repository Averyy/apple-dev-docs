# OnDiskCodeSigningFlags.ValueSet

**Framework**: LightweightCodeRequirements  
**Kind**: struct

Code signing flags that can be set on code on disk.

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
- [init(rawValue: Int64)](ondiskcodesigningflags/valueset/init(rawvalue:).md)
  Creates a new option set from the given raw value.
### Instance Properties
- [let rawValue: Int64](ondiskcodesigningflags/valueset/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [OnDiskCodeSigningFlags.ValueSet.ArrayLiteralElement](ondiskcodesigningflags/valueset/arrayliteralelement.md)
  The type of the elements of an array literal.
- [OnDiskCodeSigningFlags.ValueSet.Element](ondiskcodesigningflags/valueset/element.md)
  The element type of the option set.
- [OnDiskCodeSigningFlags.ValueSet.RawValue](ondiskcodesigningflags/valueset/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let isAdhocSigned: OnDiskCodeSigningFlags.ValueSet](ondiskcodesigningflags/valueset/isadhocsigned.md)
  The code is adhoc signed i.e. it contains a code directory and page hashes but no CMS signature.
- [static let isCertificateExpirationEnforced: OnDiskCodeSigningFlags.ValueSet](ondiskcodesigningflags/valueset/iscertificateexpirationenforced.md)
  Flag indicating that the signature on this code should be treated as invalid if the certificate it was signed with expired.
- [static let isCodeSignatureRequiredForAllExecutableCode: OnDiskCodeSigningFlags.ValueSet](ondiskcodesigningflags/valueset/iscodesignaturerequiredforallexecutablecode.md)
  Flag indicating that the process should not allow code to execute from memory if that memory is not associated with a code signature.
- [static let isDynamicLinkerPolicyHardened: OnDiskCodeSigningFlags.ValueSet](ondiskcodesigningflags/valueset/isdynamiclinkerpolicyhardened.md)
  Flag indicating that the process should get hardened dynamic linker policies.
- [static let isHardenedRuntimeEnforced: OnDiskCodeSigningFlags.ValueSet](ondiskcodesigningflags/valueset/ishardenedruntimeenforced.md)
  Flag indicating that the process has enabled the Hardened Runtime
- [static let isLibraryValidationRequired: OnDiskCodeSigningFlags.ValueSet](ondiskcodesigningflags/valueset/islibraryvalidationrequired.md)
  Flag indicating that the process should enforce Library Validation.
- [static let isSignedByLinker: OnDiskCodeSigningFlags.ValueSet](ondiskcodesigningflags/valueset/issignedbylinker.md)
  Flag indicating that the code was signed by the linker and not an invocation of codesign.
- [static let signalsBusErrorOnCodeSigningFailure: OnDiskCodeSigningFlags.ValueSet](ondiskcodesigningflags/valueset/signalsbuserroroncodesigningfailure.md)
  Code signing failures on page-in should be rejected as SIGBUS errors.
- [static let terminatesOnCodeSigningFailure: OnDiskCodeSigningFlags.ValueSet](ondiskcodesigningflags/valueset/terminatesoncodesigningfailure.md)
  Code signing failures on page in should cause the process to be terminated.
### Default Implementations
- [Equatable Implementations](ondiskcodesigningflags/valueset/equatable-implementations.md)
- [OptionSet Implementations](ondiskcodesigningflags/valueset/optionset-implementations.md)
- [RawRepresentable Implementations](ondiskcodesigningflags/valueset/rawrepresentable-implementations.md)
- [SetAlgebra Implementations](ondiskcodesigningflags/valueset/setalgebra-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcodesigningflags/valueset)*