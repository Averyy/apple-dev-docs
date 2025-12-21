# evaluate(with:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func evaluate(with object: Any?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `object` matches the conditions specified by the predicate, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `object`: The object against which to evaluate the predicate.

## See Also

- [func evaluate(with: Any?, substitutionVariables: [String : Any]?) -> Bool](nspredicate/evaluate(with:substitutionvariables:).md)
  Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies after substituting in the values from a specified variables dictionary.
- [func allowEvaluation()](nspredicate/allowevaluation.md)
  Forces a securely decoded predicate to allow evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspredicate/evaluate(with:))*