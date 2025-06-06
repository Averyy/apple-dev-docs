# ==(_:_:)

**Framework**: App Intents  
**Kind**: op

Returns a Boolean value indicating whether two values are equal.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
static func == (lhs: IntentParameter<Value>.ValueState, rhs: IntentParameter<Value>.ValueState) -> Bool
```

#### Discussion

Equality is the inverse of inequality. For any values `a` and `b`, `a == b` implies that `a != b` is `false`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/valuestate-swift.enum/==(_:_:))*