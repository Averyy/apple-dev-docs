# comparisonModifier

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The corresponding value is an `NSNumber` object representing a `NSComparisonPredicateModifier` constant the of the predicate.

**Availability**:
- macOS

## Declaration

```swift
static let comparisonModifier: NSRuleEditor.PredicatePartKey
```

```c
extern NSRuleEditorPredicatePartKey const NSRuleEditorPredicateComparisonModifier;
```

#### Discussion

This value is optional. If not specified, [`NSComparisonPredicate.Modifier.direct`](../../../Foundation/nscomparisonpredicate/modifier/direct.md) is assumed.

## See Also

### Predicate Part Keys
- [static let compoundType: NSRuleEditor.PredicatePartKey](./compoundtype.md)
  The corresponding value is an `NSNumber` object representing a `NSCompoundPredicateType` constant.
- [static let customSelector: NSRuleEditor.PredicatePartKey](./customselector.md)
  The corresponding value is an `NSString` object representing a custom selector.
- [static let leftExpression: NSRuleEditor.PredicatePartKey](./leftexpression.md)
  The corresponding value is an `NSExpression` object representing the left expression in the predicate.
- [static let operatorType: NSRuleEditor.PredicatePartKey](./operatortype.md)
  The corresponding value is an `NSNumber` object representing a `NSPredicateOperatorType` constant.
- [static let options: NSRuleEditor.PredicatePartKey](./options.md)
  The corresponding value is an `NSNumber` object representing an `NSComparisonPredicateOptions` bitfield.
- [static let rightExpression: NSRuleEditor.PredicatePartKey](./rightexpression.md)
  The corresponding value is an `NSExpression` object representing the right expression in the predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/predicatepartkey/comparisonmodifier)*