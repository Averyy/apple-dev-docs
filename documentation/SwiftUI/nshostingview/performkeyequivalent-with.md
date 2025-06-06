# performKeyEquivalent(with:)

**Framework**: SwiftUI  
**Kind**: method

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func performKeyEquivalent(with nsEvent: NSEvent) -> Bool
```

## See Also

- [func keyDown(with: NSEvent)](nshostingview/keydown(with:).md)
  Called when the user presses a key on the keyboard while this view is in the responder chain.
- [func keyUp(with: NSEvent)](nshostingview/keyup(with:).md)
  Called when the user releases a key on the keyboard while this view is in the responder chain.
- [func insertText(Any)](nshostingview/inserttext(_:).md)
- [func didChangeValue(forKey: String)](nshostingview/didchangevalue(forkey:).md)
- [func makeTouchBar() -> NSTouchBar?](nshostingview/maketouchbar.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingview/performkeyequivalent(with:))*