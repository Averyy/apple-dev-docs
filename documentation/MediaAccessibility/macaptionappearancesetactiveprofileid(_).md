# MACaptionAppearanceSetActiveProfileID(_:)

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
func MACaptionAppearanceSetActiveProfileID(_ profileID: CFString)
```

```c
extern void MACaptionAppearanceSetActiveProfileID(CFStringRef profileID);
```

#### Discussion

Sets the currently-selected caption drawing profileID system wide. Behavior is undefined if NULL or an invalid profileID is provided

## Parameters

- `profileID`: The profileID to make active.

## See Also

### Profile settings
- [func MACaptionAppearanceCopyProfileIDs() -> CFArray](./macaptionappearancecopyprofileids%28%29.md)
- [func MACaptionAppearanceCopyActiveProfileID() -> CFString](./macaptionappearancecopyactiveprofileid%28%29.md)
- [func MACaptionAppearanceCopyProfileName(CFString) -> CFString](./macaptionappearancecopyprofilename%28_%29.md)
- [func MACaptionAppearanceExecuteBlockForProfileID(CFString, () -> Void)](./macaptionappearanceexecuteblockforprofileid%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancesetactiveprofileid(_:))*