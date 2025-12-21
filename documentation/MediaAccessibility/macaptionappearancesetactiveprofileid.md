# MACaptionAppearanceSetActiveProfileID(_:)

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
func MACaptionAppearanceSetActiveProfileID(_ profileID: CFString)
```

#### Discussion

Sets the currently-selected caption drawing profileID system wide. Behavior is undefined if NULL or an invalid profileID is provided

## Parameters

- `profileID`: The profileID to make active.

## See Also

- [func MACaptionAppearanceCopyProfileIDs() -> CFArray](macaptionappearancecopyprofileids().md)
- [func MACaptionAppearanceCopyActiveProfileID() -> CFString](macaptionappearancecopyactiveprofileid().md)
- [func MACaptionAppearanceCopyProfileName(CFString) -> CFString](macaptionappearancecopyprofilename(_:).md)
- [func MACaptionAppearanceExecuteBlockForProfileID(CFString, () -> Void)](macaptionappearanceexecuteblockforprofileid(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancesetactiveprofileid(_:))*