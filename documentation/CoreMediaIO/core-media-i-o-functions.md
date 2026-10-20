# DAL plug-in functions

**Framework**: Core Media I/O  
**Role**: API Collection

## Topics

### Functions
- [func CMIODeviceProcessAVCCommand(CMIODeviceID, UnsafeMutablePointer<CMIODeviceAVCCommand>!) -> OSStatus](./cmiodeviceprocessavccommand%28_,_%29.md)
- [func CMIODeviceProcessRS422Command(CMIODeviceID, UnsafeMutablePointer<CMIODeviceRS422Command>!) -> OSStatus](./cmiodeviceprocessrs422command%28_,_%29.md)
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
- [func CMIOStreamClockInvalidate(CFTypeRef!) -> OSStatus](./cmiostreamclockinvalidate%28_%29.md)
- [func CMIOStreamClockPostTimingEvent(CMTime, UInt64, Bool, CFTypeRef!) -> OSStatus](./cmiostreamclockposttimingevent%28_,_,_,_%29.md)
- [func CMIOStreamCopyBufferQueue(CMIOStreamID, CMIODeviceStreamQueueAlteredProc!, UnsafeMutableRawPointer!, UnsafeMutablePointer<Unmanaged<CMSimpleQueue>?>!) -> OSStatus](./cmiostreamcopybufferqueue%28_,_,_,_%29.md)
- [func CMIOStreamDeckCueTo(CMIOStreamID, UInt64, Bool) -> OSStatus](./cmiostreamdeckcueto%28_,_,_%29.md)
- [func CMIOStreamDeckJog(CMIOStreamID, Int32) -> OSStatus](./cmiostreamdeckjog%28_,_%29.md)
- [func CMIOStreamDeckPlay(CMIOStreamID) -> OSStatus](./cmiostreamdeckplay%28_%29.md)
- [func CMIOStreamDeckStop(CMIOStreamID) -> OSStatus](./cmiostreamdeckstop%28_%29.md)

## See Also

### Reference
- [DAL plug-in structures](./core-media-i-o-structures.md)
- [DAL plug-in enumerations](./core-media-i-o-enumerations.md)
- [DAL plug-in data types](./core-media-i-o-data-types.md)
- [DAL plug-in errors](./core-media-i-o-errors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/core-media-i-o-functions)*