# ABPerson

**Framework**: Address Book  
**Kind**: class  
**Role**: Class

An object that encapsulates all information about a person in the Address Book database.

**Availability**:
- macOS

## Declaration

```swift
class ABPerson
```

```objc
@interface ABPerson : ABRecord
```

#### Overview

An `ABPerson` object corresponds to a single person record in the database. A person object contains the person’s name, company, address, email addresses, and phone numbers.

The `ABPerson` class is “toll-free bridged” with its procedural C opaque-type counterpart. This means that the `ABPersonRef` type is interchangeable in function or method calls with instances of the `ABPerson` class.

## Topics

### Managing Properties
- [class func addPropertiesAndTypes([AnyHashable : Any]!) -> Int](./abperson/addpropertiesandtypes%28_%29.md)
  Adds the given properties to all the records of this type in the Address Book database.
- [class func removeProperties([Any]!) -> Int](./abperson/removeproperties%28_%29.md)
  Removes the given properties from all the records of this type in the Address Book database.
- [class func properties() -> [Any]!](./abperson/properties%28%29.md)
  Returns an array of  the names of all the properties for the record in the Address Book database.
- [class func type(ofProperty: String!) -> ABPropertyType](./abperson/type%28ofproperty%29.md)
  Returns the type of a given property.
### Managing Linked People
- [func linkedPeople() -> [Any]!](./abperson/linkedpeople%28%29.md)
  Returns the array of all person records that are linked to the person this record represents.
### Managing Groups
- [func parentGroups() -> [Any]!](./abperson/parentgroups%28%29.md)
  Returns an array of the address book groups that this person belongs to.
### Managing Images
- [class func cancelLoadingImageData(forTag: Int)](./abperson/cancelloadingimagedata%28fortag%29.md)
  Cancels an asynchronous fetch of the images for a given tag.
- [func beginLoadingImageData(for: (any ABImageClient)!) -> Int](./abperson/beginloadingimagedata%28for%29.md)
  Starts an asynchronous fetch for image data in all locations
- [func imageData() -> Data!](./abperson/imagedata%28%29.md)
  Returns data that contains a picture of this person.
- [func setImageData(Data!) -> Bool](./abperson/setimagedata%28_%29.md)
  Sets the image for this person to the given data.
### Searching
- [class func searchElement(forProperty: String!, label: String!, key: String!, value: Any!, comparison: ABSearchComparison) -> ABSearchElement!](./abperson/searchelement%28forproperty,label,key,value,comparison%29.md)
  Returns a search element object that specifies a query for records of this type.
### Importing and Exporting vCard Formatted Files
- [init!(VCardRepresentation: Data!)](./abperson/init%28vcardrepresentation%29-5c7h8.md)
  Returns an `ABPerson` instance initialized with the given data.
- [func vCardRepresentation() -> Data!](./abperson/vcardrepresentation%28%29.md)
  Returns the vCard representation of the person record as a data object in vCard format.
### Constants
- [Person Flags](./person-flags.md)
  Settings that determine how person records are displayed.
### Initializers
- [init!(vCardRepresentation: Data!)](./abperson/init%28vcardrepresentation%29-1bqog.md)
### Default Implementations
- [ABPerson Implementations](./abperson/abperson-implementations.md)

## Relationships

### Inherits From
- [ABRecord](./abrecord-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Data Types
- [class ABGroup](./abgroup.md)
  An object that represents a group of records in the Address Book database.
- [class ABMultiValue](./abmultivalue-swift.class.md)
  An immutable representation of a property that might have multiple values.
- [class ABMutableMultiValue](./abmutablemultivalue-swift.class.md)
  A mutable representation of a property that might have multiple values.
- [protocol ABImageClient](./abimageclient.md)
  Methods for responding to a request to load images associated with a contact.
- [class ABRecord](./abrecord-swift.class.md)
  An abstract class that defines the common properties for all Address Book records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abperson)*