# NSItemProvider.LoadHandler

**Framework**: Foundation  
**Kind**: typealias

A block that loads the item provider’s data and coerces it to the specified type.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias LoadHandler = (NSItemProvider.CompletionHandler?, AnyClass?, [AnyHashable : Any]?) -> Void
```

#### Discussion

Use this block when registering a type-specific coercion handler with the [`registerItem(forTypeIdentifier:loadHandler:)`](nsitemprovider/registeritem(fortypeidentifier:loadhandler:).md) method. The parameters for this block are as follows:

When a client calls the [`loadItem(forTypeIdentifier:options:completionHandler:)`](nsitemprovider/loaditem(fortypeidentifier:options:completionhandler:).md) method and requests the appropriate type, the item provider executes your block. In your implementation, create an object of the expected type and execute the block in the `completionHandler` parameter, passing the newly created object as the first parameter of that block. If there is an error, pass `nil` for the object and provide an appropriate [`NSError`](nserror.md) object explaining what happened.

This type of block is also used for generating preview images. In the case of a preview image, the `expectedValueClass` is always a [`NSData`](nsdata.md), [`NSURL`](nsurl.md), [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) (in iOS), or [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage) (in macOS) class.

## See Also

- [NSItemProvider.CompletionHandler](nsitemprovider/completionhandler.md)
  A block that receives the item provider’s data.
- [Options Dictionary Key](options-dictionary-key.md)
  Keys indicating options to use when generating the item provider’s data.
- [Keys for Items Accessed in JavaScript Code](keys-for-items-accessed-in-javascript-code.md)
  Keys in property list items that the system recieves from or sends to JavaScript code.
- [class let errorDomain: String](nsitemprovider/errordomain.md)
  The error domain associated with the item provider.
- [struct NSItemProviderFileOptions](nsitemproviderfileoptions.md)
  Data-access specifications that declare how to handle items.
- [protocol NSItemProviderReading](nsitemproviderreading.md)
  The protocol for implementing a class to allow an item provider to create an instance of the class.
- [protocol NSItemProviderWriting](nsitemproviderwriting.md)
  The protocol for implementing a class to allow an item provider to retrieve data from an instance of the class.
- [enum NSItemProviderRepresentationVisibility](nsitemproviderrepresentationvisibility.md)
  Specifications that control which categories of processes can see an item.
- [NSItemProvider.ErrorCode](nsitemprovider/errorcode.md)
  The error codes that describe problems with consuming data from an item provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/loadhandler)*