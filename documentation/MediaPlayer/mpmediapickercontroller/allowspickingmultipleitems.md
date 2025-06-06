# allowsPickingMultipleItems

**Framework**: Media Player  
**Kind**: property

A Boolean value specifying the default selection behavior for a media item picker.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var allowsPickingMultipleItems: Bool { get set }
```

#### Discussion

When set to [`true`](https://developer.apple.com/documentation/swift/true), the media item picker allows the selection of multiple media items. When set to [`false`](https://developer.apple.com/documentation/swift/false), the media picker only allows the selection of a single media item. The label for the button that dismisses the picker is “Done” when this value is [`true`](https://developer.apple.com/documentation/swift/true) and “Cancel” when it’s [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var showsCloudItems: Bool](mpmediapickercontroller/showsclouditems.md)
  A Boolean value specifying whether to display iCloud Media Library items for a media picker.
- [var mediaTypes: MPMediaType](mpmediapickercontroller/mediatypes.md)
  The media types that media item picker presents.
- [var prompt: String?](mpmediapickercontroller/prompt.md)
  A prompt, for the user, that appears above the navigation bar buttons.
- [var showsItemsWithProtectedAssets: Bool](mpmediapickercontroller/showsitemswithprotectedassets.md)
  A Boolean value that specifies whether the media item picker displays protected assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/allowspickingmultipleitems)*