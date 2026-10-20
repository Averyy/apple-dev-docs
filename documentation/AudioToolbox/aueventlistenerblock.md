# AUEventListenerBlock

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AUEventListenerBlock = (UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>, UInt64, AudioUnitParameterValue) -> Void
```

```c
typedef void (^)(void *, const struct AudioUnitEvent *, unsigned long long, float) AUEventListenerBlock;
```

## See Also

### Responding to Events
- [func AUEventListenerCreateWithDispatchQueue(UnsafeMutablePointer<AUEventListenerRef?>, Float32, Float32, dispatch_queue_t, AUEventListenerBlock) -> OSStatus](./aueventlistenercreatewithdispatchqueue%28_,_,_,_,_%29.md)
- [func AUEventListenerCreate(AUEventListenerProc, UnsafeMutableRawPointer?, CFRunLoop?, CFString?, Float32, Float32, UnsafeMutablePointer<AUEventListenerRef?>) -> OSStatus](./aueventlistenercreate%28_,_,_,_,_,_,_%29.md)
- [func AUListenerDispose(AUParameterListenerRef) -> OSStatus](./aulistenerdispose%28_%29.md)
- [func AUEventListenerNotify(AUEventListenerRef?, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](./aueventlistenernotify%28_,_,_%29.md)
- [func AUEventListenerAddEventType(AUEventListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](./aueventlisteneraddeventtype%28_,_,_%29.md)
- [func AUEventListenerRemoveEventType(AUEventListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](./aueventlistenerremoveeventtype%28_,_,_%29.md)
- [func AUListenerAddParameter(AUParameterListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>) -> OSStatus](./aulisteneraddparameter%28_,_,_%29.md)
- [func AUListenerRemoveParameter(AUParameterListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>) -> OSStatus](./aulistenerremoveparameter%28_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aueventlistenerblock)*