# ABMultiValue

**Framework**: Address Book  
**Kind**: class

An immutable representation of a property that might have multiple values.

**Availability**:
- macOS ?+

## Declaration

```swift
class ABMultiValue
```

#### Overview

Each value in a multivalue list must be of the same type, and must have an associated predefined or user-defined label, and unique identifier. The labels, however, need not be unique. For example, you can have multiple Home phone numbers. Each multivalue object may have a primary identifier—used as a default value when a label is not provided. For example, a person record may have multiple addresses with the labels Home and Work, where Work is designated as the primary value. Instances of this class are immutable, see [`ABMutableMultiValue`](abmutablemultivalue-swift.class.md) for methods that manipulate the content of a multivalue list.

The `ABMultiValue` class is “toll-free bridged” with its procedural C opaque-type counterpart. This means that the [`ABMultiValue`](abmultivalue-swift.typealias.md) type is interchangeable in function or method calls with instances of the `ABMultiValue` class.

## Topics

### Accessing the primary identifier
- [func primaryIdentifier() -> String!](abmultivalue-swift.class/primaryidentifier.md)
  Returns the identifier for the primary value.
### Accessing identifiers
- [func identifier(at: Int) -> String!](abmultivalue-swift.class/identifier(at:).md)
  Returns the identifier for the given index.
- [func index(forIdentifier: String!) -> Int](abmultivalue-swift.class/index(foridentifier:).md)
  Returns the index for the given identifier.
### Accessing entries
- [func label(at: Int) -> String!](abmultivalue-swift.class/label(at:).md)
  Returns the label for the given index.
- [func value(at: Int) -> Any!](abmultivalue-swift.class/value(at:).md)
  Returns the value for the given index.
- [func value(forIdentifier: String!) -> Any!](abmultivalue-swift.class/value(foridentifier:).md)
  Returns the value for the given identifier.
- [func label(forIdentifier: String!) -> Any!](abmultivalue-swift.class/label(foridentifier:).md)
  Returns the label for the given identifier.
### Querying the list
- [func count() -> Int](abmultivalue-swift.class/count.md)
  Returns the number of entries in a multivalue list.
- [func propertyType() -> ABPropertyType](abmultivalue-swift.class/propertytype.md)
  Returns the type for the values in a multivalue list.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [ABMutableMultiValue](abmutablemultivalue-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSFastEnumeration](../foundation/nsfastenumeration.md)
- [NSMutableCopying](../foundation/nsmutablecopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class ABPerson](abperson.md)
  An object that encapsulates all information about a person in the Address Book database.
- [class ABGroup](abgroup.md)
  An object that represents a group of records in the Address Book database.
- [class ABMutableMultiValue](abmutablemultivalue-swift.class.md)
  A mutable representation of a property that might have multiple values.
- [protocol ABImageClient](abimageclient.md)
  Methods for responding to a request to load images associated with a contact.
- [class ABRecord](abrecord-swift.class.md)
  An abstract class that defines the common properties for all Address Book records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalue-swift.class)*