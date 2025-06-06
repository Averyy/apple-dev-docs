# CFMutableDictionary

**Framework**: Core Foundation  
**Kind**: class

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CFMutableDictionary
```

#### Overview

CFMutableDictionary manages dynamic dictionaries. The basic interface for managing dictionaries is provided by [`CFDictionary`](cfdictionary.md). CFMutableDictionary adds functions to modify the contents of a dictionary.

You create a mutable dictionary object using either the [`CFDictionaryCreateMutable(_:_:_:_:)`](cfdictionarycreatemutable(_:_:_:_:).md) or [`CFDictionaryCreateMutableCopy(_:_:_:)`](cfdictionarycreatemutablecopy(_:_:_:).md) function. You can add key-value pairs using the [`CFDictionaryAddValue(_:_:_:)`](cfdictionaryaddvalue(_:_:_:).md) and [`CFDictionarySetValue(_:_:_:)`](cfdictionarysetvalue(_:_:_:).md) functions. When adding key-value pairs to a dictionary, the keys and values are not copied—they are retained so they are not invalidated before the dictionary is deallocated. You can remove key-value pairs using the [`CFDictionaryRemoveValue(_:_:)`](cfdictionaryremovevalue(_:_:).md) function. When removing key-value pairs from a dictionary, the keys and values are released.

CFMutableDictionary is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSMutableDictionary`](https://developer.apple.com/documentation/Foundation/NSMutableDictionary). What this means is that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. This means that in a method where you see an `NSMutableDictionary *` parameter, you can pass in a `CFMutableDictionaryRef`, and in a function where you see a `CFMutableDictionaryRef` parameter, you can pass in an NSMutableDictionary instance. This also applies to concrete subclasses of NSMutableDictionary. See [`Toll-Free Bridged Types`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### Creating a Mutable Dictionary
- [func CFDictionaryCreateMutable(CFAllocator!, CFIndex, UnsafePointer<CFDictionaryKeyCallBacks>!, UnsafePointer<CFDictionaryValueCallBacks>!) -> CFMutableDictionary!](cfdictionarycreatemutable(_:_:_:_:).md)
  Creates a new mutable dictionary.
- [func CFDictionaryCreateMutableCopy(CFAllocator!, CFIndex, CFDictionary!) -> CFMutableDictionary!](cfdictionarycreatemutablecopy(_:_:_:).md)
  Creates a new mutable dictionary with the key-value pairs from another dictionary.
### Modifying a Dictionary
- [func CFDictionaryAddValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](cfdictionaryaddvalue(_:_:_:).md)
  Adds a key-value pair to a dictionary if the specified key is not already present.
- [func CFDictionaryRemoveAllValues(CFMutableDictionary!)](cfdictionaryremoveallvalues(_:).md)
  Removes all the key-value pairs from a dictionary, making it empty.
- [func CFDictionaryRemoveValue(CFMutableDictionary!, UnsafeRawPointer!)](cfdictionaryremovevalue(_:_:).md)
  Removes a key-value pair.
- [func CFDictionaryReplaceValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](cfdictionaryreplacevalue(_:_:_:).md)
  Replaces a value corresponding to a given key.
- [func CFDictionarySetValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](cfdictionarysetvalue(_:_:_:).md)
  Sets the value corresponding to a given key.

## Relationships

### Inherits From
- [CFDictionary](cfdictionary.md)
### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Property List Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [Collections Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/CFCollections.html#//apple_ref/doc/uid/10000124i)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmutabledictionary)*