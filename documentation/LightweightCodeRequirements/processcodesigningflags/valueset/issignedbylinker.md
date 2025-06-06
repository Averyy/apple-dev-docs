# isSignedByLinker

**Framework**: LightweightCodeRequirements  
**Kind**: property

Flag indicating that the code was signed by the linker and not an invocation of codesign.

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
static let isSignedByLinker: ProcessCodeSigningFlags.ValueSet
```

#### Discussion

This is equivalent to `CS_LINKER_SIGNED` in C APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/processcodesigningflags/valueset/issignedbylinker)*