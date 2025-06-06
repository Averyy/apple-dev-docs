# delegate

**Framework**: BrowserEngineKit  
**Kind**: property

The object that manages the drag interaction lifecycle.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
weak var delegate: (any BEDragInteractionDelegate)? { get }
```

#### Discussion

The drag interaction’s delegate object.

#### Overview

The delegate conforms to [`BEDragInteractionDelegate`](bedraginteractiondelegate.md).

## See Also

- [protocol BEDragInteractionDelegate](bedraginteractiondelegate.md)
  A protocol to which the drag interaction delegates conform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedraginteraction/delegate)*