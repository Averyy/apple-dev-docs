# kMIDIPropertyPrivate

**Framework**: Core MIDI  
**Kind**: var

A Boolean value that indicates whether the system hides an endpoint from other clients.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kMIDIPropertyPrivate: CFString
```

#### Discussion

You can set this property on a device or entity, but it still appears in the API; the system only hides the object’s owned endpoints.

## See Also

- [let kMIDIPropertyOffline: CFString](kmidipropertyoffline.md)
  A Boolean value that indicates whether the object is offline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/kmidipropertyprivate)*