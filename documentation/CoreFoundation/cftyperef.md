# CFTypeRef

**Framework**: Core Foundation  
**Kind**: typealias  
**Role**: Type Alias

An untyped “generic” reference to any Core Foundation object.

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
typealias CFTypeRef = AnyObject
```

```c
typedef const void * CFTypeRef;
```

#### Discussion

All other Core Foundation opaque types derive from `CFTypeRef`. The functions, callbacks, data types, and constants defined for CFType can be used by any derived opaque type. Hence, `CFTypeRef` functions are referred to as “polymorphic functions.” You use `CFTypeRef` functions to retain and release objects, to compare and inspect objects, get descriptions of objects and opaque types, and to get object allocators.

## Topics

### Memory Management
- [func CFGetAllocator(CFTypeRef!) -> CFAllocator!](./cfgetallocator%28_%29.md)
  Returns the allocator used to allocate a Core Foundation object.
- [func CFGetRetainCount(CFTypeRef!) -> CFIndex](./cfgetretaincount%28_%29.md)
  Returns the reference count of a Core Foundation object.
### Determining Equality
- [func CFEqual(CFTypeRef!, CFTypeRef!) -> Bool](./cfequal%28_,_%29.md)
  Determines whether two Core Foundation objects are considered equal.
### Hashing
- [func CFHash(CFTypeRef!) -> CFHashCode](./cfhash%28_%29.md)
  Returns a code that can be used to identify an object in a hashing structure.
### Miscellaneous Functions
- [func CFCopyDescription(CFTypeRef!) -> CFString!](./cfcopydescription%28_%29.md)
  Returns a textual description of a Core Foundation object.
- [func CFCopyTypeIDDescription(CFTypeID) -> CFString!](./cfcopytypeiddescription%28_%29.md)
  Returns a textual description of a Core Foundation type, as identified by its type ID, which can be used when debugging.
- [func CFGetTypeID(CFTypeRef!) -> CFTypeID](./cfgettypeid%28_%29.md)
  Returns the unique identifier of an opaque type to which a Core Foundation object belongs.
- [func CFShow(CFTypeRef!)](./cfshow%28_%29.md)
  Prints a description of a Core Foundation object to stderr.
### Data Types
- [typealias CFHashCode](./cfhashcode.md)
  A type for hash codes returned by the `CFHash` function.
- [typealias CFTypeID](./cftypeid.md)
  A type for unique, constant integer values that identify particular Core Foundation opaque types.

## See Also

### Related Documentation
- [Memory Management Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i)
- [Core Foundation Design Concepts](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/CFDesignConcepts.html#//apple_ref/doc/uid/10000122i)
### Data Types
- [typealias CFAllocatorTypeID](./cfallocatortypeid.md)
- [struct CFCalendarIdentifier](./cfcalendaridentifier.md)
- [struct CFDateFormatterKey](./cfdateformatterkey.md)
- [typealias CFErrorDomain](./cferrordomain.md)
- [struct CFLocaleIdentifier](./cflocaleidentifier.md)
- [struct CFLocaleKey](./cflocalekey.md)
- [struct CFNotificationName](./cfnotificationname.md)
- [struct CFNumberFormatterKey](./cfnumberformatterkey.md)
- [struct CFRunLoopMode](./cfrunloopmode.md)
- [struct CFStreamPropertyKey](./cfstreampropertykey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftyperef)*