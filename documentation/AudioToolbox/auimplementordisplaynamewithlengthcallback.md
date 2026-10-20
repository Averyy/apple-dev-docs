# AUImplementorDisplayNameWithLengthCallback

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

A block called to obtain a parameter node’s display name, possibly truncated to a desired length.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AUImplementorDisplayNameWithLengthCallback = (AUParameterNode, Int) -> String
```

```c
typedef NSString *(^)(AUParameterNode *, long) AUImplementorDisplayNameWithLengthCallback;
```

#### Discussion

This block is only of interest to audio unit subclasses.

The block returns a truncated parameter node display name.

The block takes the following parameters:

- **node**: The parameter node to query.
- **desiredLength**: The desired length, in characters, of the display name.

## See Also

### Related Documentation
- [var implementorDisplayNameWithLengthCallback: AUImplementorDisplayNameWithLengthCallback](./auparameternode/implementordisplaynamewithlengthcallback.md)
  The callback for obtaining an abbreviated version of a parameter node display name.
### Monitoring Parameter Changes
- [func AUListenerCreateWithDispatchQueue(UnsafeMutablePointer<AUParameterListenerRef?>, Float32, dispatch_queue_t, AUParameterListenerBlock) -> OSStatus](./aulistenercreatewithdispatchqueue%28_,_,_,_%29.md)
- [func AUListenerCreate(AUParameterListenerProc, UnsafeMutableRawPointer, CFRunLoop?, CFString?, Float32, UnsafeMutablePointer<AUParameterListenerRef?>) -> OSStatus](./aulistenercreate%28_,_,_,_,_,_%29.md)
- [func AUParameterListenerNotify(AUParameterListenerRef?, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>) -> OSStatus](./auparameterlistenernotify%28_,_,_%29.md)
- [func AUParameterFormatValue(Float64, UnsafePointer<AudioUnitParameter>, UnsafeMutablePointer<CChar>, UInt32) -> UnsafeMutablePointer<CChar>](./auparameterformatvalue%28_,_,_,_%29.md)
- [func AUParameterSet(AUParameterListenerRef?, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>, AudioUnitParameterValue, UInt32) -> OSStatus](./auparameterset%28_,_,_,_,_%29.md)
- [func AUParameterValueFromLinear(Float32, UnsafePointer<AudioUnitParameter>) -> AudioUnitParameterValue](./auparametervaluefromlinear%28_,_%29.md)
- [func AUParameterValueToLinear(AudioUnitParameterValue, UnsafePointer<AudioUnitParameter>) -> Float32](./auparametervaluetolinear%28_,_%29.md)
- [typealias AUParameterListenerBlock](./auparameterlistenerblock.md)
- [typealias AUParameterListenerProc](./auparameterlistenerproc.md)
- [typealias AUParameterListenerRef](./auparameterlistenerref.md)
- [typealias AUImplementorStringFromValueCallback](./auimplementorstringfromvaluecallback.md)
  A block called to convert a parameter value to a string representation.
- [typealias AUImplementorValueFromStringCallback](./auimplementorvaluefromstringcallback.md)
  A block called to convert a string to a parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auimplementordisplaynamewithlengthcallback)*