# AudioUnitGetPropertyInfo(_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets information about an audio unit property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioUnitGetPropertyInfo(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ outDataSize: UnsafeMutablePointer<UInt32>?, _ outWritable: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

Some properties that have read/write access when an audio unit is uninitialized become read-only when the audio unit is initialized.

## Parameters

- `inUnit`: The audio unit that you want to get property information from.
- `inID`: The identifier for the property.
- `inScope`: The audio unit scope for the property.
- `inElement`: The audio unit element for the property.
- `outDataSize`: On successful output, the maximum size for the audio unit property. Can be   on input, in which case no value is returned.
- `outWritable`: On successful output, a Boolean value indicating whether the property can be written to ( ) or not ( ). Can be   on input, in which case no value is returned.

## See Also

- [func AudioUnitGetProperty(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](audiounitgetproperty(_:_:_:_:_:_:).md)
  Gets the value of an audio unit property.
- [func AudioUnitSetProperty(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeRawPointer?, UInt32) -> OSStatus](audiounitsetproperty(_:_:_:_:_:_:).md)
  Sets the value of an audio unit property.
- [func AudioUnitAddPropertyListener(AudioUnit, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audiounitaddpropertylistener(_:_:_:_:).md)
  Registers a callback to receive audio unit property change notifications.
- [func AudioUnitRemovePropertyListenerWithUserData(AudioUnit, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audiounitremovepropertylistenerwithuserdata(_:_:_:_:).md)
  Unregisters a previously-registered property listener callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitgetpropertyinfo(_:_:_:_:_:_:))*