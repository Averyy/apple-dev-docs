# itemIdentifier

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

The local identifier of the item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS

## Declaration

```swift
var itemIdentifier: String? { get }
```

#### Discussion

This value is `nil` if you create a Photos picker without a photo library.

## See Also

### Inspecting a picker item
- [var supportedContentTypes: [UTType]](./supportedcontenttypes.md)
  The content types the item supports in order of the most preferred to the least.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/photospickeritem/itemidentifier)*