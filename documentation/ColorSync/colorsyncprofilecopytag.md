# ColorSyncProfileCopyTag(_:_:)

**Framework**: ColorSync  
**Kind**: func

Copies a tag from a profile.

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
func ColorSyncProfileCopyTag(_ prof: ColorSyncProfile!, _ signature: CFString!) -> Unmanaged<CFData>?
```

#### Return Value

The tag data, or `NULL` in case of failure.

## Parameters

- `prof`: The profile to copy the tag from.
- `signature`: The signature of the tag to copy.

## See Also

- [func ColorSyncProfileContainsTag(ColorSyncProfile!, CFString!) -> Bool](colorsyncprofilecontainstag(_:_:).md)
  Returns a Boolean value indicating whether a profile contains a given tag.
- [func ColorSyncProfileCopyTagSignatures(ColorSyncProfile!) -> Unmanaged<CFArray>?](colorsyncprofilecopytagsignatures(_:).md)
  Copies the tag signatures of a profile.
- [func ColorSyncProfileRemoveTag(ColorSyncMutableProfile!, CFString!)](colorsyncprofileremovetag(_:_:).md)
  Removes a tag from a mutable profile.
- [func ColorSyncProfileSetHeader(ColorSyncMutableProfile!, CFData!)](colorsyncprofilesetheader(_:_:).md)
  Sets the header of a mutable profile.
- [func ColorSyncProfileSetTag(ColorSyncMutableProfile!, CFString!, CFData!)](colorsyncprofilesettag(_:_:_:).md)
  Sets a tag in a mutable profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecopytag(_:_:))*