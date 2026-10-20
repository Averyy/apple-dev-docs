# performKeyEquivalent(with:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func performKeyEquivalent(with nsEvent: NSEvent) -> Bool
```

## See Also

### Managing keyboard interaction
- [func keyDown(with: NSEvent)](./keydown%28with%29.md)
  Called when the user presses a key on the keyboard while this view is in the responder chain.
- [func keyUp(with: NSEvent)](./keyup%28with%29.md)
  Called when the user releases a key on the keyboard while this view is in the responder chain.
- [func insertText(Any)](./inserttext%28_%29.md)
- [func didChangeValue(forKey: String)](./didchangevalue%28forkey%29.md)
- [func makeTouchBar() -> NSTouchBar?](./maketouchbar%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingview/performkeyequivalent(with:))*