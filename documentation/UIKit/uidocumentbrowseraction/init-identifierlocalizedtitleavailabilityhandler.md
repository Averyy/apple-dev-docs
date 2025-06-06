# init(identifier:localizedTitle:availability:handler:)

**Framework**: UIKit  
**Kind**: init

Instantiates and returns a new browser action item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(identifier: String, localizedTitle: String, availability: UIDocumentBrowserAction.Availability, handler: @escaping ([URL]) -> Void)
```

## Parameters

- `identifier`: A unique identifier for the activity.
- `localizedTitle`: The title that appears in the Edit Menu or navigation bar. This title should be a   returned by   .
- `availability`: For a list of valid values, see  .
- `handler`: A block that is called when the user triggers the action. The block takes the following parameter:

## See Also

- [var image: UIImage?](uidocumentbrowseraction/image.md)
  The action’s image displayed in the navigation bar.
- [var supportedContentTypes: [String]](uidocumentbrowseraction/supportedcontenttypes.md)
  An array of uniform type identifiers that define the types of documents that the action supports.
- [var supportsMultipleItems: Bool](uidocumentbrowseraction/supportsmultipleitems.md)
  A Boolean value that determines whether the action can be triggered on more than one document at a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowseraction/init(identifier:localizedtitle:availability:handler:))*