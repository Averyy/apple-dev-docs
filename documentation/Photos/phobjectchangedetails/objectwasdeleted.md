# objectWasDeleted

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the object has been deleted from the Photos library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var objectWasDeleted: Bool { get }
```

```objc
@property (atomic, readonly) BOOL objectWasDeleted;
```

## Discussion

If this value is `true`, the asset or collection has been permanently deleted from the Photos library.

To instead track the removal of assets from collections (or collections from collection lists), fetch the collection’s contents and use the [`changeDetails(for:)`](../phchange/changedetails%28for%29-33a6n.md) method to track changes to the fetch result.

## See Also

### Getting Change Information
- [var assetContentChanged: Bool](./assetcontentchanged.md)
  A Boolean value that indicates whether the asset’s photo or video content has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phobjectchangedetails/objectwasdeleted)*