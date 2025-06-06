# evaluate()

**Framework**: Foundation  
**Kind**: method

Causes the receiver to evaluate its position.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func evaluate()
```

#### Discussion

Calling [`insertionContainer`](nspositionalspecifier/insertioncontainer.md), [`insertionKey`](nspositionalspecifier/insertionkey.md), [`insertionIndex`](nspositionalspecifier/insertionindex.md), or [`insertionReplaces`](nspositionalspecifier/insertionreplaces.md) also causes the receiver to be evaluated, if it hasn’t already been evaluated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspositionalspecifier/evaluate())*