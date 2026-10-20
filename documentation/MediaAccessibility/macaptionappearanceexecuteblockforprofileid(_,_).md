# MACaptionAppearanceExecuteBlockForProfileID(_:_:)

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
func MACaptionAppearanceExecuteBlockForProfileID(_ profileID: CFString, _ aBlock: @escaping () -> Void)
```

```c
extern void MACaptionAppearanceExecuteBlockForProfileID(CFStringRef profileID, void (^aBlock)());
```

#### Discussion

Executes a block of code as if the provided profileID was active. This is used in cases such as a need to get the fonts and colors of a profileID without changing the currently selected profileID.

## Parameters

- `profileID`: The profileID which will appear active when executing the block
- `aBlock`: The block of code to execute

## See Also

### Profile settings
- [func MACaptionAppearanceCopyProfileIDs() -> CFArray](./macaptionappearancecopyprofileids%28%29.md)
- [func MACaptionAppearanceSetActiveProfileID(CFString)](./macaptionappearancesetactiveprofileid%28_%29.md)
- [func MACaptionAppearanceCopyActiveProfileID() -> CFString](./macaptionappearancecopyactiveprofileid%28%29.md)
- [func MACaptionAppearanceCopyProfileName(CFString) -> CFString](./macaptionappearancecopyprofilename%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearanceexecuteblockforprofileid(_:_:))*