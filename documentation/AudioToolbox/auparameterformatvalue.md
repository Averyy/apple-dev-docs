# AUParameterFormatValue(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AUParameterFormatValue(_ inParameterValue: Float64, _ inParameter: UnsafePointer<AudioUnitParameter>, _ inTextBuffer: UnsafeMutablePointer<CChar>, _ inDigits: UInt32) -> UnsafeMutablePointer<CChar>
```

## See Also

- [func AUListenerCreateWithDispatchQueue(UnsafeMutablePointer<AUParameterListenerRef?>, Float32, dispatch_queue_t, AUParameterListenerBlock) -> OSStatus](aulistenercreatewithdispatchqueue(_:_:_:_:).md)
- [func AUListenerCreate(AUParameterListenerProc, UnsafeMutableRawPointer, CFRunLoop?, CFString?, Float32, UnsafeMutablePointer<AUParameterListenerRef?>) -> OSStatus](aulistenercreate(_:_:_:_:_:_:).md)
- [func AUParameterListenerNotify(AUParameterListenerRef?, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>) -> OSStatus](auparameterlistenernotify(_:_:_:).md)
- [func AUParameterSet(AUParameterListenerRef?, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>, AudioUnitParameterValue, UInt32) -> OSStatus](auparameterset(_:_:_:_:_:).md)
- [func AUParameterValueFromLinear(Float32, UnsafePointer<AudioUnitParameter>) -> AudioUnitParameterValue](auparametervaluefromlinear(_:_:).md)
- [func AUParameterValueToLinear(AudioUnitParameterValue, UnsafePointer<AudioUnitParameter>) -> Float32](auparametervaluetolinear(_:_:).md)
- [typealias AUParameterListenerBlock](auparameterlistenerblock.md)
- [typealias AUParameterListenerProc](auparameterlistenerproc.md)
- [typealias AUParameterListenerRef](auparameterlistenerref.md)
- [typealias AUImplementorDisplayNameWithLengthCallback](auimplementordisplaynamewithlengthcallback.md)
  A block called to obtain a parameter node’s display name, possibly truncated to a desired length.
- [typealias AUImplementorStringFromValueCallback](auimplementorstringfromvaluecallback.md)
  A block called to convert a parameter value to a string representation.
- [typealias AUImplementorValueFromStringCallback](auimplementorvaluefromstringcallback.md)
  A block called to convert a string to a parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameterformatvalue(_:_:_:_:))*