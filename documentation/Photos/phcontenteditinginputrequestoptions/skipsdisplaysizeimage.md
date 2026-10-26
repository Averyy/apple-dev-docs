# skipsDisplaySizeImage

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

Set this value to `true` if you don’t want a `displaySizeImage` on the `PHContentEditingInput`. This can give performance wins when the image will not be used.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var skipsDisplaySizeImage: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL skipsDisplaySizeImage;
```

## See Also

### Specifying Edting Request Options
- [var canHandleAdjustmentData: (PHAdjustmentData) -> Bool](./canhandleadjustmentdata.md)
  A block to be called when Photos needs to determine whether your app can continue previous edits made to an asset.
- [var originalResourceChoice: PHAsset.OriginalResourceChoice](./originalresourcechoice.md)
  The original resource to use as the unadjusted base when fulfilling the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginputrequestoptions/skipsdisplaysizeimage)*