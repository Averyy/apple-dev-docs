# MIDIObjectRemoveProperty(_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus MIDIObjectRemoveProperty(MIDIObjectRef obj, CFStringRef propertyID);
```

## Return Value

An `OSStatus` result code.

## Parameters

- `obj`: The object to modify,
- `propertyID`: The property to remove.

## See Also

### Property Accessors
- [func MIDIObjectGetProperties(MIDIObjectRef, UnsafeMutablePointer<Unmanaged<CFPropertyList>?>, Bool) -> OSStatus](./midiobjectgetproperties%28_,_,_%29.md)
  Returns all properties of an object.
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
- [func MIDIObjectGetDictionaryProperty(MIDIObjectRef, CFString, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](./midiobjectgetdictionaryproperty%28_,_,_%29.md)
  Gets an object’s dictionary-type property.
- [func MIDIObjectSetDictionaryProperty(MIDIObjectRef, CFString, CFDictionary) -> OSStatus](./midiobjectsetdictionaryproperty%28_,_,_%29.md)
  Sets an object’s dictionary-type property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjectremoveproperty(_:_:))*