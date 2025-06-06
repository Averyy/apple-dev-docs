# AudioUnitSetProperty(_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Sets the value of an audio unit property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioUnitSetProperty(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ inData: UnsafeRawPointer?, _ inDataSize: UInt32) -> OSStatus
```

## Mentions

- [Migrating Your Audio Unit Host to the AUv3 API](migrating-your-audio-unit-host-to-the-auv3-api.md)

#### Return Value

A result code.

#### Discussion

To clear an audio unit property value, set the `inData` parameter to  `NULL` and set the `inDataSize` parameter to `0`. Clearing properties works only for those properties that do not have a default value.

## Parameters

- `inUnit`: The audio unit that you want to set a property value for.
- `inID`: The audio unit property identifier.
- `inScope`: The audio unit scope for the property.
- `inElement`: The audio unit element for the property.
- `inData`: Always pass property values by reference. For example, for a property value of type  , pass it as  .
- `inDataSize`: The size of the data you are providing in the   parameter.

## See Also

- [func AudioUnitGetProperty(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](audiounitgetproperty(_:_:_:_:_:_:).md)
  Gets the value of an audio unit property.
- [func AudioUnitGetPropertyInfo(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audiounitgetpropertyinfo(_:_:_:_:_:_:).md)
  Gets information about an audio unit property.
- [func AudioUnitAddPropertyListener(AudioUnit, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audiounitaddpropertylistener(_:_:_:_:).md)
  Registers a callback to receive audio unit property change notifications.
- [func AudioUnitRemovePropertyListenerWithUserData(AudioUnit, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audiounitremovepropertylistenerwithuserdata(_:_:_:_:).md)
  Unregisters a previously-registered property listener callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitsetproperty(_:_:_:_:_:_:))*