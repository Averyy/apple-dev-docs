# BETextSelectionDirectionNavigation

**Framework**: BrowserEngineKit  
**Kind**: protocol

A protocol that defines methods for cursor and selection adjustments.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
protocol BETextSelectionDirectionNavigation
```

#### Overview

This protocol enables your app to request text-cursor movement and selection modifications. In response to a person’s input, the system calls your app in the conditions described by the protocol. Your app performs the requested operation and updates text cursor or selection state accordingly.

## Topics

### Extending the text section
- [func extend(in: UITextLayoutDirection)](betextselectiondirectionnavigation/extend(in:).md)
  Extends text selection in the specified directions, such as in response to an arrow key press while shift is held.
- [func extend(in: UITextStorageDirection, by: UITextGranularity)](betextselectiondirectionnavigation/extend(in:by:).md)
  Moves the selection in the specified directions by granularity, in response to different key combinations:
### Moving the cursor
- [func move(in: UITextLayoutDirection)](betextselectiondirectionnavigation/move(in:).md)
  Moves the cursor in the specified directions, such as in response to an arrow key press.
- [func move(in: UITextStorageDirection, by: UITextGranularity)](betextselectiondirectionnavigation/move(in:by:).md)
  Moves the cursor in the specified directions by granularity, in response to different key combinations:

## Relationships

### Inherited By
- [BETextInput](betextinput.md)

## See Also

- [struct BESelectionFlags](beselectionflags.md)
  Flags that indicate different states or characteristics of a text selection.
- [enum BESelectionTouchPhase](beselectiontouchphase.md)
  The different phases of touch interaction during text selection operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextselectiondirectionnavigation)*