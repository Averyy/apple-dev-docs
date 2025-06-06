# developerID

**Framework**: LightweightCodeRequirements  
**Kind**: property

Indicates that the code is signed by an Apple issued Developer ID certificate.

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
static let developerID: ValidationCategory.Value
```

#### Discussion

This category will only match process on macOS. This category could match code on disk on iOS/watchOS/tvOS/visionOS but that code cannot run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/validationcategory/value/developerid)*