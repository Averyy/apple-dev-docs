# init(rawValue:)

**Framework**: Core ML  
**Kind**: init

Creates an image feature option key from a raw value string.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(rawValue: String)
```

#### Discussion

Don’t use this initializer directly. Create an image option key with [`cropAndScale`](mlfeaturevalue/imageoption/cropandscale.md) or [`cropRect`](mlfeaturevalue/imageoption/croprect.md) instead.

## Parameters

- `rawValue`: A string that represents the name of the image feature option key.

## See Also

- [init(String)](mlfeaturevalue/imageoption/init(_:).md)
  Creates an image feature option key from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturevalue/imageoption/init(rawvalue:))*