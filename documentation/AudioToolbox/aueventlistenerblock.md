# AUEventListenerBlock

**Framework**: Audio Toolbox  
**Kind**: typealias

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AUEventListenerBlock = (UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>, UInt64, AudioUnitParameterValue) -> Void
```

## See Also

- [func AUEventListenerCreateWithDispatchQueue(UnsafeMutablePointer<AUEventListenerRef?>, Float32, Float32, dispatch_queue_t, AUEventListenerBlock) -> OSStatus](aueventlistenercreatewithdispatchqueue(_:_:_:_:_:).md)
- [func AUEventListenerCreate(AUEventListenerProc, UnsafeMutableRawPointer?, CFRunLoop?, CFString?, Float32, Float32, UnsafeMutablePointer<AUEventListenerRef?>) -> OSStatus](aueventlistenercreate(_:_:_:_:_:_:_:).md)
- [func AUListenerDispose(AUParameterListenerRef) -> OSStatus](aulistenerdispose(_:).md)
- [func AUEventListenerNotify(AUEventListenerRef?, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](aueventlistenernotify(_:_:_:).md)
- [func AUEventListenerAddEventType(AUEventListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](aueventlisteneraddeventtype(_:_:_:).md)
- [func AUEventListenerRemoveEventType(AUEventListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](aueventlistenerremoveeventtype(_:_:_:).md)
- [func AUListenerAddParameter(AUParameterListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>) -> OSStatus](aulisteneraddparameter(_:_:_:).md)
- [func AUListenerRemoveParameter(AUParameterListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>) -> OSStatus](aulistenerremoveparameter(_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aueventlistenerblock)*