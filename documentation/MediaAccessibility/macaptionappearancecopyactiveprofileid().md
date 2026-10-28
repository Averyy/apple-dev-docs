# MACaptionAppearanceCopyActiveProfileID()

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
func MACaptionAppearanceCopyActiveProfileID() -> CFString
```

```c
extern CFStringRefMACaptionAppearanceCopyActiveProfileID();
```

## Return Value

The currently-selected profileID.

## Discussion

Gets the currently-selected caption drawing profileID system wide.

## See Also

### Profile settings
- [func MACaptionAppearanceCopyProfileIDs() -> CFArray](./macaptionappearancecopyprofileids%28%29.md)
- [func MACaptionAppearanceSetActiveProfileID(CFString)](./macaptionappearancesetactiveprofileid%28_%29.md)
- [func MACaptionAppearanceCopyProfileName(CFString) -> CFString](./macaptionappearancecopyprofilename%28_%29.md)
- [func MACaptionAppearanceExecuteBlockForProfileID(CFString, () -> Void)](./macaptionappearanceexecuteblockforprofileid%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancecopyactiveprofileid())*