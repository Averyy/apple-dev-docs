# AudioUnitRemovePropertyListenerWithUserData(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Unregisters a previously-registered property listener callback function.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioUnitRemovePropertyListenerWithUserData(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inProc: AudioUnitPropertyListenerProc, _ inProcUserData: UnsafeMutableRawPointer?) -> OSStatus
```

#### Return Value

A result code.

## Parameters

- `inUnit`: The audio unit that you no longer want to receive property change notifications from.
- `inID`: The identifier for the property that you no longer want to monitor.
- `inProc`: The callback function that you previously registered and are now unregistering.
- `inProcUserData`: The custom data that you provided when registering the callback function.

## See Also

- [func AudioUnitGetProperty(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](audiounitgetproperty(_:_:_:_:_:_:).md)
  Gets the value of an audio unit property.
- [func AudioUnitSetProperty(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeRawPointer?, UInt32) -> OSStatus](audiounitsetproperty(_:_:_:_:_:_:).md)
  Sets the value of an audio unit property.
- [func AudioUnitGetPropertyInfo(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audiounitgetpropertyinfo(_:_:_:_:_:_:).md)
  Gets information about an audio unit property.
- [func AudioUnitAddPropertyListener(AudioUnit, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audiounitaddpropertylistener(_:_:_:_:).md)
  Registers a callback to receive audio unit property change notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitremovepropertylistenerwithuserdata(_:_:_:_:))*