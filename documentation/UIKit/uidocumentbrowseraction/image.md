# image

**Framework**: UIKit  
**Kind**: property

The action’s image displayed in the navigation bar.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var image: UIImage? { get set }
```

#### Discussion

This property is used only when the action is displayed in the navigation bar. By default, it is set to `nil`, and the navigation bar displays the value of the action’s [`localizedTitle`](uidocumentbrowseraction/localizedtitle.md) property.

If set, the navigation bar derives a bar button image from this image. Only the alpha values in the source image are used to create the bar button image—opaque values are ignored.

If this image is too large, it is scaled to fit. Typically, navigation bar images are 20 x 20 points.

## See Also

- [init(identifier: String, localizedTitle: String, availability: UIDocumentBrowserAction.Availability, handler: ([URL]) -> Void)](uidocumentbrowseraction/init(identifier:localizedtitle:availability:handler:).md)
  Instantiates and returns a new browser action item.
- [var supportedContentTypes: [String]](uidocumentbrowseraction/supportedcontenttypes.md)
  An array of uniform type identifiers that define the types of documents that the action supports.
- [var supportsMultipleItems: Bool](uidocumentbrowseraction/supportsmultipleitems.md)
  A Boolean value that determines whether the action can be triggered on more than one document at a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowseraction/image)*