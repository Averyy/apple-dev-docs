# MIDIObjectGetProperties(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

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

#### Return Value

An `OSStatus` result code.

#### Discussion

The property list may be a dictionary or an array. Dictionaries map property names ([`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString)) to values, which may be [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber), [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString), or [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData). Arrays provide collections of other property list types.

Properties that an object inherits from its owning object aren’t included.

## Parameters

- `obj`: The object to query.
- `outProperties`: On successful return, the object’s properties.
- `deep`: Specify   to include the object’s children; for example, a device’s entities, or an entity’s endpoints.

## See Also

- [func MIDIObjectRemoveProperty(MIDIObjectRef, CFString) -> OSStatus](midiobjectremoveproperty(_:_:).md)
  Removes an object’s property.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjectgetproperties(_:_:_:))*