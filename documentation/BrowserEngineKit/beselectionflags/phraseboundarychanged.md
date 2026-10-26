# phraseBoundaryChanged

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Type Property

A flag that indicates whether a text selection crosses or modifies phrase boundaries in an active selection.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
static var phraseBoundaryChanged: BESelectionFlags { get }
```

```c
BEPhraseBoundaryChanged
```

## See Also

### Describing a text selection
- [static var selectionFlipped: BESelectionFlags](./selectionflipped.md)
  A flag that indicates whether a text selection is reversed or flipped in direction from its original direction.
- [static var wordIsNearTap: BESelectionFlags](./wordisneartap.md)
  A flag that indicates whether a word resides near the person’s tap gesture.
- [BESelectionFlagsNone](./beselectionflagsnone.md)
  An option that indicates no active flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beselectionflags/phraseboundarychanged)*