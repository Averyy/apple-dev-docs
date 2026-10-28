# AUImplementorStringFromValueCallback

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

A block called to convert a parameter value to a string representation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AUImplementorStringFromValueCallback = (AUParameter, UnsafePointer<AUValue>?) -> String
```

```c
typedef NSString *(^)(AUParameter *, const float *) AUImplementorStringFromValueCallback;
```

## Discussion

This block is only of interest to audio unit subclasses.

The block returns a string representing a parameter value.

The block takes the following parameters:

- **param**: The parameter that contains the value.
- **value**: The parameter value to be converted.

## See Also

### Related Documentation
- [var implementorStringFromValueCallback: AUImplementorStringFromValueCallback](./auparameternode/implementorstringfromvaluecallback.md)
  The callback for providing a string representation of a parameter value.
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
- [typealias AUImplementorDisplayNameWithLengthCallback](./auimplementordisplaynamewithlengthcallback.md)
  A block called to obtain a parameter node’s display name, possibly truncated to a desired length.
- [typealias AUImplementorValueFromStringCallback](./auimplementorvaluefromstringcallback.md)
  A block called to convert a string to a parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auimplementorstringfromvaluecallback)*