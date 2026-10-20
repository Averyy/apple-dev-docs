# AUListenerAddParameter(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AUListenerAddParameter(_ inListener: AUParameterListenerRef, _ inObject: UnsafeMutableRawPointer?, _ inParameter: UnsafePointer<AudioUnitParameter>) -> OSStatus
```

```c
extern OSStatus AUListenerAddParameter(AUParameterListenerRef inListener, void *inObject, const AudioUnitParameter *inParameter);
```

## See Also

### Responding to Events
- [func AUEventListenerCreateWithDispatchQueue(UnsafeMutablePointer<AUEventListenerRef?>, Float32, Float32, dispatch_queue_t, AUEventListenerBlock) -> OSStatus](./aueventlistenercreatewithdispatchqueue%28_,_,_,_,_%29.md)
- [func AUEventListenerCreate(AUEventListenerProc, UnsafeMutableRawPointer?, CFRunLoop?, CFString?, Float32, Float32, UnsafeMutablePointer<AUEventListenerRef?>) -> OSStatus](./aueventlistenercreate%28_,_,_,_,_,_,_%29.md)
- [func AUListenerDispose(AUParameterListenerRef) -> OSStatus](./aulistenerdispose%28_%29.md)
- [func AUEventListenerNotify(AUEventListenerRef?, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](./aueventlistenernotify%28_,_,_%29.md)
- [func AUEventListenerAddEventType(AUEventListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](./aueventlisteneraddeventtype%28_,_,_%29.md)
- [func AUEventListenerRemoveEventType(AUEventListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](./aueventlistenerremoveeventtype%28_,_,_%29.md)
- [func AUListenerRemoveParameter(AUParameterListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>) -> OSStatus](./aulistenerremoveparameter%28_,_,_%29.md)
- [typealias AUEventListenerBlock](./aueventlistenerblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aulisteneraddparameter(_:_:_:))*