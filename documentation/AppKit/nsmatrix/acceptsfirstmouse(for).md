# acceptsFirstMouse(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the receiver accepts the first mouse.

**Availability**:
- macOS

## Declaration

```swift
func acceptsFirstMouse(for event: NSEvent?) -> Bool
```

```objc
- (BOOL) acceptsFirstMouse:(NSEvent *) event;
```

## Return Value

[`false`](../../Swift/false.md) if the selection mode of the receiver is `NSListModeMatrix`, [`true`](../../Swift/true.md) if the receiver is in any other selection mode. The receiver does not accept first mouse in `NSListModeMatrix` to prevent the loss of multiple selections.

## Parameters

- `event`: This parameter is ignored.

## See Also

### Related Documentation
- [var mode: NSMatrix.Mode](./mode-swift.property.md)
  The selection mode of the receiver.
### Handling Event and Action Messages
- [func mouseDown(with: NSEvent)](./mousedown%28with%29.md)
  Responds to a mouse-down event.
- [var mouseDownFlags: Int](./mousedownflags.md)
  The flags in effect at the mouse-down event that started the current tracking session.
- [func performKeyEquivalent(with: NSEvent) -> Bool](./performkeyequivalent%28with%29.md)
  Looks for a cell that has the given key equivalent and, if found, makes that cell respond as if clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/acceptsfirstmouse(for:))*