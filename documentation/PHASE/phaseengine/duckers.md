# duckers

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

An array of objects that reduce the volume of simultaneously playing sounds.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var duckers: [PHASEDucker] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<PHASEDucker *> * duckers;
```

## See Also

### Managing Groups of Sounds
- [var groups: [String : PHASEGroup]](./groups.md)
  A list of named groups that contain sounds the app operates on collectively.
- [var activeGroupPreset: PHASEGroupPreset?](./activegrouppreset.md)
  The settings that define playback for a group of sounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/duckers)*