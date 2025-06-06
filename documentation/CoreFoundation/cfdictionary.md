# CFDictionary

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
class CFDictionary
```

#### Overview

CFDictionary and its derived mutable type, [`CFMutableDictionary`](cfmutabledictionary.md), manage associations of key-value pairs. CFDictionary creates static dictionaries where you set the key-value pairs when first creating a dictionary and cannot modify them afterward; CFMutableDictionary creates dynamic dictionaries where you can add or delete key-value pairs at any time, and the dictionary automatically allocates memory as needed.

A key-value pair within a dictionary is called an entry. Each entry consists of one object that represents the key and a second object that is that key’s value. Within a dictionary, the keys are unique. That is, no two keys in a single dictionary are equal (as determined by the equal callback). Internally, a dictionary uses a hash table to organize its storage and to provide rapid access to a value given the corresponding key.

Keys for a CFDictionary may be of any C type, however note that if you want to convert a CFPropertyList to XML, any dictionary’s keys must be CFString objects.

You create static dictionaries using either the [`CFDictionaryCreate(_:_:_:_:_:_:)`](cfdictionarycreate(_:_:_:_:_:_:).md) or [`CFDictionaryCreateCopy(_:_:)`](cfdictionarycreatecopy(_:_:).md) function. Key-value pairs are passed as parameters to [`CFDictionaryCreate(_:_:_:_:_:_:)`](cfdictionarycreate(_:_:_:_:_:_:).md). When adding key-value pairs to a dictionary, the keys and values are not copied—they are retained so they are not invalidated before the dictionary is deallocated.

CFDictionary provides functions for querying the values of a dictionary. The function [`CFDictionaryGetCount(_:)`](cfdictionarygetcount(_:).md) returns the number of key-value pairs in a dictionary; the [`CFDictionaryContainsValue(_:_:)`](cfdictionarycontainsvalue(_:_:).md) function checks if a value is in a dictionary; and [`CFDictionaryGetKeysAndValues(_:_:_:)`](cfdictionarygetkeysandvalues(_:_:_:).md) returns a C array containing all the values and a C array containing all the keys in a dictionary.

The [`CFDictionaryApplyFunction(_:_:_:)`](cfdictionaryapplyfunction(_:_:_:).md) function lets you apply a function to all key-value pairs in a dictionary.

CFDictionary is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSDictionary *` parameter, you can pass in a `CFDictionaryRef`, and in a function where you see a `CFDictionaryRef` parameter, you can pass in an NSDictionary instance. This also applies to concrete subclasses of NSDictionary. See [`Toll-Free Bridged Types`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### Creating a dictionary
- [func CFDictionaryCreate(CFAllocator!, UnsafeMutablePointer<UnsafeRawPointer?>!, UnsafeMutablePointer<UnsafeRawPointer?>!, CFIndex, UnsafePointer<CFDictionaryKeyCallBacks>!, UnsafePointer<CFDictionaryValueCallBacks>!) -> CFDictionary!](cfdictionarycreate(_:_:_:_:_:_:).md)
  Creates an immutable dictionary containing the specified key-value pairs.
- [func CFDictionaryCreateCopy(CFAllocator!, CFDictionary!) -> CFDictionary!](cfdictionarycreatecopy(_:_:).md)
  Creates and returns a new immutable dictionary with the key-value pairs of another dictionary.
### Examining a dictionary
- [func CFDictionaryContainsKey(CFDictionary!, UnsafeRawPointer!) -> Bool](cfdictionarycontainskey(_:_:).md)
  Returns a Boolean value that indicates whether a given key is in a dictionary.
- [func CFDictionaryContainsValue(CFDictionary!, UnsafeRawPointer!) -> Bool](cfdictionarycontainsvalue(_:_:).md)
  Returns a Boolean value that indicates whether a given value is in a dictionary.
- [func CFDictionaryGetCount(CFDictionary!) -> CFIndex](cfdictionarygetcount(_:).md)
  Returns the number of key-value pairs in a dictionary.
- [func CFDictionaryGetCountOfKey(CFDictionary!, UnsafeRawPointer!) -> CFIndex](cfdictionarygetcountofkey(_:_:).md)
  Returns the number of times a key occurs in a dictionary.
- [func CFDictionaryGetCountOfValue(CFDictionary!, UnsafeRawPointer!) -> CFIndex](cfdictionarygetcountofvalue(_:_:).md)
  Counts the number of times a given value occurs in the dictionary.
- [func CFDictionaryGetKeysAndValues(CFDictionary!, UnsafeMutablePointer<UnsafeRawPointer?>!, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfdictionarygetkeysandvalues(_:_:_:).md)
  Fills two buffers with the keys and values from a dictionary.
- [func CFDictionaryGetValue(CFDictionary!, UnsafeRawPointer!) -> UnsafeRawPointer!](cfdictionarygetvalue(_:_:).md)
  Returns the value associated with a given key.
- [func CFDictionaryGetValueIfPresent(CFDictionary!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](cfdictionarygetvalueifpresent(_:_:_:).md)
  Returns a Boolean value that indicates whether a given value for a given key is in a dictionary, and returns that value indirectly if it exists.
### Applying a function to a dictionary
- [func CFDictionaryApplyFunction(CFDictionary!, ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, UnsafeMutableRawPointer!)](cfdictionaryapplyfunction(_:_:_:).md)
  Calls a function once for each key-value pair in a dictionary.
### Getting the CFDictionary type ID
- [func CFDictionaryGetTypeID() -> CFTypeID](cfdictionarygettypeid().md)
  Returns the type identifier for the CFDictionary opaque type.
### Callbacks
- [typealias CFDictionaryApplierFunction](cfdictionaryapplierfunction.md)
  Prototype of a callback function that may be applied to every key-value pair in a dictionary.
- [typealias CFDictionaryCopyDescriptionCallBack](cfdictionarycopydescriptioncallback.md)
  Prototype of a callback function used to get a description of a value or key in a dictionary.
- [typealias CFDictionaryEqualCallBack](cfdictionaryequalcallback.md)
  Prototype of a callback function used to determine if two values or keys in a dictionary are equal.
- [typealias CFDictionaryHashCallBack](cfdictionaryhashcallback.md)
  Prototype of a callback function invoked to compute a hash code for a key. Hash codes are used when key-value pairs are accessed, added, or removed from a collection.
- [typealias CFDictionaryReleaseCallBack](cfdictionaryreleasecallback.md)
  Prototype of a callback function used to release a key-value pair before it’s removed from a dictionary.
- [typealias CFDictionaryRetainCallBack](cfdictionaryretaincallback.md)
  Prototype of a callback function used to retain a value or key being added to a dictionary.
### Data Types
- [struct CFDictionaryKeyCallBacks](cfdictionarykeycallbacks.md)
  This structure contains the callbacks used to retain, release, describe, and compare the keys in a dictionary.
- [struct CFDictionaryValueCallBacks](cfdictionaryvaluecallbacks.md)
  This structure contains the callbacks used to retain, release, describe, and compare the values in a dictionary.
### Constants
- [Predefined Callback Structures](cfdictionary-predefined-callback-structures.md)
  CFDictionary provides some predefined callbacks for your convenience.

## Relationships

### Inherited By
- [CFMutableDictionary](cfmutabledictionary.md)
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
- [class CFError](cferror.md)
- [class CFFileDescriptor](cffiledescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionary)*