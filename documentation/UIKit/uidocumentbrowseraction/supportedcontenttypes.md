# supportedContentTypes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of uniform type identifiers that define the types of documents that the action supports.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var supportedContentTypes: [String] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSString *> * supportedContentTypes;
```

## Discussion

The action can be triggered only on documents that are allowed by both the action’s [`supportedContentTypes`](./supportedcontenttypes.md) property and the document browser’s [`allowedContentTypes`](../uidocumentbrowserviewcontroller/allowedcontenttypes.md) property.

By default, this property contains only the `public.item` uniform type identifier (UTI)—indicating that there are no additional restrictions on document types.

To further restrict the supported documents, assign an array that contains a more restricted set of UTIs. These UTIs should define a subset of the UTIs supported by the document browser.

For more about UTIs, see [Uniform Type Identifiers Reference](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/UTIRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009257).

## See Also

### Creating and configuring actions
- [init(identifier: String, localizedTitle: String, availability: UIDocumentBrowserAction.Availability, handler: ([URL]) -> Void)](./init%28identifier,localizedtitle,availability,handler%29.md)
  Instantiates and returns a new browser action item.
- [var image: UIImage?](./image.md)
  The action’s image displayed in the navigation bar.
- [var supportsMultipleItems: Bool](./supportsmultipleitems.md)
  A Boolean value that determines whether the action can be triggered on more than one document at a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowseraction/supportedcontenttypes)*