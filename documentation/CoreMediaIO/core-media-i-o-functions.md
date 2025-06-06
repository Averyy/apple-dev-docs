# DAL plug-in functions

**Framework**: Core Media I/O

## Topics

### Functions
- [func CMIODeviceProcessAVCCommand(CMIODeviceID, UnsafeMutablePointer<CMIODeviceAVCCommand>!) -> OSStatus](cmiodeviceprocessavccommand(_:_:).md)
- [func CMIODeviceProcessRS422Command(CMIODeviceID, UnsafeMutablePointer<CMIODeviceRS422Command>!) -> OSStatus](cmiodeviceprocessrs422command(_:_:).md)
- [func CMIODeviceStartStream(CMIODeviceID, CMIOStreamID) -> OSStatus](cmiodevicestartstream(_:_:).md)
- [func CMIODeviceStopStream(CMIODeviceID, CMIOStreamID) -> OSStatus](cmiodevicestopstream(_:_:).md)
- [func CMIOObjectAddPropertyListener(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!, CMIOObjectPropertyListenerProc!, UnsafeMutableRawPointer!) -> OSStatus](cmioobjectaddpropertylistener(_:_:_:_:).md)
- [func CMIOObjectAddPropertyListenerBlock(CMIOObjectID, UnsafePointer<CMIOObjectPropertyAddress>!, dispatch_queue_t!, CMIOObjectPropertyListenerBlock!) -> OSStatus](cmioobjectaddpropertylistenerblock(_:_:_:_:).md)
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
- [func CMIOStreamClockInvalidate(CFTypeRef!) -> OSStatus](cmiostreamclockinvalidate(_:).md)
- [func CMIOStreamClockPostTimingEvent(CMTime, UInt64, Bool, CFTypeRef!) -> OSStatus](cmiostreamclockposttimingevent(_:_:_:_:).md)
- [func CMIOStreamCopyBufferQueue(CMIOStreamID, CMIODeviceStreamQueueAlteredProc!, UnsafeMutableRawPointer!, UnsafeMutablePointer<Unmanaged<CMSimpleQueue>?>!) -> OSStatus](cmiostreamcopybufferqueue(_:_:_:_:).md)
- [func CMIOStreamDeckCueTo(CMIOStreamID, UInt64, Bool) -> OSStatus](cmiostreamdeckcueto(_:_:_:).md)
- [func CMIOStreamDeckJog(CMIOStreamID, Int32) -> OSStatus](cmiostreamdeckjog(_:_:).md)
- [func CMIOStreamDeckPlay(CMIOStreamID) -> OSStatus](cmiostreamdeckplay(_:).md)
- [func CMIOStreamDeckStop(CMIOStreamID) -> OSStatus](cmiostreamdeckstop(_:).md)

## See Also

- [DAL plug-in structures](core-media-i-o-structures.md)
- [DAL plug-in enumerations](core-media-i-o-enumerations.md)
- [DAL plug-in data types](core-media-i-o-data-types.md)
- [DAL plug-in errors](core-media-i-o-errors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/core-media-i-o-functions)*