# comparisonModifier

**Framework**: AppKit  
**Kind**: property

The corresponding value is an `NSNumber` object representing a `NSComparisonPredicateModifier` constant the of the predicate.

**Availability**:
- macOS ?+

## Declaration

```swift
static let comparisonModifier: NSRuleEditor.PredicatePartKey
```

#### Discussion

This value is optional. If not specified, [`NSComparisonPredicate.Modifier.direct`](https://developer.apple.com/documentation/Foundation/NSComparisonPredicate/Modifier/direct) is assumed.

## See Also

- [static let compoundType: NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey/compoundtype.md)
  The corresponding value is an `NSNumber` object representing a `NSCompoundPredicateType` constant.
- [static let customSelector: NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey/customselector.md)
  The corresponding value is an `NSString` object representing a custom selector.
- [static let leftExpression: NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey/leftexpression.md)
  The corresponding value is an `NSExpression` object representing the left expression in the predicate.
- [static let operatorType: NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey/operatortype.md)
  The corresponding value is an `NSNumber` object representing a `NSPredicateOperatorType` constant.
- [static let options: NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey/options.md)
  The corresponding value is an `NSNumber` object representing an `NSComparisonPredicateOptions` bitfield.
- [static let rightExpression: NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey/rightexpression.md)
  The corresponding value is an `NSExpression` object representing the right expression in the predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/predicatepartkey/comparisonmodifier)*