# AudioUnitSetProperty(_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus AudioUnitSetProperty(AudioUnit inUnit, AudioUnitPropertyID inID, AudioUnitScope inScope, AudioUnitElement inElement, const void *inData, UInt32 inDataSize);
```

## Mentions

- [Migrating Your Audio Unit Host to the AUv3 API](./migrating-your-audio-unit-host-to-the-auv3-api.md)

#### Return Value

A result code.

#### Discussion

To clear an audio unit property value, set the `inData` parameter to  `NULL` and set the `inDataSize` parameter to `0`. Clearing properties works only for those properties that do not have a default value.

## Parameters

- `inUnit`: The audio unit that you want to set a property value for.
- `inID`: The audio unit property identifier.
- `inScope`: The audio unit scope for the property.
- `inElement`: The audio unit element for the property.
- `inData`: The value that you want to apply to the property. May be `NULL` (see Discussion).

  Always pass property values by reference. For example, for a property value of type `CFStringRef`, pass it as `&myCFString`.
- `inDataSize`: The size of the data you are providing in the `inData` parameter.

## See Also

### Configuring Audio Unit Properties
- [func AudioUnitGetProperty(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiounitgetproperty%28_,_,_,_,_,_%29.md)
  Gets the value of an audio unit property.
- [func AudioUnitGetPropertyInfo(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./audiounitgetpropertyinfo%28_,_,_,_,_,_%29.md)
  Gets information about an audio unit property.
- [func AudioUnitAddPropertyListener(AudioUnit, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](./audiounitaddpropertylistener%28_,_,_,_%29.md)
  Registers a callback to receive audio unit property change notifications.
- [func AudioUnitRemovePropertyListenerWithUserData(AudioUnit, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](./audiounitremovepropertylistenerwithuserdata%28_,_,_,_%29.md)
  Unregisters a previously-registered property listener callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitsetproperty(_:_:_:_:_:_:))*