# showsItemsWithProtectedAssets

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether the media item picker displays protected assets.

**Availability**:
- iOS 9.2+
- iPadOS 9.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var showsItemsWithProtectedAssets: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsItemsWithProtectedAssets;
```

## Discussion

When set to [`true`](../../Swift/true.md), the media item picker displays media items with DRM. The default value for this property is [`true`](../../Swift/true.md).

## See Also

### Using a media item picker
- [var allowsPickingMultipleItems: Bool](./allowspickingmultipleitems.md)
  A Boolean value specifying the default selection behavior for a media item picker.
- [var showsCloudItems: Bool](./showsclouditems.md)
  A Boolean value specifying whether to display iCloud Media Library items for a media picker.
- [var mediaTypes: MPMediaType](./mediatypes.md)
  The media types that media item picker presents.
- [var prompt: String?](./prompt.md)
  A prompt, for the user, that appears above the navigation bar buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/showsitemswithprotectedassets)*