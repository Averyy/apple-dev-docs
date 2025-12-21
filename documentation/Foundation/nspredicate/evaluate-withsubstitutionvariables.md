# evaluate(with:substitutionVariables:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies after substituting in the values from a specified variables dictionary.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func evaluate(with object: Any?, substitutionVariables bindings: [String : Any]?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `object` matches the conditions specified by the predicate after substituting in the values in `bindings` for any replacement tokens, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method returns the same result as the two step process of first invoking [`withSubstitutionVariables(_:)`](nspredicate/withsubstitutionvariables(_:).md) on the predicate and then invoking [`evaluate(with:)`](nspredicate/evaluate(with:).md) on the returned value. This method is optimized for situations which require repeatedly evaluating a predicate with substitution variables with different variable substitutions.

## Parameters

- `object`: The object against which to evaluate the predicate.
- `bindings`: The substitution variables dictionary. The dictionary must contain key-value pairs for all variables in the predicate.

## See Also

- [func evaluate(with: Any?) -> Bool](nspredicate/evaluate(with:).md)
  Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies.
- [func allowEvaluation()](nspredicate/allowevaluation.md)
  Forces a securely decoded predicate to allow evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspredicate/evaluate(with:substitutionvariables:))*