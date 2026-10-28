# CFPropertyList

**Framework**: Core Foundation  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias CFPropertyList = CFTypeRef
```

```c
typedef CFTypeRef CFPropertyListRef;
```

## Overview

CFPropertyList provides functions that convert property list objects to and from several serialized formats such as XML. The [`CFPropertyList`](./cfpropertylist.md) type that denotes CFPropertyList objects is an abstract type for property list objects. Depending on the contents of the XML data used to create the property list, `CFPropertyListRef` can be any of the property list objects: CFData, CFString, CFArray, CFDictionary, CFDate, CFBoolean, and CFNumber. Note that if you use a property list to generate XML, the keys of any dictionaries in the property list must be CFString objects.

It is important to understand that CFPropertyList provides an abstraction for all the property list types—you can think of CFPropertyList in object-oriented terms as being the superclass of CFString, CFNumber, CFDictionary, and so on. When a Core Foundation function returns a `CFPropertyListRef`, it means that the value may be any of the property list types. For example, [`CFPreferencesCopyAppValue(_:_:)`](./cfpreferencescopyappvalue%28_,_%29.md) returns a `CFPropertyListRef`. This means that the value returned can be a CFString object, a CFNumber object, a CFDictionary object, and so on again. You can use [`CFGetTypeID(_:)`](./cfgettypeid%28_%29.md) to determine what type of object a property list value is.

You use one of the `CFPropertyListCreate...` functions to create a property list object given an existing property list object, raw XML data (as in a file), or a stream. You can also convert a property list object to XML using the [`CFPropertyListCreateXMLData(_:_:)`](./cfpropertylistcreatexmldata%28_,_%29.md) function. You use the [`CFPropertyListWriteToStream(_:_:_:_:)`](./cfpropertylistwritetostream%28_,_,_,_%29.md) function to write a property list to an output stream, and validate a property list object using the [`CFPropertyListIsValid(_:_:)`](./cfpropertylistisvalid%28_,_%29.md) function. CFPropertyList properly takes care of endian issues—a property list (whether represented by a stream, XML, or a CFData object) created on a PowerPC-based Macintosh is correctly interpreted on an Intel-based Macintosh, and vice versa.

For code examples illustrating how to read and write property list files, see [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i) and in particular [Saving and Restoring Property Lists](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/Articles/Saving.html#//apple_ref/doc/uid/20001175).

## Topics

### Creating a Property List
- [func CFPropertyListCreateWithData(CFAllocator!, CFData!, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!](./cfpropertylistcreatewithdata%28_,_,_,_,_%29.md)
  Creates a property list from a given CFData object.
- [func CFPropertyListCreateWithStream(CFAllocator!, CFReadStream!, CFIndex, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!](./cfpropertylistcreatewithstream%28_,_,_,_,_,_%29.md)
  Create and return a property list with a CFReadStream input.
- [func CFPropertyListCreateDeepCopy(CFAllocator!, CFPropertyList!, CFOptionFlags) -> CFPropertyList!](./cfpropertylistcreatedeepcopy%28_,_,_%29.md)
  Recursively creates a copy of a given property list.
- [func CFPropertyListCreateFromXMLData(CFAllocator!, CFData!, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!](./cfpropertylistcreatefromxmldata%28_,_,_,_%29.md)
  Creates a property list using the specified XML or binary property list data.
- [func CFPropertyListCreateFromStream(CFAllocator!, CFReadStream!, CFIndex, CFOptionFlags, UnsafeMutablePointer<CFPropertyListFormat>!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!](./cfpropertylistcreatefromstream%28_,_,_,_,_,_%29.md)
  Creates a property list using data from a stream.
### Exporting a Property List
- [func CFPropertyListCreateData(CFAllocator!, CFPropertyList!, CFPropertyListFormat, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!](./cfpropertylistcreatedata%28_,_,_,_,_%29.md)
  Returns a CFData object containing a serialized representation of a given property list in a specified format.
- [func CFPropertyListWrite(CFPropertyList!, CFWriteStream!, CFPropertyListFormat, CFOptionFlags, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFIndex](./cfpropertylistwrite%28_,_,_,_,_%29.md)
  Write the bytes of a serialized property list out to a stream.
- [func CFPropertyListCreateXMLData(CFAllocator!, CFPropertyList!) -> Unmanaged<CFData>!](./cfpropertylistcreatexmldata%28_,_%29.md)
  Creates an XML representation of the specified property list.
- [func CFPropertyListWriteToStream(CFPropertyList!, CFWriteStream!, CFPropertyListFormat, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFIndex](./cfpropertylistwritetostream%28_,_,_,_%29.md)
  Writes the bytes of a property list serialization out to a stream.
### Validating a Property List
- [func CFPropertyListIsValid(CFPropertyList!, CFPropertyListFormat) -> Bool](./cfpropertylistisvalid%28_,_%29.md)
  Determines if a property list is valid.
### Data Types
- [struct CFPropertyListMutabilityOptions](./cfpropertylistmutabilityoptions.md)
  Type for flags that determine the degree of mutability of newly created property lists.
### Constants
- [enum CFPropertyListFormat](./cfpropertylistformat.md)
  Specifies the format of a property list.
- [Property List Mutability Options](./property_list_mutability_options.md)
  Option flags that determine the degree of mutability of newly created property lists.
- [Reading and Writing Error Codes](./api-1429999-reading-and-writing-error-codes.md)
  Error codes for property list reading and writing functions such as [`CFPropertyListCreateWithData(_:_:_:_:_:)`](./cfpropertylistcreatewithdata%28_,_,_,_,_%29.md).

## See Also

### Related Documentation
- [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [XML Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFXML/CFXML.html#//apple_ref/doc/uid/10000138i)
### Opaque Types
- [class CFAllocator](./cfallocator.md)
- [class CFArray](./cfarray.md)
- [class CFAttributedString](./cfattributedstring.md)
- [class CFBag](./cfbag.md)
- [class CFBinaryHeap](./cfbinaryheap.md)
- [class CFBitVector](./cfbitvector.md)
- [class CFBoolean](./cfboolean.md)
- [class CFBundle](./cfbundle.md)
- [class CFCalendar](./cfcalendar.md)
- [class CFCharacterSet](./cfcharacterset.md)
- [class CFData](./cfdata.md)
- [class CFDate](./cfdate.md)
- [class CFDateFormatter](./cfdateformatter.md)
- [class CFDictionary](./cfdictionary.md)
- [class CFError](./cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpropertylist)*