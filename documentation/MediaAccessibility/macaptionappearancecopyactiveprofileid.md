# MACaptionAppearanceCopyActiveProfileID()

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
func MACaptionAppearanceCopyActiveProfileID() -> CFString
```

#### Return Value

The currently-selected profileID.

#### Discussion

Gets the currently-selected caption drawing profileID system wide.

## See Also

- [func MACaptionAppearanceCopyProfileIDs() -> CFArray](macaptionappearancecopyprofileids().md)
- [func MACaptionAppearanceSetActiveProfileID(CFString)](macaptionappearancesetactiveprofileid(_:).md)
- [func MACaptionAppearanceCopyProfileName(CFString) -> CFString](macaptionappearancecopyprofilename(_:).md)
- [func MACaptionAppearanceExecuteBlockForProfileID(CFString, () -> Void)](macaptionappearanceexecuteblockforprofileid(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancecopyactiveprofileid())*