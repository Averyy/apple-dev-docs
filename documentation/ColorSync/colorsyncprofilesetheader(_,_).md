# ColorSyncProfileSetHeader(_:_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Sets the header of a mutable profile.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func ColorSyncProfileSetHeader(_ prof: ColorSyncMutableProfile!, _ header: CFData!)
```

```c
extern void ColorSyncProfileSetHeader(ColorSyncMutableProfileRef prof, CFDataRef header);
```

## Parameters

- `prof`: The profile in which to set the header.
- `header`: The header data (must be in host endianness).

## See Also

### Managing tags and the header
- [func ColorSyncProfileContainsTag(ColorSyncProfile!, CFString!) -> Bool](./colorsyncprofilecontainstag%28_,_%29.md)
  Returns a Boolean value indicating whether a profile contains a given tag.
- [func ColorSyncProfileCopyTag(ColorSyncProfile!, CFString!) -> Unmanaged<CFData>?](./colorsyncprofilecopytag%28_,_%29.md)
  Copies a tag from a profile.
- [func ColorSyncProfileCopyTagSignatures(ColorSyncProfile!) -> Unmanaged<CFArray>?](./colorsyncprofilecopytagsignatures%28_%29.md)
  Copies the tag signatures of a profile.
- [func ColorSyncProfileRemoveTag(ColorSyncMutableProfile!, CFString!)](./colorsyncprofileremovetag%28_,_%29.md)
  Removes a tag from a mutable profile.
- [func ColorSyncProfileSetTag(ColorSyncMutableProfile!, CFString!, CFData!)](./colorsyncprofilesettag%28_,_,_%29.md)
  Sets a tag in a mutable profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilesetheader(_:_:))*