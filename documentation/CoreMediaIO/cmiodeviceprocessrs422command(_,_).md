# CMIODeviceProcessRS422Command(_:_:)

**Framework**: Core Media I/O  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```swift
func CMIODeviceProcessRS422Command(_ deviceID: CMIODeviceID, _ ioRS422Command: UnsafeMutablePointer<CMIODeviceRS422Command>!) -> OSStatus
```

```c
extern OSStatus CMIODeviceProcessRS422Command(CMIODeviceID deviceID, CMIODeviceRS422Command *ioRS422Command);
```

## See Also

### Functions
- [func CMIODeviceProcessAVCCommand(CMIODeviceID, UnsafeMutablePointer<CMIODeviceAVCCommand>!) -> OSStatus](./cmiodeviceprocessavccommand%28_,_%29.md)
- [func CMIODeviceStartStream(CMIODeviceID, CMIOStreamID) -> OSStatus](./cmiodevicestartstream%28_,_%29.md)
- [func CMIODeviceStopStream(CMIODeviceID, CMIOStreamID) -> OSStatus](./cmiodevicestopstream%28_,_%29.md)
- [func CMIOObjectAddPropertyListener(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!, CMIOObjectPropertyListenerProc!, UnsafeMutableRawPointer!) -> OSStatus](./cmioobjectaddpropertylistener%28_,_,_,_%29.md)
- [func CMIOObjectAddPropertyListenerBlock(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!, dispatch_queue_t!, CMIOObjectPropertyListenerBlock!) -> OSStatus](./cmioobjectaddpropertylistenerblock%28_,_,_,_%29.md)
- [func CMIOObjectGetPropertyData(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!, UInt32, UnsafeRawPointer!, UInt32, UnsafeMutablePointer<UInt32>!, UnsafeMutableRawPointer!) -> OSStatus](./cmioobjectgetpropertydata%28_,_,_,_,_,_,_%29.md)
- [func CMIOObjectGetPropertyDataSize(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!, UInt32, UnsafeRawPointer!, UnsafeMutablePointer<UInt32>!) -> OSStatus](./cmioobjectgetpropertydatasize%28_,_,_,_,_%29.md)
- [func CMIOObjectHasProperty(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!) -> Bool](./cmioobjecthasproperty%28_,_%29.md)
- [func CMIOObjectIsPropertySettable(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!, UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus](./cmioobjectispropertysettable%28_,_,_%29.md)
- [func CMIOObjectRemovePropertyListener(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!, CMIOObjectPropertyListenerProc!, UnsafeMutableRawPointer!) -> OSStatus](./cmioobjectremovepropertylistener%28_,_,_,_%29.md)
- [func CMIOObjectRemovePropertyListenerBlock(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!, dispatch_queue_t!, CMIOObjectPropertyListenerBlock!) -> OSStatus](./cmioobjectremovepropertylistenerblock%28_,_,_,_%29.md)
- [func CMIOObjectSetPropertyData(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!, UInt32, UnsafeRawPointer!, UInt32, UnsafeRawPointer!) -> OSStatus](./cmioobjectsetpropertydata%28_,_,_,_,_,_%29.md)
- [func CMIOObjectShow(CMIOObjectID)](./cmioobjectshow%28_%29.md)
- [func CMIOStreamClockConvertHostTimeToDeviceTime(UInt64, CFTypeRef!) -> CMTime](./cmiostreamclockconverthosttimetodevicetime%28_,_%29.md)
- [func CMIOStreamClockCreate(CFAllocator!, CFString!, UnsafeRawPointer!, CMTime, UInt32, UInt32, UnsafeMutablePointer<Unmanaged<CFTypeRef>?>!) -> OSStatus](./cmiostreamclockcreate%28_,_,_,_,_,_,_%29.md)
- [CMIOSampleBufferCopyNonRequiredAttachments](./cmiosamplebuffercopynonrequiredattachments.md)
- [CMIOSampleBufferCopySampleAttachments](./cmiosamplebuffercopysampleattachments.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmiodeviceprocessrs422command(_:_:))*