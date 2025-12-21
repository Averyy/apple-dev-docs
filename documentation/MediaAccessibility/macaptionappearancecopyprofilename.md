# MACaptionAppearanceCopyProfileName(_:)

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
func MACaptionAppearanceCopyProfileName(_ profileID: CFString) -> CFString
```

#### Return Value

A human-readable name of the provided profileID

#### Discussion

Copies the human-readable name of a profileID

## Parameters

- `profileID`: The profileID to copy the name of

## See Also

- [func MACaptionAppearanceCopyProfileIDs() -> CFArray](macaptionappearancecopyprofileids().md)
- [func MACaptionAppearanceSetActiveProfileID(CFString)](macaptionappearancesetactiveprofileid(_:).md)
- [func MACaptionAppearanceCopyActiveProfileID() -> CFString](macaptionappearancecopyactiveprofileid().md)
- [func MACaptionAppearanceExecuteBlockForProfileID(CFString, () -> Void)](macaptionappearanceexecuteblockforprofileid(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancecopyprofilename(_:))*