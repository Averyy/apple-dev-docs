# activeGroupPreset

**Framework**: PHASE  
**Kind**: property

The settings that define playback for a group of sounds.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var activeGroupPreset: PHASEGroupPreset? { get }
```

#### Discussion

This property returns the most recent group preset on which the app calls [`activate()`](phasegrouppreset/activate().md). Group presets map a collection of sounds in a group to settings the app applies in a specific context. For more information, see [`PHASEGroupPreset`](phasegrouppreset.md).

## See Also

- [var groups: [String : PHASEGroup]](phaseengine/groups.md)
  A list of named groups that contain sounds the app operates on collectively.
- [var duckers: [PHASEDucker]](phaseengine/duckers.md)
  An array of objects that reduce the volume of simultaneously playing sounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/activegrouppreset)*