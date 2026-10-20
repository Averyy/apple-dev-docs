# OnDiskCodeSigningFlags.ValueSet

**Framework**: LightweightCodeRequirements  
**Kind**: struct  
**Role**: Structure

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

### Type Properties
- [static let isAdhocSigned: OnDiskCodeSigningFlags.ValueSet](./valueset/isadhocsigned.md)
  The code is adhoc signed i.e. it contains a code directory and page hashes but no CMS signature.
- [static let isCertificateExpirationEnforced: OnDiskCodeSigningFlags.ValueSet](./valueset/iscertificateexpirationenforced.md)
  Flag indicating that the signature on this code should be treated as invalid if the certificate it was signed with expired.
- [static let isCodeSignatureRequiredForAllExecutableCode: OnDiskCodeSigningFlags.ValueSet](./valueset/iscodesignaturerequiredforallexecutablecode.md)
  Flag indicating that the process should not allow code to execute from memory if that memory is not associated with a code signature.
- [static let isDynamicLinkerPolicyHardened: OnDiskCodeSigningFlags.ValueSet](./valueset/isdynamiclinkerpolicyhardened.md)
  Flag indicating that the process should get hardened dynamic linker policies.
- [static let isHardenedRuntimeEnforced: OnDiskCodeSigningFlags.ValueSet](./valueset/ishardenedruntimeenforced.md)
  Flag indicating that the process has enabled the Hardened Runtime
- [static let isLibraryValidationRequired: OnDiskCodeSigningFlags.ValueSet](./valueset/islibraryvalidationrequired.md)
  Flag indicating that the process should enforce Library Validation.
- [static let isSignedByLinker: OnDiskCodeSigningFlags.ValueSet](./valueset/issignedbylinker.md)
  Flag indicating that the code was signed by the linker and not an invocation of codesign.
- [static let signalsBusErrorOnCodeSigningFailure: OnDiskCodeSigningFlags.ValueSet](./valueset/signalsbuserroroncodesigningfailure.md)
  Code signing failures on page-in should be rejected as SIGBUS errors.
- [static let terminatesOnCodeSigningFailure: OnDiskCodeSigningFlags.ValueSet](./valueset/terminatesoncodesigningfailure.md)
  Code signing failures on page in should cause the process to be terminated.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcodesigningflags/valueset)*