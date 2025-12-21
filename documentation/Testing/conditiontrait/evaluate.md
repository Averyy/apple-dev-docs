# evaluate()

**Framework**: Swift Testing  
**Kind**: method

Evaluate this instance’s underlying condition.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
func evaluate() async throws -> Bool
```

#### Return Value

The result of evaluating this instance’s underlying condition.

#### Discussion

The evaluation is performed each time this function is called, and is not cached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/conditiontrait/evaluate())*