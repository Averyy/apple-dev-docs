# CFPlugInInstanceGetInterfaceFunctionTable(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Not recommended.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFPlugInInstanceGetInterfaceFunctionTable(_ instance: CFPlugInInstance!, _ interfaceName: CFString!, _ ftbl: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> Bool
```

## See Also

- [func CFPlugInInstanceCreateWithInstanceDataSize(CFAllocator!, CFIndex, CFPlugInInstanceDeallocateInstanceDataFunction!, CFString!, CFPlugInInstanceGetInterfaceFunction!) -> CFPlugInInstance!](cfplugininstancecreatewithinstancedatasize(_:_:_:_:_:).md)
  Not recommended.
- [func CFPlugInInstanceGetFactoryName(CFPlugInInstance!) -> CFString!](cfplugininstancegetfactoryname(_:).md)
  Not recommended.
- [func CFPlugInInstanceGetInstanceData(CFPlugInInstance!) -> UnsafeMutableRawPointer!](cfplugininstancegetinstancedata(_:).md)
  Not recommended.
- [func CFPlugInInstanceGetTypeID() -> CFTypeID](cfplugininstancegettypeid().md)
  Not recommended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfplugininstancegetinterfacefunctiontable(_:_:_:))*