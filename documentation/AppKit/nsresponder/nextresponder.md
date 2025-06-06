# nextResponder

**Framework**: AppKit  
**Kind**: property

The next responder after this one, or `nil` if it has none.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
unowned(unsafe) var nextResponder: NSResponder? { get set }
```

#### Discussion

The next responder must be an object that inherits, directly or indirectly, from `NSResponder`.

## See Also

- [func noResponder(for: Selector)](nsresponder/noresponder(for:).md)
  Handles the case where an event or action message falls off the end of the responder chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/nextresponder)*