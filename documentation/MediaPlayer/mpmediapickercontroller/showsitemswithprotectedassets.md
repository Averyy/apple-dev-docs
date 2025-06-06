# showsItemsWithProtectedAssets

**Framework**: Media Player  
**Kind**: property

A Boolean value that specifies whether the media item picker displays protected assets.

**Availability**:
- iOS 9.2+
- iPadOS 9.2+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var showsItemsWithProtectedAssets: Bool { get set }
```

#### Discussion

When set to [`true`](https://developer.apple.com/documentation/swift/true), the media item picker displays media items with DRM. The default value for this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var allowsPickingMultipleItems: Bool](mpmediapickercontroller/allowspickingmultipleitems.md)
  A Boolean value specifying the default selection behavior for a media item picker.
- [var showsCloudItems: Bool](mpmediapickercontroller/showsclouditems.md)
  A Boolean value specifying whether to display iCloud Media Library items for a media picker.
- [var mediaTypes: MPMediaType](mpmediapickercontroller/mediatypes.md)
  The media types that media item picker presents.
- [var prompt: String?](mpmediapickercontroller/prompt.md)
  A prompt, for the user, that appears above the navigation bar buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/showsitemswithprotectedassets)*