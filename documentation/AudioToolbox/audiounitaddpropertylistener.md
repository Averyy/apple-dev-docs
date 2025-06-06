# AudioUnitAddPropertyListener(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Registers a callback to receive audio unit property change notifications.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioUnitAddPropertyListener(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inProc: AudioUnitPropertyListenerProc, _ inProcUserData: UnsafeMutableRawPointer?) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

When an audio unit property value changes, a notification callback can be called by the audio unit to inform interested parties that this event has occurred. The notification is defined by the tuple of the `inProc`, `inProcUserData`, `inID` parameters.

To unregister a callback, use the [`AudioUnitRemovePropertyListenerWithUserData(_:_:_:_:)`](audiounitremovepropertylistenerwithuserdata(_:_:_:_:).md) function.

## Parameters

- `inUnit`: The audio unit you want to receive property change notifications from.
- `inID`: The identifier for the property that you want to monitor.
- `inProc`: The callback that you are registering.
- `inProcUserData`: Custom data that you want to be sent to your callback. Use this, for example, to identify the property listener.

## See Also

- [func AudioUnitGetProperty(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](audiounitgetproperty(_:_:_:_:_:_:).md)
  Gets the value of an audio unit property.
- [func AudioUnitSetProperty(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeRawPointer?, UInt32) -> OSStatus](audiounitsetproperty(_:_:_:_:_:_:).md)
  Sets the value of an audio unit property.
- [func AudioUnitGetPropertyInfo(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audiounitgetpropertyinfo(_:_:_:_:_:_:).md)
  Gets information about an audio unit property.
- [func AudioUnitRemovePropertyListenerWithUserData(AudioUnit, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audiounitremovepropertylistenerwithuserdata(_:_:_:_:).md)
  Unregisters a previously-registered property listener callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitaddpropertylistener(_:_:_:_:))*