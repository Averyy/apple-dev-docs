# BETextSelectionDirectionNavigation

**Framework**: BrowserEngineKit  
**Kind**: protocol

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
protocol BETextSelectionDirectionNavigation
```

## Topics

### Instance Methods
- [func extend(in: UITextLayoutDirection)](betextselectiondirectionnavigation/extend(in:).md)
  Extends text selection in the specified directions, such as in response to an arrow key press while shift is held.
- [func extend(in: UITextStorageDirection, by: UITextGranularity)](betextselectiondirectionnavigation/extend(in:by:).md)
  Moves the selection in the specified directions by granularity, in response to different key combinations:
- [func move(in: UITextLayoutDirection)](betextselectiondirectionnavigation/move(in:).md)
  Moves the cursor in the specified directions, such as in response to an arrow key press.
- [func move(in: UITextStorageDirection, by: UITextGranularity)](betextselectiondirectionnavigation/move(in:by:).md)
  Moves the cursor in the specified directions by granularity, in response to different key combinations:

## Relationships

### Inherited By
- [BETextInput](betextinput.md)

## See Also

- [struct BESelectionFlags](beselectionflags.md)
- [enum BESelectionTouchPhase](beselectiontouchphase.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextselectiondirectionnavigation)*