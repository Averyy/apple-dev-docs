# AUEventListenerCreate(_:_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AUEventListenerCreate(_ inProc: AUEventListenerProc, _ inUserData: UnsafeMutableRawPointer?, _ inRunLoop: CFRunLoop?, _ inRunLoopMode: CFString?, _ inNotificationInterval: Float32, _ inValueChangeGranularity: Float32, _ outListener: UnsafeMutablePointer<AUEventListenerRef?>) -> OSStatus
```

## See Also

- [func AUEventListenerCreateWithDispatchQueue(UnsafeMutablePointer<AUEventListenerRef?>, Float32, Float32, dispatch_queue_t, AUEventListenerBlock) -> OSStatus](aueventlistenercreatewithdispatchqueue(_:_:_:_:_:).md)
- [func AUListenerDispose(AUParameterListenerRef) -> OSStatus](aulistenerdispose(_:).md)
- [func AUEventListenerNotify(AUEventListenerRef?, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](aueventlistenernotify(_:_:_:).md)
- [func AUEventListenerAddEventType(AUEventListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](aueventlisteneraddeventtype(_:_:_:).md)
- [func AUEventListenerRemoveEventType(AUEventListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](aueventlistenerremoveeventtype(_:_:_:).md)
- [func AUListenerAddParameter(AUParameterListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>) -> OSStatus](aulisteneraddparameter(_:_:_:).md)
- [func AUListenerRemoveParameter(AUParameterListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>) -> OSStatus](aulistenerremoveparameter(_:_:_:).md)
- [typealias AUEventListenerBlock](aueventlistenerblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aueventlistenercreate(_:_:_:_:_:_:_:))*