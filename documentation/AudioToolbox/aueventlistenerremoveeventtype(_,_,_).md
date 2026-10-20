# AUEventListenerRemoveEventType(_:_:_:)

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
func AUEventListenerRemoveEventType(_ inListener: AUEventListenerRef, _ inObject: UnsafeMutableRawPointer?, _ inEvent: UnsafePointer<AudioUnitEvent>) -> OSStatus
```

## See Also

- [func AUEventListenerCreateWithDispatchQueue(UnsafeMutablePointer<AUEventListenerRef?>, Float32, Float32, dispatch_queue_t, AUEventListenerBlock) -> OSStatus](aueventlistenercreatewithdispatchqueue(_:_:_:_:_:).md)
- [func AUEventListenerCreate(AUEventListenerProc, UnsafeMutableRawPointer?, CFRunLoop?, CFString?, Float32, Float32, UnsafeMutablePointer<AUEventListenerRef?>) -> OSStatus](aueventlistenercreate(_:_:_:_:_:_:_:).md)
- [func AUListenerDispose(AUParameterListenerRef) -> OSStatus](aulistenerdispose(_:).md)
- [func AUEventListenerNotify(AUEventListenerRef?, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](aueventlistenernotify(_:_:_:).md)
- [func AUEventListenerAddEventType(AUEventListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](aueventlisteneraddeventtype(_:_:_:).md)
- [func AUListenerAddParameter(AUParameterListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>) -> OSStatus](aulisteneraddparameter(_:_:_:).md)
- [func AUListenerRemoveParameter(AUParameterListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>) -> OSStatus](aulistenerremoveparameter(_:_:_:).md)
- [typealias AUEventListenerBlock](aueventlistenerblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aueventlistenerremoveeventtype(_:_:_:))*