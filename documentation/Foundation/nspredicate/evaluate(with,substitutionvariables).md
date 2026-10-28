# evaluate(with:substitutionVariables:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) evaluateWithObject:(id) object substitutionVariables:(NSDictionary<NSString *,id> *) bindings;
```

## Return Value

[`true`](../../Swift/true.md) if `object` matches the conditions specified by the predicate after substituting in the values in `bindings` for any replacement tokens, otherwise [`false`](../../Swift/false.md).

## Discussion

This method returns the same result as the two step process of first invoking [`withSubstitutionVariables(_:)`](./withsubstitutionvariables%28_%29.md) on the predicate and then invoking [`evaluate(with:)`](./evaluate%28with%29.md) on the returned value. This method is optimized for situations which require repeatedly evaluating a predicate with substitution variables with different variable substitutions.

## Parameters

- `object`: The object against which to evaluate the predicate.
- `bindings`: The substitution variables dictionary. The dictionary must contain key-value pairs for all variables in the predicate.

## See Also

### Evaluating a Predicate
- [func evaluate(with: Any?) -> Bool](./evaluate%28with%29.md)
  Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies.
- [func allowEvaluation()](./allowevaluation%28%29.md)
  Forces a securely decoded predicate to allow evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspredicate/evaluate(with:substitutionvariables:))*