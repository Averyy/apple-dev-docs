# allowEvaluation()

**Framework**: Foundation  
**Kind**: method

Forces a securely decoded predicate to allow evaluation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func allowEvaluation()
```

#### Discussion

When securely decoding [`NSPredicate`](nspredicate.md) objects that are encoded using [`NSSecureCoding`](nssecurecoding.md), evaluation is disabled because it is potentially unsafe to evaluate predicates you get out of an archive.

Before you enable evaluation, you should validate key paths, selectors, and other details to ensure no erroneous or malicious code will be executed. Once you’ve verified the predicate, you can enable the receiver for evaluation by calling [`allowEvaluation()`](nspredicate/allowevaluation().md).

## See Also

- [func evaluate(with: Any?) -> Bool](nspredicate/evaluate(with:).md)
  Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies.
- [func evaluate(with: Any?, substitutionVariables: [String : Any]?) -> Bool](nspredicate/evaluate(with:substitutionvariables:).md)
  Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies after substituting in the values from a specified variables dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspredicate/allowevaluation())*