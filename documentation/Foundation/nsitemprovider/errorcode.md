# NSItemProvider.ErrorCode

**Framework**: Foundation  
**Kind**: enum

The error codes that describe problems with consuming data from an item provider.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum ErrorCode
```

## Topics

### Constants
- [NSItemProvider.ErrorCode.itemUnavailableError](nsitemprovider/errorcode/itemunavailableerror.md)
  An error code indicating that the requested data was unavailable from an item provider.
- [NSItemProvider.ErrorCode.unavailableCoercionError](nsitemprovider/errorcode/unavailablecoercionerror.md)
  An error code indicating that the requested data type coercion is unavailable from an item provider.
- [NSItemProvider.ErrorCode.unexpectedValueClassError](nsitemprovider/errorcode/unexpectedvalueclasserror.md)
  An error code indicating that type coercion to the requested class failed.
- [NSItemProvider.ErrorCode.unknownError](nsitemprovider/errorcode/unknownerror.md)
  An error code indicating an unknown error with consuming data from an item provider.
### Initializers
- [init?(rawValue: Int)](nsitemprovider/errorcode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [protocol NSItemProviderWriting](nsitemproviderwriting.md)
  The protocol for implementing a class to allow an item provider to retrieve data from an instance of the class.
- [enum NSItemProviderRepresentationVisibility](nsitemproviderrepresentationvisibility.md)
  Specifications that control which categories of processes can see an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/errorcode)*