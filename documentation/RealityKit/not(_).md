# !(_:)

**Framework**: RealityKit  
**Kind**: op  
**Role**: Operator

Returns a predicate which evaluates to `true` if `operand` evaluates to `false`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
func ! <Value>(operand: QueryPredicate<Value>) -> QueryPredicate<Value>
```

## See Also

### Comparing predicates
- [func && <Value>(QueryPredicate<Value>, QueryPredicate<Value>) -> QueryPredicate<Value>](./ampamp%28_,_%29.md)
  Returns a predicate which evaluates to `true` if `left` AND `right` evaluate to `true`.
- [func || <Value>(QueryPredicate<Value>, QueryPredicate<Value>) -> QueryPredicate<Value>](./opop%28_,_%29.md)
  Returns a predicate which evaluates to `true` if `left` OR `right` evaluates to `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/!(_:))*