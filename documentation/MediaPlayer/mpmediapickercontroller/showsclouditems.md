# showsCloudItems

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A Boolean value specifying whether to display iCloud Media Library items for a media picker.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var showsCloudItems: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsCloudItems;
```

## Discussion

When set to [`true`](../../Swift/true.md), the picker shows available iCloud Music Library items, including purchased items, imported content, and Apple Music subscription content. When set to [`false`](../../Swift/false.md), the picker only shows content downloaded to the device. The default value is [`true`](../../Swift/true.md).

## See Also

### Using a media item picker
- [var allowsPickingMultipleItems: Bool](./allowspickingmultipleitems.md)
  A Boolean value specifying the default selection behavior for a media item picker.
- [var mediaTypes: MPMediaType](./mediatypes.md)
  The media types that media item picker presents.
- [var prompt: String?](./prompt.md)
  A prompt, for the user, that appears above the navigation bar buttons.
- [var showsItemsWithProtectedAssets: Bool](./showsitemswithprotectedassets.md)
  A Boolean value that specifies whether the media item picker displays protected assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/showsclouditems)*