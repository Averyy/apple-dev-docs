# NSRuleEditor.PredicatePartKey

**Framework**: AppKit  
**Kind**: struct

These strings are used as keys to the dictionary returned from the delegate’s [`ruleEditor(_:predicatePartsForCriterion:withDisplayValue:inRow:)`](nsruleeditordelegate/ruleeditor(_:predicatepartsforcriterion:withdisplayvalue:inrow:).md) optional method. To construct a valid predicate, the union of the dictionaries for each item in the row must contain the required parts.

**Availability**:
- macOS ?+

## Declaration

```swift
struct PredicatePartKey
```

## Topics

### Predicate Part Keys
- [static let comparisonModifier: NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey/comparisonmodifier.md)
  The corresponding value is an `NSNumber` object representing a `NSComparisonPredicateModifier` constant the of the predicate.
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
### Initializers
- [init(rawValue: String)](nsruleeditor/predicatepartkey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func ruleEditor(NSRuleEditor, child: Int, forCriterion: Any?, with: NSRuleEditor.RowType) -> Any](nsruleeditordelegate/ruleeditor(_:child:forcriterion:with:).md)
  Returns the child of a given item at a given index.
- [func ruleEditor(NSRuleEditor, displayValueForCriterion: Any, inRow: Int) -> Any](nsruleeditordelegate/ruleeditor(_:displayvalueforcriterion:inrow:).md)
  Returns the value for a given criterion.
- [func ruleEditor(NSRuleEditor, numberOfChildrenForCriterion: Any?, with: NSRuleEditor.RowType) -> Int](nsruleeditordelegate/ruleeditor(_:numberofchildrenforcriterion:with:).md)
  Returns the number of child items of a given criterion or row type.
- [func ruleEditor(NSRuleEditor, predicatePartsForCriterion: Any, withDisplayValue: Any, inRow: Int) -> [NSRuleEditor.PredicatePartKey : Any]?](nsruleeditordelegate/ruleeditor(_:predicatepartsforcriterion:withdisplayvalue:inrow:).md)
  Returns a dictionary representing the parts of the predicate determined by the given criterion and value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/predicatepartkey)*