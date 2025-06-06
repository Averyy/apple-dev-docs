# NSItemProviderWriting

**Framework**: Foundation  
**Kind**: protocol

The protocol for implementing a class to allow an item provider to retrieve data from an instance of the class.

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
protocol NSItemProviderWriting : NSObjectProtocol
```

#### Overview

A source app uses an object that conforms to this protocol to initialize an item provider for a copied or dragged item.

## Topics

### Loading data
- [func loadData(withTypeIdentifier: String, forItemProviderCompletionHandler: (Data?, (any Error)?) -> Void) -> Progress?](nsitemproviderwriting/loaddata(withtypeidentifier:foritemprovidercompletionhandler:).md)
  Loads data of a particular type, identified by the given UTI.
### Getting the writable type identifiers
- [static var writableTypeIdentifiersForItemProvider: [String]](nsitemproviderwriting/writabletypeidentifiersforitemprovider-swift.type.property.md)
  An array of UTI strings representing the types of data that can be loaded for an item provider.
- [var writableTypeIdentifiersForItemProvider: [String]](nsitemproviderwriting/writabletypeidentifiersforitemprovider-swift.property.md)
  An array of UTI strings representing the types of data that can be loaded for an item provider.
### Getting the representation visibility specification
- [static func itemProviderVisibilityForRepresentation(withTypeIdentifier: String) -> NSItemProviderRepresentationVisibility](nsitemproviderwriting/itemprovidervisibilityforrepresentation(withtypeidentifier:)-swift.type.method.md)
  Asks the item provider for the default representation visibility specification for the given UTI.
- [func itemProviderVisibilityForRepresentation(withTypeIdentifier: String) -> NSItemProviderRepresentationVisibility](nsitemproviderwriting/itemprovidervisibilityforrepresentation(withtypeidentifier:)-swift.method.md)
  Asks the item provider for the representation visibility specification for the given UTI.

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
- [protocol NSItemProviderReading](nsitemproviderreading.md)
  The protocol for implementing a class to allow an item provider to create an instance of the class.
- [enum NSItemProviderRepresentationVisibility](nsitemproviderrepresentationvisibility.md)
  Specifications that control which categories of processes can see an item.
- [NSItemProvider.ErrorCode](nsitemprovider/errorcode.md)
  The error codes that describe problems with consuming data from an item provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemproviderwriting)*