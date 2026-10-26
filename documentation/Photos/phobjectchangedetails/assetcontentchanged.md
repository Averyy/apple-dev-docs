# assetContentChanged

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the asset’s photo or video content has changed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var assetContentChanged: Bool { get }
```

```objc
@property (atomic, readonly) BOOL assetContentChanged;
```

#### Discussion

If this value `true`, you can use the [`PHImageManager`](../phimagemanager.md) class to retrieve updated content.

This value is `false` if the asset has not changed or if the change details do not refer to a [`PHAsset`](../phasset.md) object.

## See Also

### Getting Change Information
- [var objectWasDeleted: Bool](./objectwasdeleted.md)
  A Boolean value that indicates whether the object has been deleted from the Photos library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phobjectchangedetails/assetcontentchanged)*