# MIDIObjectGetDictionaryProperty(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Gets an object’s dictionary-type property.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func MIDIObjectGetDictionaryProperty(_ obj: MIDIObjectRef, _ propertyID: CFString, _ outDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus
```

```c
extern OSStatus MIDIObjectGetDictionaryProperty(MIDIObjectRef obj, CFStringRef propertyID, CFDictionaryRef*outDict);
```

#### Return Value

An `OSStatus` result code.

#### Discussion

See [`MIDIObjectRef`](./midiobjectref.md) for information about properties.

## Parameters

- `obj`: The object to query.
- `propertyID`: The name of the property to return.
- `outDict`: On successful return, the property value.

## See Also

### Property Accessors
- [func MIDIObjectGetProperties(MIDIObjectRef, UnsafeMutablePointer<Unmanaged<CFPropertyList>?>, Bool) -> OSStatus](./midiobjectgetproperties%28_,_,_%29.md)
  Returns all properties of an object.
- [func MIDIObjectRemoveProperty(MIDIObjectRef, CFString) -> OSStatus](./midiobjectremoveproperty%28_,_%29.md)
  Removes an object’s property.
- [func MIDIObjectGetStringProperty(MIDIObjectRef, CFString, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./midiobjectgetstringproperty%28_,_,_%29.md)
  Gets an object’s string-type property.
- [func MIDIObjectSetStringProperty(MIDIObjectRef, CFString, CFString) -> OSStatus](./midiobjectsetstringproperty%28_,_,_%29.md)
  Sets an object’s string-type property.
- [func MIDIObjectGetIntegerProperty(MIDIObjectRef, CFString, UnsafeMutablePointer<Int32>) -> OSStatus](./midiobjectgetintegerproperty%28_,_,_%29.md)
  Gets an object’s integer-type property.
- [func MIDIObjectSetIntegerProperty(MIDIObjectRef, CFString, Int32) -> OSStatus](./midiobjectsetintegerproperty%28_,_,_%29.md)
  Sets an object’s integer-type property.
- [func MIDIObjectGetDataProperty(MIDIObjectRef, CFString, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus](./midiobjectgetdataproperty%28_,_,_%29.md)
  Gets an object’s data-type property.
- [func MIDIObjectSetDataProperty(MIDIObjectRef, CFString, CFData) -> OSStatus](./midiobjectsetdataproperty%28_,_,_%29.md)
  Sets an object’s data-type property.
- [func MIDIObjectSetDictionaryProperty(MIDIObjectRef, CFString, CFDictionary) -> OSStatus](./midiobjectsetdictionaryproperty%28_,_,_%29.md)
  Sets an object’s dictionary-type property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjectgetdictionaryproperty(_:_:_:))*