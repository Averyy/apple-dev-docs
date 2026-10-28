# supportsMultipleItems

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign) BOOL supportsMultipleItems;
```

## Discussion

This property defaults to [`true`](../../Swift/true.md).

## See Also

### Creating and configuring actions
- [init(identifier: String, localizedTitle: String, availability: UIDocumentBrowserAction.Availability, handler: ([URL]) -> Void)](./init%28identifier,localizedtitle,availability,handler%29.md)
  Instantiates and returns a new browser action item.
- [var image: UIImage?](./image.md)
  The action’s image displayed in the navigation bar.
- [var supportedContentTypes: [String]](./supportedcontenttypes.md)
  An array of uniform type identifiers that define the types of documents that the action supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowseraction/supportsmultipleitems)*