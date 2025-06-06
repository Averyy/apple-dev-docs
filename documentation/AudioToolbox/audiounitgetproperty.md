# AudioUnitGetProperty(_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets the value of an audio unit property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioUnitGetProperty(_ inUnit: AudioUnit, _ inID: AudioUnitPropertyID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ outData: UnsafeMutableRawPointer, _ ioDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus
```

## Mentions

- [Migrating Your Audio Unit Host to the AUv3 API](migrating-your-audio-unit-host-to-the-auv3-api.md)

#### Return Value

A result code.

#### Discussion

Some Core Audio property values are C types and others are Core Foundation objects.

If you call this function to retrieve a value that is a Core Foundation object, then this function—despite the use of “Get” in its name—duplicates the object. You are responsible for releasing the object, as described in [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029) in [`Memory Management Programming Guide for Core Foundation`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i).

## Parameters

- `inUnit`: The audio unit that you want to get a property value from.
- `inID`: The identifier for the property.
- `inScope`: The audio unit scope for the property.
- `inElement`: The audio unit element for the property.
- `outData`: On successful output, the current value for the specified audio unit property. Set this parameter to   when calling this function if you only want to determine how much memory to allocate for a variable size property.
- `ioDataSize`: On input, the expected size of the property value, as pointed to by the   parameter. On output, the size of the data that was returned.

## See Also

- [func AudioUnitSetProperty(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeRawPointer?, UInt32) -> OSStatus](audiounitsetproperty(_:_:_:_:_:_:).md)
  Sets the value of an audio unit property.
- [func AudioUnitGetPropertyInfo(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audiounitgetpropertyinfo(_:_:_:_:_:_:).md)
  Gets information about an audio unit property.
- [func AudioUnitAddPropertyListener(AudioUnit, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audiounitaddpropertylistener(_:_:_:_:).md)
  Registers a callback to receive audio unit property change notifications.
- [func AudioUnitRemovePropertyListenerWithUserData(AudioUnit, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audiounitremovepropertylistenerwithuserdata(_:_:_:_:).md)
  Unregisters a previously-registered property listener callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitgetproperty(_:_:_:_:_:_:))*