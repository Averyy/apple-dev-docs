# CFBoolean

**Framework**: Core Foundation  
**Kind**: class  
**Role**: Class

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
class CFBoolean
```

```c
typedef const struct __CFBoolean * CFBooleanRef;
```

#### Overview

CFBoolean objects are used to wrap boolean values for use in Core Foundation property lists and collection types.

## Topics

### CFBoolean Miscellaneous Functions
- [func CFBooleanGetTypeID() -> CFTypeID](./cfbooleangettypeid%28%29.md)
  Returns the Core Foundation type identifier for the CFBoolean opaque type.
- [func CFBooleanGetValue(CFBoolean!) -> Bool](./cfbooleangetvalue%28_%29.md)
  Returns the value of a CFBoolean object as a standard C type `Boolean`.
### Constants
- [Boolean Values](./boolean-values.md)
  CFBoolean evaluates to either true or false values where `kCFBooleanTrue` is the true, and `kCFBooleanFalse` is the false value.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Related Documentation
- [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
### Opaque Types
- [class CFAllocator](./cfallocator.md)
- [class CFArray](./cfarray.md)
- [class CFAttributedString](./cfattributedstring.md)
- [class CFBag](./cfbag.md)
- [class CFBinaryHeap](./cfbinaryheap.md)
- [class CFBitVector](./cfbitvector.md)
- [class CFBundle](./cfbundle.md)
- [class CFCalendar](./cfcalendar.md)
- [class CFCharacterSet](./cfcharacterset.md)
- [class CFData](./cfdata.md)
- [class CFDate](./cfdate.md)
- [class CFDateFormatter](./cfdateformatter.md)
- [class CFDictionary](./cfdictionary.md)
- [class CFError](./cferror.md)
- [class CFFileDescriptor](./cffiledescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfboolean)*