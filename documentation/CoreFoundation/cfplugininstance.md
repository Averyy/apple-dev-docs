# CFPlugInInstance

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
class CFPlugInInstance
```

#### Overview

CFPlugInInstance is deprecated. Use the functions defined by [`CFPlugIn`](cfplugin.md) instead.

## Topics

### Deprecated
- [func CFPlugInInstanceCreateWithInstanceDataSize(CFAllocator!, CFIndex, CFPlugInInstanceDeallocateInstanceDataFunction!, CFString!, CFPlugInInstanceGetInterfaceFunction!) -> CFPlugInInstance!](cfplugininstancecreatewithinstancedatasize(_:_:_:_:_:).md)
  Not recommended.
- [func CFPlugInInstanceGetFactoryName(CFPlugInInstance!) -> CFString!](cfplugininstancegetfactoryname(_:).md)
  Not recommended.
- [func CFPlugInInstanceGetInstanceData(CFPlugInInstance!) -> UnsafeMutableRawPointer!](cfplugininstancegetinstancedata(_:).md)
  Not recommended.
- [func CFPlugInInstanceGetInterfaceFunctionTable(CFPlugInInstance!, CFString!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> Bool](cfplugininstancegetinterfacefunctiontable(_:_:_:).md)
  Not recommended.
- [func CFPlugInInstanceGetTypeID() -> CFTypeID](cfplugininstancegettypeid().md)
  Not recommended.
### Callbacks
- [typealias CFPlugInInstanceDeallocateInstanceDataFunction](cfplugininstancedeallocateinstancedatafunction.md)
  Not recommended.
- [typealias CFPlugInInstanceGetInterfaceFunction](cfplugininstancegetinterfacefunction.md)
  Not recommended.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfplugininstance)*