# CFPlugInInstance

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
class CFPlugInInstance
```

```c
typedef struct __CFPlugInInstance * CFPlugInInstanceRef;
```

## Overview

CFPlugInInstance is deprecated. Use the functions defined by [`CFPlugIn`](./cfplugin.md) instead.

## Topics

### Deprecated
- [func CFPlugInInstanceCreateWithInstanceDataSize(CFAllocator!, CFIndex, CFPlugInInstanceDeallocateInstanceDataFunction!, CFString!, CFPlugInInstanceGetInterfaceFunction!) -> CFPlugInInstance!](./cfplugininstancecreatewithinstancedatasize%28_,_,_,_,_%29.md)
  Not recommended.
- [func CFPlugInInstanceGetFactoryName(CFPlugInInstance!) -> CFString!](./cfplugininstancegetfactoryname%28_%29.md)
  Not recommended.
- [func CFPlugInInstanceGetInstanceData(CFPlugInInstance!) -> UnsafeMutableRawPointer!](./cfplugininstancegetinstancedata%28_%29.md)
  Not recommended.
- [func CFPlugInInstanceGetInterfaceFunctionTable(CFPlugInInstance!, CFString!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> Bool](./cfplugininstancegetinterfacefunctiontable%28_,_,_%29.md)
  Not recommended.
- [func CFPlugInInstanceGetTypeID() -> CFTypeID](./cfplugininstancegettypeid%28%29.md)
  Not recommended.
### Callbacks
- [typealias CFPlugInInstanceDeallocateInstanceDataFunction](./cfplugininstancedeallocateinstancedatafunction.md)
  Not recommended.
- [typealias CFPlugInInstanceGetInterfaceFunction](./cfplugininstancegetinterfacefunction.md)
  Not recommended.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfplugininstance)*