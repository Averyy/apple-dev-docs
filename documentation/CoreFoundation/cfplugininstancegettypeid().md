# CFPlugInInstanceGetTypeID()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Not recommended.

**Availability**:
- iOS 2.0+ - Deprecated in 27.0
- iPadOS 2.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.0+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.0

> **Deprecated**: Use UUID-based plugins instead

## Declaration

```swift
func CFPlugInInstanceGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CFPlugInInstanceGetTypeID();
```

## See Also

### Deprecated
- [func CFPlugInInstanceCreateWithInstanceDataSize(CFAllocator!, CFIndex, CFPlugInInstanceDeallocateInstanceDataFunction!, CFString!, CFPlugInInstanceGetInterfaceFunction!) -> CFPlugInInstance!](./cfplugininstancecreatewithinstancedatasize%28_,_,_,_,_%29.md)
  Not recommended.
- [func CFPlugInInstanceGetFactoryName(CFPlugInInstance!) -> CFString!](./cfplugininstancegetfactoryname%28_%29.md)
  Not recommended.
- [func CFPlugInInstanceGetInstanceData(CFPlugInInstance!) -> UnsafeMutableRawPointer!](./cfplugininstancegetinstancedata%28_%29.md)
  Not recommended.
- [func CFPlugInInstanceGetInterfaceFunctionTable(CFPlugInInstance!, CFString!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> Bool](./cfplugininstancegetinterfacefunctiontable%28_,_,_%29.md)
  Not recommended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfplugininstancegettypeid())*