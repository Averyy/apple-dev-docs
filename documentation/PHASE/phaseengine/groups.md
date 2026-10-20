# groups

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

A list of named groups that contain sounds the app operates on collectively.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var groups: [String : PHASEGroup] { get }
```

```objc
@property (nonatomic, copy, readonly) NSDictionary<NSString *,PHASEGroup *> * groups;
```

## See Also

### Managing Groups of Sounds
- [var activeGroupPreset: PHASEGroupPreset?](./activegrouppreset.md)
  The settings that define playback for a group of sounds.
- [var duckers: [PHASEDucker]](./duckers.md)
  An array of objects that reduce the volume of simultaneously playing sounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/groups)*