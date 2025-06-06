# scrubber(_:didHighlightItemAt:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the item at the specified index was highlighted.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
optional func scrubber(_ scrubber: NSScrubber, didHighlightItemAt highlightedIndex: Int)
```

## Parameters

- `scrubber`: The scrubber object that is notifying you of the highlight change.
- `highlightedIndex`: The index of the item that is now highlighted.

## See Also

- [func scrubber(NSScrubber, didSelectItemAt: Int)](nsscrubberdelegate/scrubber(_:didselectitemat:).md)
  Tells the delegate that the item at the specified index was selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberdelegate/scrubber(_:didhighlightitemat:))*