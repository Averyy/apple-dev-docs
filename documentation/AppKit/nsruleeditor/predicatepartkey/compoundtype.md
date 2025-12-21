# compoundType

**Framework**: AppKit  
**Kind**: property

The corresponding value is an `NSNumber` object representing a `NSCompoundPredicateType` constant.

**Availability**:
- macOS ?+

## Declaration

```swift
static let compoundType: NSRuleEditor.PredicatePartKey
```

#### Discussion

If specified, the other keys are ignored and the predicate for the row will be an [`NSCompoundPredicate`](https://developer.apple.com/documentation/Foundation/NSCompoundPredicate) predicate whose subpredicates are the predicates of the subrows of the given row.

## See Also

- [static let comparisonModifier: NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey/comparisonmodifier.md)
  The corresponding value is an `NSNumber` object representing a `NSComparisonPredicateModifier` constant the of the predicate.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/predicatepartkey/compoundtype)*