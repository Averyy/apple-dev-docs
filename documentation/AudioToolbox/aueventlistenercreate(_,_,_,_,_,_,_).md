# AUEventListenerCreate(_:_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus AUEventListenerCreate(AUEventListenerProc inProc, void *inUserData, CFRunLoopRef inRunLoop, CFStringRef inRunLoopMode, Float32 inNotificationInterval, Float32 inValueChangeGranularity, AUEventListenerRef*outListener);
```

## See Also

### Responding to Events
- [func AUEventListenerCreateWithDispatchQueue(UnsafeMutablePointer<AUEventListenerRef?>, Float32, Float32, dispatch_queue_t, AUEventListenerBlock) -> OSStatus](./aueventlistenercreatewithdispatchqueue%28_,_,_,_,_%29.md)
- [func AUListenerDispose(AUParameterListenerRef) -> OSStatus](./aulistenerdispose%28_%29.md)
- [func AUEventListenerNotify(AUEventListenerRef?, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](./aueventlistenernotify%28_,_,_%29.md)
- [func AUEventListenerAddEventType(AUEventListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](./aueventlisteneraddeventtype%28_,_,_%29.md)
- [func AUEventListenerRemoveEventType(AUEventListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](./aueventlistenerremoveeventtype%28_,_,_%29.md)
- [func AUListenerAddParameter(AUParameterListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>) -> OSStatus](./aulisteneraddparameter%28_,_,_%29.md)
- [func AUListenerRemoveParameter(AUParameterListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>) -> OSStatus](./aulistenerremoveparameter%28_,_,_%29.md)
- [typealias AUEventListenerBlock](./aueventlistenerblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aueventlistenercreate(_:_:_:_:_:_:_:))*