# CFPlugInInstanceCreateWithInstanceDataSize(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Not recommended.

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
func CFPlugInInstanceCreateWithInstanceDataSize(_ allocator: CFAllocator!, _ instanceDataSize: CFIndex, _ deallocateInstanceFunction: CFPlugInInstanceDeallocateInstanceDataFunction!, _ factoryName: CFString!, _ getInterfaceFunction: CFPlugInInstanceGetInterfaceFunction!) -> CFPlugInInstance!
```

## See Also

- [func CFPlugInInstanceGetFactoryName(CFPlugInInstance!) -> CFString!](cfplugininstancegetfactoryname(_:).md)
  Not recommended.
- [func CFPlugInInstanceGetInstanceData(CFPlugInInstance!) -> UnsafeMutableRawPointer!](cfplugininstancegetinstancedata(_:).md)
  Not recommended.
- [func CFPlugInInstanceGetInterfaceFunctionTable(CFPlugInInstance!, CFString!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> Bool](cfplugininstancegetinterfacefunctiontable(_:_:_:).md)
  Not recommended.
- [func CFPlugInInstanceGetTypeID() -> CFTypeID](cfplugininstancegettypeid().md)
  Not recommended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfplugininstancecreatewithinstancedatasize(_:_:_:_:_:))*