# allowsPickingMultipleItems

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A Boolean value specifying the default selection behavior for a media item picker.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var allowsPickingMultipleItems: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsPickingMultipleItems;
```

## Discussion

When set to [`true`](../../Swift/true.md), the media item picker allows the selection of multiple media items. When set to [`false`](../../Swift/false.md), the media picker only allows the selection of a single media item. The label for the button that dismisses the picker is “Done” when this value is [`true`](../../Swift/true.md) and “Cancel” when it’s [`false`](../../Swift/false.md).

## See Also

### Using a media item picker
- [var showsCloudItems: Bool](./showsclouditems.md)
  A Boolean value specifying whether to display iCloud Media Library items for a media picker.
- [var mediaTypes: MPMediaType](./mediatypes.md)
  The media types that media item picker presents.
- [var prompt: String?](./prompt.md)
  A prompt, for the user, that appears above the navigation bar buttons.
- [var showsItemsWithProtectedAssets: Bool](./showsitemswithprotectedassets.md)
  A Boolean value that specifies whether the media item picker displays protected assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/allowspickingmultipleitems)*