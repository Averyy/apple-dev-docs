# prompt

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A prompt, for the user, that appears above the navigation bar buttons.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var prompt: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * prompt;
```

## See Also

### Using a media item picker
- [var allowsPickingMultipleItems: Bool](./allowspickingmultipleitems.md)
  A Boolean value specifying the default selection behavior for a media item picker.
- [var showsCloudItems: Bool](./showsclouditems.md)
  A Boolean value specifying whether to display iCloud Media Library items for a media picker.
- [var mediaTypes: MPMediaType](./mediatypes.md)
  The media types that media item picker presents.
- [var showsItemsWithProtectedAssets: Bool](./showsitemswithprotectedassets.md)
  A Boolean value that specifies whether the media item picker displays protected assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/prompt)*