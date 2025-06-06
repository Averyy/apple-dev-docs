# MIDIObjectRemoveProperty(_:_:)

**Framework**: Core MIDI  
**Kind**: func

Removes an object’s property.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func MIDIObjectRemoveProperty(_ obj: MIDIObjectRef, _ propertyID: CFString) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

## Parameters

- `obj`: The object to modify,
- `propertyID`: The property to remove.

## See Also

- [func MIDIObjectGetProperties(MIDIObjectRef, UnsafeMutablePointer<Unmanaged<CFPropertyList>?>, Bool) -> OSStatus](midiobjectgetproperties(_:_:_:).md)
  Returns all properties of an object.
- [func MIDIObjectGetStringProperty(MIDIObjectRef, CFString, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](midiobjectgetstringproperty(_:_:_:).md)
  Gets an object’s string-type property.
- [func MIDIObjectSetStringProperty(MIDIObjectRef, CFString, CFString) -> OSStatus](midiobjectsetstringproperty(_:_:_:).md)
  Sets an object’s string-type property.
- [func MIDIObjectGetIntegerProperty(MIDIObjectRef, CFString, UnsafeMutablePointer<Int32>) -> OSStatus](midiobjectgetintegerproperty(_:_:_:).md)
  Gets an object’s integer-type property.
- [func MIDIObjectSetIntegerProperty(MIDIObjectRef, CFString, Int32) -> OSStatus](midiobjectsetintegerproperty(_:_:_:).md)
  Sets an object’s integer-type property.
- [func MIDIObjectGetDataProperty(MIDIObjectRef, CFString, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus](midiobjectgetdataproperty(_:_:_:).md)
  Gets an object’s data-type property.
- [func MIDIObjectSetDataProperty(MIDIObjectRef, CFString, CFData) -> OSStatus](midiobjectsetdataproperty(_:_:_:).md)
  Sets an object’s data-type property.
- [func MIDIObjectGetDictionaryProperty(MIDIObjectRef, CFString, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](midiobjectgetdictionaryproperty(_:_:_:).md)
  Gets an object’s dictionary-type property.
- [func MIDIObjectSetDictionaryProperty(MIDIObjectRef, CFString, CFDictionary) -> OSStatus](midiobjectsetdictionaryproperty(_:_:_:).md)
  Sets an object’s dictionary-type property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjectremoveproperty(_:_:))*