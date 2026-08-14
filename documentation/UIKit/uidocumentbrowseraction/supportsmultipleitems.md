# supportsMultipleItems

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the action can be triggered on more than one document at a time.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var supportsMultipleItems: Bool { get set }
```

#### Discussion

This property defaults to [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [init(identifier: String, localizedTitle: String, availability: UIDocumentBrowserAction.Availability, handler: ([URL]) -> Void)](uidocumentbrowseraction/init(identifier:localizedtitle:availability:handler:).md)
  Instantiates and returns a new browser action item.
- [var image: UIImage?](uidocumentbrowseraction/image.md)
  The action’s image displayed in the navigation bar.
- [var supportedContentTypes: [String]](uidocumentbrowseraction/supportedcontenttypes.md)
  An array of uniform type identifiers that define the types of documents that the action supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowseraction/supportsmultipleitems)*