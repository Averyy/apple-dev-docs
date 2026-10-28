# MIDIObjectGetProperties(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Returns all properties of an object.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.1+
- visionOS 1.0+

## Declaration

```swift
func MIDIObjectGetProperties(_ obj: MIDIObjectRef, _ outProperties: UnsafeMutablePointer<Unmanaged<CFPropertyList>?>, _ deep: Bool) -> OSStatus
```

```c
extern OSStatus MIDIObjectGetProperties(MIDIObjectRef obj, CFPropertyListRef*outProperties, Boolean deep);
```

## Return Value

An `OSStatus` result code.

## Discussion

The property list may be a dictionary or an array. Dictionaries map property names ([`CFString`](../CoreFoundation/cfstring.md)) to values, which may be [`CFNumber`](../CoreFoundation/cfnumber.md), [`CFString`](../CoreFoundation/cfstring.md), or [`CFData`](../CoreFoundation/cfdata.md). Arrays provide collections of other property list types.

Properties that an object inherits from its owning object aren’t included.

## Parameters

- `obj`: The object to query.
- `outProperties`: On successful return, the object’s properties.
- `deep`: Specify `true` to include the object’s children; for example, a device’s entities, or an entity’s endpoints.

## See Also

### Property Accessors
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
- [func MIDIObjectGetDictionaryProperty(MIDIObjectRef, CFString, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](./midiobjectgetdictionaryproperty%28_,_,_%29.md)
  Gets an object’s dictionary-type property.
- [func MIDIObjectSetDictionaryProperty(MIDIObjectRef, CFString, CFDictionary) -> OSStatus](./midiobjectsetdictionaryproperty%28_,_,_%29.md)
  Sets an object’s dictionary-type property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjectgetproperties(_:_:_:))*