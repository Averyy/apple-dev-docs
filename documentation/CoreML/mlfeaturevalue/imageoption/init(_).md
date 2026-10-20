# init(_:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates an image feature option key from a string.

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
init(_ rawValue: String)
```

#### Discussion

Don’t use this initializer directly. Create an image option key with [`cropAndScale`](./cropandscale.md) or [`cropRect`](./croprect.md) instead.

## Parameters

- `rawValue`: A string that represents the name of the image feature option key.

## See Also

### Image option key initializers
- [init(rawValue: String)](./init%28rawvalue%29.md)
  Creates an image feature option key from a raw value string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturevalue/imageoption/init(_:))*