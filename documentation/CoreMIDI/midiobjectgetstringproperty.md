# MIDIObjectGetStringProperty(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Gets an object’s string-type property.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIObjectGetStringProperty(_ obj: MIDIObjectRef, _ propertyID: CFString, _ str: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

See [`MIDIObjectRef`](midiobjectref.md) for information about properties.

## Parameters

- `obj`: The object to query.
- `propertyID`: The name of the property to return.
- `str`: On successful return, the property value.

## See Also

- [func MIDIObjectGetProperties(MIDIObjectRef, UnsafeMutablePointer<Unmanaged<CFPropertyList>?>, Bool) -> OSStatus](midiobjectgetproperties(_:_:_:).md)
  Returns all properties of an object.
- [func MIDIObjectRemoveProperty(MIDIObjectRef, CFString) -> OSStatus](midiobjectremoveproperty(_:_:).md)
  Removes an object’s property.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjectgetstringproperty(_:_:_:))*