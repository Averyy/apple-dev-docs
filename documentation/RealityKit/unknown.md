# ||(_:_:)

**Framework**: RealityKit  
**Kind**: op

Returns a predicate which evaluates to `true` if `left` OR `right` evaluates to `true`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
func || <Value>(left: QueryPredicate<Value>, right: QueryPredicate<Value>) -> QueryPredicate<Value>
```

## See Also

- [func ! <Value>(QueryPredicate<Value>) -> QueryPredicate<Value>](!(_:).md)
  Returns a predicate which evaluates to `true` if `operand` evaluates to `false`.
- [func && <Value>(QueryPredicate<Value>, QueryPredicate<Value>) -> QueryPredicate<Value>](&&(_:_:).md)
  Returns a predicate which evaluates to `true` if `left` AND `right` evaluate to `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/__(_:_:))*