# leftExpression

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The corresponding value is an `NSExpression` object representing the left expression in the predicate.

**Availability**:
- macOS

## Declaration

```swift
static let leftExpression: NSRuleEditor.PredicatePartKey
```

```c
extern NSRuleEditorPredicatePartKey const NSRuleEditorPredicateLeftExpression;
```

## Discussion

This value is required for a non-`nil` comparison predicate.

## See Also

### Predicate Part Keys
- [static let comparisonModifier: NSRuleEditor.PredicatePartKey](./comparisonmodifier.md)
  The corresponding value is an `NSNumber` object representing a `NSComparisonPredicateModifier` constant the of the predicate.
- [static let compoundType: NSRuleEditor.PredicatePartKey](./compoundtype.md)
  The corresponding value is an `NSNumber` object representing a `NSCompoundPredicateType` constant.
- [static let customSelector: NSRuleEditor.PredicatePartKey](./customselector.md)
  The corresponding value is an `NSString` object representing a custom selector.
- [static let operatorType: NSRuleEditor.PredicatePartKey](./operatortype.md)
  The corresponding value is an `NSNumber` object representing a `NSPredicateOperatorType` constant.
- [static let options: NSRuleEditor.PredicatePartKey](./options.md)
  The corresponding value is an `NSNumber` object representing an `NSComparisonPredicateOptions` bitfield.
- [static let rightExpression: NSRuleEditor.PredicatePartKey](./rightexpression.md)
  The corresponding value is an `NSExpression` object representing the right expression in the predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/predicatepartkey/leftexpression)*