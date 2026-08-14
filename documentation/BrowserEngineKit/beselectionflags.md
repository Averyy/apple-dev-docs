# BESelectionFlags

**Framework**: BrowserEngineKit  
**Kind**: struct

Flags that indicate different states or characteristics of a text selection.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS ?+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
struct BESelectionFlags
```

#### Overview

The [`BETextInput`](betextinput.md) protocol provides your app an instance of this structure as an argument to the  [`adjustSelectionBoundary(to:touchPhase:baseIsStart:flags:)`](betextinput/adjustselectionboundary(to:touchphase:baseisstart:flags:).md) callback.

## Topics

### Describing a text selection
- [static var phraseBoundaryChanged: BESelectionFlags](beselectionflags/phraseboundarychanged.md)
  A flag that indicates whether a text selection crosses or modifies phrase boundaries in an active selection.
- [static var selectionFlipped: BESelectionFlags](beselectionflags/selectionflipped.md)
  A flag that indicates whether a text selection is reversed or flipped in direction from its original direction.
- [static var wordIsNearTap: BESelectionFlags](beselectionflags/wordisneartap.md)
  A flag that indicates whether a word resides near the person’s tap gesture.
### Creating a selection flag
- [init(rawValue: UInt)](beselectionflags/init(rawvalue:).md)
  Creates a selection flags instance with the given underlying value.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [protocol BETextSelectionDirectionNavigation](betextselectiondirectionnavigation.md)
  A protocol that defines methods for cursor and selection adjustments.
- [enum BESelectionTouchPhase](beselectiontouchphase.md)
  The different phases of touch interaction during text selection operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beselectionflags)*