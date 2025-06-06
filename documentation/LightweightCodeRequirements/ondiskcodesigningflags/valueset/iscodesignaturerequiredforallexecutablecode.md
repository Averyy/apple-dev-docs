# isCodeSignatureRequiredForAllExecutableCode

**Framework**: LightweightCodeRequirements  
**Kind**: property

Flag indicating that the process should not allow code to execute from memory if that memory is not associated with a code signature.

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
static let isCodeSignatureRequiredForAllExecutableCode: OnDiskCodeSigningFlags.ValueSet
```

#### Discussion

This flag may be present on any on disk signature. This flag only has effect on main executables.  This flag has no effect on iOS/watchOS/tvOS/visionOS or iOS apps on macOS. All processes on iOS/watchOS/tvOS/visionOS and all iOS apps on macOS always require code signatures to be associated with all executable memory. On all platforms, entitlements provide an exception to this policy to allow JIT. This is equivalent to `CS_ENFORCEMENT` in C APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcodesigningflags/valueset/iscodesignaturerequiredforallexecutablecode)*