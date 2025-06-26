# ABImageClient

**Framework**: Address Book  
**Kind**: protocol

Methods for responding to a request to load images associated with a contact.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol ABImageClient : NSObjectProtocol
```

## Topics

### Loading an image
- [func consumeImageData(Data!, forTag: Int)](abimageclient/consumeimagedata(_:fortag:).md)
  Gets the image data for the given tag that was initiated by an asynchronous fetch.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ABPerson](abperson.md)
  An object that encapsulates all information about a person in the Address Book database.
- [class ABGroup](abgroup.md)
  An object that represents a group of records in the Address Book database.
- [class ABMultiValue](abmultivalue.md)
  An immutable representation of a property that might have multiple values.
- [class ABMutableMultiValue](abmutablemultivalue.md)
  A mutable representation of a property that might have multiple values.
- [class ABRecord](abrecord-swift.class.md)
  An abstract class that defines the common properties for all Address Book records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abimageclient)*