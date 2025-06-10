# operatorType

**Framework**: AppKit  
**Kind**: property

The corresponding value is an `NSNumber` object representing a [`NSComparisonPredicate.Operator`](https://developer.apple.com/documentation/Foundation/NSComparisonPredicate/Operator) constant.

**Availability**:
- macOS ?+

## Declaration

```swift
static let operatorType: NSRuleEditor.PredicatePartKey
```

#### Discussion

This value is required for a non-`nil` comparison predicate.

## See Also

- [static let comparisonModifier: NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey/comparisonmodifier.md)
  The corresponding value is an `NSNumber` object representing a [`NSComparisonPredicate.Modifier`](https://developer.apple.com/documentation/Foundation/NSComparisonPredicate/Modifier) constant the of the predicate.
- [static let compoundType: NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey/compoundtype.md)
  The corresponding value is an `NSNumber` object representing a [`NSCompoundPredicate.LogicalType`](https://developer.apple.com/documentation/Foundation/NSCompoundPredicate/LogicalType) constant.
- [static let customSelector: NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey/customselector.md)
  The corresponding value is an `NSString` object representing a custom selector.
- [static let leftExpression: NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey/leftexpression.md)
  The corresponding value is an `NSExpression` object representing the left expression in the predicate.
- [static let options: NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey/options.md)
  The corresponding value is an `NSNumber` object representing a NSComparisonPredicate_Optionsbitfield.
- [static let rightExpression: NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey/rightexpression.md)
  The corresponding value is an `NSExpression` object representing the right expression in the predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/predicatepartkey/operatortype)*