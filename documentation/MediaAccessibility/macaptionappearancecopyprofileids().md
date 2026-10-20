# MACaptionAppearanceCopyProfileIDs()

**Framework**: Media Accessibility  
**Kind**: func

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func MACaptionAppearanceCopyProfileIDs() -> CFArray
```

#### Return Value

An array of strings where each string represents a unique caption profile ID.

#### Discussion

Copies all system and user defined profiles, each represented by a CFString containing a non-human-readable ID

## See Also

- [func MACaptionAppearanceSetActiveProfileID(CFString)](macaptionappearancesetactiveprofileid(_:).md)
- [func MACaptionAppearanceCopyActiveProfileID() -> CFString](macaptionappearancecopyactiveprofileid().md)
- [func MACaptionAppearanceCopyProfileName(CFString) -> CFString](macaptionappearancecopyprofilename(_:).md)
- [func MACaptionAppearanceExecuteBlockForProfileID(CFString, () -> Void)](macaptionappearanceexecuteblockforprofileid(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancecopyprofileids())*