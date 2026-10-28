# ABGroup

**Framework**: Address Book  
**Kind**: class  
**Role**: Class

An object that represents a group of records in the Address Book database.

**Availability**:
- macOS

## Declaration

```swift
class ABGroup
```

```objc
@interface ABGroup : ABRecord
```

## Overview

The `ABGroup` class supports the concept of a “group” containing one or more persons. People may belong to multiple groups, and groups may also belong to other groups unless the relationship causes a circular reference. The only predefined property of a group is its name. However, similar to person records, you can add your own properties to group records. Groups not only help to organize person records, but also allow you to create email distribution lists.

The `ABGroup` class is “toll-free bridged” with its procedural C opaque-type counterpart. This means that the `ABGroupRef` type is interchangeable in function or method calls with instances of the `ABGroup` class.

## Topics

### Managing properties
- [class func addPropertiesAndTypes([AnyHashable : Any]!) -> Int](./abgroup/addpropertiesandtypes%28_%29.md)
  Adds the given properties to all records of this type in the Address Book database.
- [class func removeProperties([Any]!) -> Int](./abgroup/removeproperties%28_%29.md)
  Removes the given properties from all the records of this type in the Address Book database.
- [class func properties() -> [Any]!](./abgroup/properties%28%29.md)
  Returns an array of the names of all the properties for this record type in the Address Book database.
- [class func type(ofProperty: String!) -> ABPropertyType](./abgroup/type%28ofproperty%29.md)
  Returns the type for a given property.
### Managing persons
- [func addMember(ABPerson!) -> Bool](./abgroup/addmember%28_%29.md)
  Adds a person to a group.
- [func removeMember(ABPerson!) -> Bool](./abgroup/removemember%28_%29.md)
  Removes a person from a group.
- [func members() -> [Any]!](./abgroup/members%28%29.md)
  Returns an array of persons in a group.
### Managing subgroups
- [func addSubgroup(ABGroup!) -> Bool](./abgroup/addsubgroup%28_%29.md)
  Adds a subgroup to another group.
- [func removeSubgroup(ABGroup!) -> Bool](./abgroup/removesubgroup%28_%29.md)
  Removes a subgroup from a group.
- [func parentGroups() -> [Any]!](./abgroup/parentgroups%28%29.md)
  Returns an array containing a group’s parents—that is, the groups that a group belongs to.
- [func subgroups() -> [Any]!](./abgroup/subgroups%28%29.md)
  Returns an array containing a group’s subgroups.
### Managing Distribution Lists
- [func distributionIdentifier(forProperty: String!, person: ABPerson!) -> String!](./abgroup/distributionidentifier%28forproperty,person%29.md)
  Returns the distribution identifier for the given property and person.
- [func setDistributionIdentifier(String!, forProperty: String!, person: ABPerson!) -> Bool](./abgroup/setdistributionidentifier%28_,forproperty,person%29.md)
  Assigns a specific distribution identifier for a person’s multivalue list property so that the group can be used as a distribution list.
### Searching
- [class func searchElement(forProperty: String!, label: String!, key: String!, value: Any!, comparison: ABSearchComparison) -> ABSearchElement!](./abgroup/searchelement%28forproperty,label,key,value,comparison%29.md)
  Returns a search element object that searches for records of this type.

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
- [class ABPerson](./abperson.md)
  An object that encapsulates all information about a person in the Address Book database.
- [class ABMultiValue](./abmultivalue-swift.class.md)
  An immutable representation of a property that might have multiple values.
- [class ABMutableMultiValue](./abmutablemultivalue-swift.class.md)
  A mutable representation of a property that might have multiple values.
- [protocol ABImageClient](./abimageclient.md)
  Methods for responding to a request to load images associated with a contact.
- [class ABRecord](./abrecord-swift.class.md)
  An abstract class that defines the common properties for all Address Book records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup)*