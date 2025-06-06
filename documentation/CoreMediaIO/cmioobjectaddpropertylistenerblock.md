# CMIOObjectAddPropertyListenerBlock(_:_:_:_:)

**Framework**: Core Media I/O  
**Kind**: func

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
func CMIOObjectAddPropertyListenerBlock(_ objectID: CMIOObjectID, _ address: UnsafePointer<CMIOObjectPropertyAddress>!, _ dispatchQueue: dispatch_queue_t!, _ listener: CMIOObjectPropertyListenerBlock!) -> OSStatus
```

## See Also

- [func CMIODeviceProcessAVCCommand(CMIODeviceID, UnsafeMutablePointer<CMIODeviceAVCCommand>!) -> OSStatus](cmiodeviceprocessavccommand(_:_:).md)
- [func CMIODeviceProcessRS422Command(CMIODeviceID, UnsafeMutablePointer<CMIODeviceRS422Command>!) -> OSStatus](cmiodeviceprocessrs422command(_:_:).md)
- [func CMIODeviceStartStream(CMIODeviceID, CMIOStreamID) -> OSStatus](cmiodevicestartstream(_:_:).md)
- [func CMIODeviceStopStream(CMIODeviceID, CMIOStreamID) -> OSStatus](cmiodevicestopstream(_:_:).md)
- [func CMIOObjectAddPropertyListener(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!, CMIOObjectPropertyListenerProc!, UnsafeMutableRawPointer!) -> OSStatus](cmioobjectaddpropertylistener(_:_:_:_:).md)
- [func CMIOObjectGetPropertyData(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!, UInt32, UnsafeRawPointer!, UInt32, UnsafeMutablePointer<UInt32>!, UnsafeMutableRawPointer!) -> OSStatus](cmioobjectgetpropertydata(_:_:_:_:_:_:_:).md)
- [func CMIOObjectGetPropertyDataSize(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!, UInt32, UnsafeRawPointer!, UnsafeMutablePointer<UInt32>!) -> OSStatus](cmioobjectgetpropertydatasize(_:_:_:_:_:).md)
- [func CMIOObjectHasProperty(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!) -> Bool](cmioobjecthasproperty(_:_:).md)
- [func CMIOObjectIsPropertySettable(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!, UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus](cmioobjectispropertysettable(_:_:_:).md)
- [func CMIOObjectRemovePropertyListener(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!, CMIOObjectPropertyListenerProc!, UnsafeMutableRawPointer!) -> OSStatus](cmioobjectremovepropertylistener(_:_:_:_:).md)
- [func CMIOObjectRemovePropertyListenerBlock(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!, dispatch_queue_t!, CMIOObjectPropertyListenerBlock!) -> OSStatus](cmioobjectremovepropertylistenerblock(_:_:_:_:).md)
- [func CMIOObjectSetPropertyData(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!, UInt32, UnsafeRawPointer!, UInt32, UnsafeRawPointer!) -> OSStatus](cmioobjectsetpropertydata(_:_:_:_:_:_:).md)
- [func CMIOObjectShow(CMIOObjectID)](cmioobjectshow(_:).md)
- [func CMIOStreamClockConvertHostTimeToDeviceTime(UInt64, CFTypeRef!) -> CMTime](cmiostreamclockconverthosttimetodevicetime(_:_:).md)
- [func CMIOStreamClockCreate(CFAllocator!, CFString!, UnsafeRawPointer!, CMTime, UInt32, UInt32, UnsafeMutablePointer<Unmanaged<CFTypeRef>?>!) -> OSStatus](cmiostreamclockcreate(_:_:_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioobjectaddpropertylistenerblock(_:_:_:_:))*