# MACaptionAppearanceExecuteBlockForProfileID(_:_:)

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
func MACaptionAppearanceExecuteBlockForProfileID(_ profileID: CFString, _ aBlock: @escaping () -> Void)
```

#### Discussion

Executes a block of code as if the provided profileID was active. This is used in cases such as a need to get the fonts and colors of a profileID without changing the currently selected profileID.

## Parameters

- `profileID`: The profileID which will appear active when executing the block
- `aBlock`: The block of code to execute

## See Also

- [func MACaptionAppearanceCopyProfileIDs() -> CFArray](macaptionappearancecopyprofileids().md)
- [func MACaptionAppearanceSetActiveProfileID(CFString)](macaptionappearancesetactiveprofileid(_:).md)
- [func MACaptionAppearanceCopyActiveProfileID() -> CFString](macaptionappearancecopyactiveprofileid().md)
- [func MACaptionAppearanceCopyProfileName(CFString) -> CFString](macaptionappearancecopyprofilename(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearanceexecuteblockforprofileid(_:_:))*