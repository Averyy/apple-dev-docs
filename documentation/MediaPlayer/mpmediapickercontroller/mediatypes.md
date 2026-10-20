# mediaTypes

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The media types that media item picker presents.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var mediaTypes: MPMediaType { get }
```

```objc
@property (nonatomic, readonly) MPMediaType mediaTypes;
```

#### Discussion

[`MPMediaType`](../mpmediatype.md) lists the available media types.

## See Also

### Using a media item picker
- [var allowsPickingMultipleItems: Bool](./allowspickingmultipleitems.md)
  A Boolean value specifying the default selection behavior for a media item picker.
- [var showsCloudItems: Bool](./showsclouditems.md)
  A Boolean value specifying whether to display iCloud Media Library items for a media picker.
- [var prompt: String?](./prompt.md)
  A prompt, for the user, that appears above the navigation bar buttons.
- [var showsItemsWithProtectedAssets: Bool](./showsitemswithprotectedassets.md)
  A Boolean value that specifies whether the media item picker displays protected assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/mediatypes)*