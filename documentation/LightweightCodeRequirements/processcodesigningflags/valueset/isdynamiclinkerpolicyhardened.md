# isDynamicLinkerPolicyHardened

**Framework**: LightweightCodeRequirements  
**Kind**: property

Flag indicating that the process should get hardened dynamic linker policies.

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
static let isDynamicLinkerPolicyHardened: ProcessCodeSigningFlags.ValueSet
```

#### Discussion

This flag may be present on any on disk signature. This flag only has effect on main executables. This flag has no effect on iOS/watchOS/tvOS/visionOS or iOS apps on macOS. All processes on iOS/watchOS/tvOS/visionOS and all iOS apps on macOS have the same dynamic linker policies. This is equivalent to `CS_RESTRICT` in C APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/processcodesigningflags/valueset/isdynamiclinkerpolicyhardened)*