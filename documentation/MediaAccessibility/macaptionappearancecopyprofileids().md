# MACaptionAppearanceCopyProfileIDs()

**Framework**: Media Accessibility  
**Kind**: func  
**Role**: Function

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

```c
extern CFArrayRefMACaptionAppearanceCopyProfileIDs();
```

#### Return Value

An array of strings where each string represents a unique caption profile ID.

#### Discussion

Copies all system and user defined profiles, each represented by a CFString containing a non-human-readable ID

## See Also

### Profile settings
- [func MACaptionAppearanceSetActiveProfileID(CFString)](./macaptionappearancesetactiveprofileid%28_%29.md)
- [func MACaptionAppearanceCopyActiveProfileID() -> CFString](./macaptionappearancecopyactiveprofileid%28%29.md)
- [func MACaptionAppearanceCopyProfileName(CFString) -> CFString](./macaptionappearancecopyprofilename%28_%29.md)
- [func MACaptionAppearanceExecuteBlockForProfileID(CFString, () -> Void)](./macaptionappearanceexecuteblockforprofileid%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancecopyprofileids())*