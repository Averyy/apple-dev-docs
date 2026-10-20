# Reading and Writing Error Codes

**Framework**: Core Foundation  
**Role**: API Collection

Error codes for property list reading and writing functions such as [`CFPropertyListCreateWithData(_:_:_:_:_:)`](./cfpropertylistcreatewithdata%28_,_,_,_,_%29.md).

## Topics

### Constants
- [var kCFPropertyListReadCorruptError: CFIndex](./kcfpropertylistreadcorrupterror.md)
  Signifies an error parsing a property list.
- [var kCFPropertyListReadUnknownVersionError: CFIndex](./kcfpropertylistreadunknownversionerror.md)
  Signifies the version number in the property list is unknown.
- [var kCFPropertyListReadStreamError: CFIndex](./kcfpropertylistreadstreamerror.md)
  Signifies a stream error reading a property list.
- [var kCFPropertyListWriteStreamError: CFIndex](./kcfpropertylistwritestreamerror.md)
  Signifies a stream error writing a property list.

## See Also

### Constants
- [enum CFPropertyListFormat](./cfpropertylistformat.md)
  Specifies the format of a property list.
- [Property List Mutability Options](./property_list_mutability_options.md)
  Option flags that determine the degree of mutability of newly created property lists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/1429999-reading-and-writing-error-codes)*