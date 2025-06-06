# invalidate()

**Framework**: Core NFC  
**Kind**: method

Invalidates the current card emulation session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func invalidate()
```

#### Discussion

This call stops any currently-running card emulation.

To restart, create a new [`CardSession`](cardsession.md) instance with `startSession()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/invalidate())*