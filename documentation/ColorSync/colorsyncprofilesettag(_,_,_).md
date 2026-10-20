# ColorSyncProfileSetTag(_:_:_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Sets a tag in a mutable profile.

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
func ColorSyncProfileSetTag(_ prof: ColorSyncMutableProfile!, _ signature: CFString!, _ data: CFData!)
```

```c
extern void ColorSyncProfileSetTag(ColorSyncMutableProfileRef prof, CFStringRef signature, CFDataRef data);
```

## Parameters

- `prof`: The profile in which to set the tag.
- `signature`: The signature of the tag to set in the profile.
- `data`: The tag data.

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
- [func ColorSyncProfileSetHeader(ColorSyncMutableProfile!, CFData!)](./colorsyncprofilesetheader%28_,_%29.md)
  Sets the header of a mutable profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilesettag(_:_:_:))*