# ABMutableMultiValue

**Framework**: Address Book  
**Kind**: class

A mutable representation of a property that might have multiple values.

**Availability**:
- macOS ?+

## Declaration

```swift
class ABMutableMultiValue
```

#### Overview

Each value in a multivalue list must be of the same type, and must have an associated predefined or user-defined label, and unique identifier. The labels, however, need not be unique. For example, you can have multiple Home phone numbers. Each multivalue object may have a primary identifier—used as a default value when a label is not provided. For example, a person record may have multiple addresses with the labels Home and Work, where Work is designated as the primary value. Instances of `ABMutableMultiValue` are mutable, see [`ABMultiValue`](abmultivalue.md) for additional methods that access the content of a multivalue list.

The `ABMutableMultiValue` class is “toll-free bridged” with its procedural C opaque-type counterpart. This means that the [`ABMutableMultiValue`](abmutablemultivalueref.md) type is interchangeable in function or method calls with instances of the `ABMutableMultiValue` class.

## Topics

### Adding a value
- [func add(Any!, withLabel: String!) -> String!](abmutablemultivalue/add(_:withlabel:).md)
  Adds a value and its label to a multivalue list.
- [func insert(Any!, withLabel: String!, at: Int) -> String!](abmutablemultivalue/insert(_:withlabel:at:).md)
  Inserts a value and its label at the given index in a multivalue list.
### Replacing values and labels
- [func replaceLabel(at: Int, withLabel: String!) -> Bool](abmutablemultivalue/replacelabel(at:withlabel:).md)
  Replaces the label at the given index.
- [func replace(at: Int, withValue: Any!) -> Bool](abmutablemultivalue/replace(at:withvalue:).md)
  Replaces the value at the given index.
### Removing values
- [func removeAndLabel(at: Int) -> Bool](abmutablemultivalue/removeandlabel(at:).md)
  Removes the value and label at the given index.
### Setting the Primary identifier
- [func setPrimaryIdentifier(String!) -> Bool](abmutablemultivalue/setprimaryidentifier(_:).md)
  Sets the primary value to be the value for the given identifier.

## Relationships

### Inherits From
- [ABMultiValue](abmultivalue.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSFastEnumeration](../Foundation/NSFastEnumeration.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ABPerson](abperson.md)
  An object that encapsulates all information about a person in the Address Book database.
- [class ABGroup](abgroup.md)
  An object that represents a group of records in the Address Book database.
- [class ABMultiValue](abmultivalue.md)
  An immutable representation of a property that might have multiple values.
- [protocol ABImageClient](abimageclient.md)
  Methods for responding to a request to load images associated with a contact.
- [class ABRecord](abrecord-swift.class.md)
  An abstract class that defines the common properties for all Address Book records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmutablemultivalue)*