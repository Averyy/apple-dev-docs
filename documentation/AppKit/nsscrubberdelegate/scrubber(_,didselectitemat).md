# scrubber(_:didSelectItemAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the item at the specified index was selected.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
optional func scrubber(_ scrubber: NSScrubber, didSelectItemAt selectedIndex: Int)
```

```objc
- (void) scrubber:(NSScrubber *) scrubber didSelectItemAtIndex:(NSInteger) selectedIndex;
```

## Parameters

- `scrubber`: The scrubber object that is notifying you of the selection change.
- `selectedIndex`: The index of the item that was selected.

## See Also

### Handling item selection and highlighting
- [func scrubber(NSScrubber, didHighlightItemAt: Int)](./scrubber%28_,didhighlightitemat%29.md)
  Tells the delegate that the item at the specified index was highlighted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberdelegate/scrubber(_:didselectitemat:))*