# evaluate(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) evaluateWithObject:(id) object;
```

## Return Value

[`true`](../../Swift/true.md) if `object` matches the conditions specified by the predicate, otherwise [`false`](../../Swift/false.md).

## Parameters

- `object`: The object against which to evaluate the predicate.

## See Also

### Evaluating a Predicate
- [func evaluate(with: Any?, substitutionVariables: [String : Any]?) -> Bool](./evaluate%28with,substitutionvariables%29.md)
  Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies after substituting in the values from a specified variables dictionary.
- [func allowEvaluation()](./allowevaluation%28%29.md)
  Forces a securely decoded predicate to allow evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspredicate/evaluate(with:))*