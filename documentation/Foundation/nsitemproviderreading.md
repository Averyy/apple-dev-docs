# NSItemProviderReading

**Framework**: Foundation  
**Kind**: protocol

The protocol for implementing a class to allow an item provider to create an instance of the class.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
protocol NSItemProviderReading : NSObjectProtocol
```

#### Overview

A destination app uses an object that conforms to this protocol to consume pasted or dropped items.

## Topics

### Creating an object from a pasted or dropped item
- [static func object(withItemProviderData: Data, typeIdentifier: String) throws -> Self](nsitemproviderreading/object(withitemproviderdata:typeidentifier:).md)
  Creates a new instance of a class using the given data and UTI string.
### Getting the readable type identifiers
- [static var readableTypeIdentifiersForItemProvider: [String]](nsitemproviderreading/readabletypeidentifiersforitemprovider.md)
  An array of UTI strings representing the data types supported by the class.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSAttributedString](nsattributedstring.md)
- [NSMutableString](nsmutablestring.md)
- [NSString](nsstring.md)
- [NSURL](nsurl.md)
- [NSUserActivity](nsuseractivity.md)

## See Also

- [NSItemProvider.CompletionHandler](nsitemprovider/completionhandler.md)
  A block that receives the item provider’s data.
- [NSItemProvider.LoadHandler](nsitemprovider/loadhandler.md)
  A block that loads the item provider’s data and coerces it to the specified type.
- [Options Dictionary Key](options-dictionary-key.md)
  Keys indicating options to use when generating the item provider’s data.
- [Keys for Items Accessed in JavaScript Code](keys-for-items-accessed-in-javascript-code.md)
  Keys in property list items that the system recieves from or sends to JavaScript code.
- [class let errorDomain: String](nsitemprovider/errordomain.md)
  The error domain associated with the item provider.
- [struct NSItemProviderFileOptions](nsitemproviderfileoptions.md)
  Data-access specifications that declare how to handle items.
- [protocol NSItemProviderWriting](nsitemproviderwriting.md)
  The protocol for implementing a class to allow an item provider to retrieve data from an instance of the class.
- [enum NSItemProviderRepresentationVisibility](nsitemproviderrepresentationvisibility.md)
  Specifications that control which categories of processes can see an item.
- [NSItemProvider.ErrorCode](nsitemprovider/errorcode.md)
  The error codes that describe problems with consuming data from an item provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemproviderreading)*