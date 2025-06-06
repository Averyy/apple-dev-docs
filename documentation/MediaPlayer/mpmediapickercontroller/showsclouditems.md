# showsCloudItems

**Framework**: Media Player  
**Kind**: property

A Boolean value specifying whether to display iCloud Media Library items for a media picker.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var showsCloudItems: Bool { get set }
```

#### Discussion

When set to [`true`](https://developer.apple.com/documentation/swift/true), the picker shows available iCloud Music Library items, including purchased items, imported content, and Apple Music subscription content. When set to [`false`](https://developer.apple.com/documentation/swift/false), the picker only shows content downloaded to the device. The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var allowsPickingMultipleItems: Bool](mpmediapickercontroller/allowspickingmultipleitems.md)
  A Boolean value specifying the default selection behavior for a media item picker.
- [var mediaTypes: MPMediaType](mpmediapickercontroller/mediatypes.md)
  The media types that media item picker presents.
- [var prompt: String?](mpmediapickercontroller/prompt.md)
  A prompt, for the user, that appears above the navigation bar buttons.
- [var showsItemsWithProtectedAssets: Bool](mpmediapickercontroller/showsitemswithprotectedassets.md)
  A Boolean value that specifies whether the media item picker displays protected assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/showsclouditems)*