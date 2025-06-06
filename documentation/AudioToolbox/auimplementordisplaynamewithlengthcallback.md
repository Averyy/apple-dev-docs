# AUImplementorDisplayNameWithLengthCallback

**Framework**: Audio Toolbox  
**Kind**: typealias

A block called to obtain a parameter node’s display name, possibly truncated to a desired length.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AUImplementorDisplayNameWithLengthCallback = (AUParameterNode, Int) -> String
```

#### Discussion

This block is only of interest to audio unit subclasses.

The block returns a truncated parameter node display name.

The block takes the following parameters:

## See Also

- [var implementorDisplayNameWithLengthCallback: AUImplementorDisplayNameWithLengthCallback](auparameternode/implementordisplaynamewithlengthcallback.md)
  The callback for obtaining an abbreviated version of a parameter node display name.
- [func AUListenerCreateWithDispatchQueue(UnsafeMutablePointer<AUParameterListenerRef?>, Float32, dispatch_queue_t, AUParameterListenerBlock) -> OSStatus](aulistenercreatewithdispatchqueue(_:_:_:_:).md)
- [func AUListenerCreate(AUParameterListenerProc, UnsafeMutableRawPointer, CFRunLoop?, CFString?, Float32, UnsafeMutablePointer<AUParameterListenerRef?>) -> OSStatus](aulistenercreate(_:_:_:_:_:_:).md)
- [func AUParameterListenerNotify(AUParameterListenerRef?, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>) -> OSStatus](auparameterlistenernotify(_:_:_:).md)
- [func AUParameterFormatValue(Float64, UnsafePointer<AudioUnitParameter>, UnsafeMutablePointer<CChar>, UInt32) -> UnsafeMutablePointer<CChar>](auparameterformatvalue(_:_:_:_:).md)
- [func AUParameterSet(AUParameterListenerRef?, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>, AudioUnitParameterValue, UInt32) -> OSStatus](auparameterset(_:_:_:_:_:).md)
- [func AUParameterValueFromLinear(Float32, UnsafePointer<AudioUnitParameter>) -> AudioUnitParameterValue](auparametervaluefromlinear(_:_:).md)
- [func AUParameterValueToLinear(AudioUnitParameterValue, UnsafePointer<AudioUnitParameter>) -> Float32](auparametervaluetolinear(_:_:).md)
- [typealias AUParameterListenerBlock](auparameterlistenerblock.md)
- [typealias AUParameterListenerProc](auparameterlistenerproc.md)
- [typealias AUParameterListenerRef](auparameterlistenerref.md)
- [typealias AUImplementorStringFromValueCallback](auimplementorstringfromvaluecallback.md)
  A block called to convert a parameter value to a string representation.
- [typealias AUImplementorValueFromStringCallback](auimplementorvaluefromstringcallback.md)
  A block called to convert a string to a parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auimplementordisplaynamewithlengthcallback)*