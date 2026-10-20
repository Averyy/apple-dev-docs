# keyDown(with:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Called when the user presses a key on the keyboard while this view is in the responder chain.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func keyDown(with event: NSEvent)
```

## See Also

### Managing keyboard interaction
- [func keyUp(with: NSEvent)](./keyup%28with%29.md)
  Called when the user releases a key on the keyboard while this view is in the responder chain.
- [func performKeyEquivalent(with: NSEvent) -> Bool](./performkeyequivalent%28with%29.md)
- [func insertText(Any)](./inserttext%28_%29.md)
- [func didChangeValue(forKey: String)](./didchangevalue%28forkey%29.md)
- [func makeTouchBar() -> NSTouchBar?](./maketouchbar%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingview/keydown(with:))*