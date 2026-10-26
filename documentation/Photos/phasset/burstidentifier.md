# burstIdentifier

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The unique identifier shared by photo assets from the same burst sequence.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var burstIdentifier: String? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSString * burstIdentifier;
```

#### Discussion

When the user takes a sequence of photos in burst mode with the Camera app (on supported devices), the Photos app user interface groups the resulting assets together. The Photos framework identifies a burst sequence as a group of assets sharing the same burst identifier string.

## See Also

### Related Documentation
- [class func fetchAssets(withBurstIdentifier: String, options: PHFetchOptions?) -> PHFetchResult<PHAsset>](./fetchassets%28withburstidentifier,options%29.md)
  Retrieves assets with the specified burst photo sequence identifier.
### Working with Burst Photo Assets
- [var burstSelectionTypes: PHAssetBurstSelectionType](./burstselectiontypes.md)
  The selection type of the asset in a burst photo sequence.
- [struct PHAssetBurstSelectionType](../phassetburstselectiontype.md)
  Bit mask values indicating whether and how an asset is marked as a favorite member of a burst photo sequence. Used by the [`burstSelectionTypes`](./burstselectiontypes.md) property.
- [var representsBurst: Bool](./representsburst.md)
  A Boolean value that indicates whether the asset is the representative photo from a burst photo sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/burstidentifier)*