# evaluate()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Causes the receiver to evaluate its position.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func evaluate()
```

```objc
- (void) evaluate;
```

## Discussion

Calling [`insertionContainer`](./insertioncontainer.md), [`insertionKey`](./insertionkey.md), [`insertionIndex`](./insertionindex.md), or [`insertionReplaces`](./insertionreplaces.md) also causes the receiver to be evaluated, if it hasn’t already been evaluated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspositionalspecifier/evaluate())*