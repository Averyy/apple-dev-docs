# canContainAssets

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the collection can contain assets.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var canContainAssets: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL canContainAssets;
```

## Discussion

If this value is `true`, the collection is a [`PHAssetCollection`](../phassetcollection.md) object; otherwise, `false`. For details on asset collections, see [`PHAssetCollection`](../phassetcollection.md).

## See Also

### Determining Collection Capabilities
- [var canContainCollections: Bool](./cancontaincollections.md)
  A Boolean value indicating whether the collection can contain other collections.
- [func canPerform(PHCollectionEditOperation) -> Bool](./canperform%28_%29.md)
  Returns whether the collection supports the specified editing operation.
- [enum PHCollectionEditOperation](../phcollectioneditoperation.md)
  Values identifying possible actions that a collection can support, used by the [`canPerform(_:)`](./canperform%28_%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollection/cancontainassets)*