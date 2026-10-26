# Property List Mutability Options

**Framework**: Core Foundation  
**Role**: API Collection

Option flags that determine the degree of mutability of newly created property lists.

## Topics

### Constants
- [static var mutableContainers: CFPropertyListMutabilityOptions](./cfpropertylistmutabilityoptions/mutablecontainers.md)
  Specifies that the property list should have mutable containers but immutable leaves.
- [static var mutableContainersAndLeaves: CFPropertyListMutabilityOptions](./cfpropertylistmutabilityoptions/mutablecontainersandleaves.md)
  Specifies that the property list should have mutable containers and mutable leaves.
- [kCFPropertyListImmutable](./cfpropertylistmutabilityoptions/kcfpropertylistimmutable.md)
  Specifies that the property list should be immutable.

## See Also

### Constants
- [enum CFPropertyListFormat](./cfpropertylistformat.md)
  Specifies the format of a property list.
- [Reading and Writing Error Codes](./api-1429999-reading-and-writing-error-codes.md)
  Error codes for property list reading and writing functions such as [`CFPropertyListCreateWithData(_:_:_:_:_:)`](./cfpropertylistcreatewithdata%28_,_,_,_,_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/property_list_mutability_options)*