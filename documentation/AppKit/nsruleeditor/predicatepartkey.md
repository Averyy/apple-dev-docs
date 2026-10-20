# NSRuleEditor.PredicatePartKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

These strings are used as keys to the dictionary returned from the delegate’s [`ruleEditor(_:predicatePartsForCriterion:withDisplayValue:inRow:)`](../nsruleeditordelegate/ruleeditor%28_,predicatepartsforcriterion,withdisplayvalue,inrow%29.md) optional method. To construct a valid predicate, the union of the dictionaries for each item in the row must contain the required parts.

**Availability**:
- macOS

## Declaration

```swift
struct PredicatePartKey
```

```c
typedef NSString * NSRuleEditorPredicatePartKey;
```

## Topics

### Predicate Part Keys
- [static let comparisonModifier: NSRuleEditor.PredicatePartKey](./predicatepartkey/comparisonmodifier.md)
  The corresponding value is an `NSNumber` object representing a `NSComparisonPredicateModifier` constant the of the predicate.
- [static let compoundType: NSRuleEditor.PredicatePartKey](./predicatepartkey/compoundtype.md)
  The corresponding value is an `NSNumber` object representing a `NSCompoundPredicateType` constant.
- [static let customSelector: NSRuleEditor.PredicatePartKey](./predicatepartkey/customselector.md)
  The corresponding value is an `NSString` object representing a custom selector.
- [static let leftExpression: NSRuleEditor.PredicatePartKey](./predicatepartkey/leftexpression.md)
  The corresponding value is an `NSExpression` object representing the left expression in the predicate.
- [static let operatorType: NSRuleEditor.PredicatePartKey](./predicatepartkey/operatortype.md)
  The corresponding value is an `NSNumber` object representing a `NSPredicateOperatorType` constant.
- [static let options: NSRuleEditor.PredicatePartKey](./predicatepartkey/options.md)
  The corresponding value is an `NSNumber` object representing an `NSComparisonPredicateOptions` bitfield.
- [static let rightExpression: NSRuleEditor.PredicatePartKey](./predicatepartkey/rightexpression.md)
  The corresponding value is an `NSExpression` object representing the right expression in the predicate.
### Initializers
- [init(rawValue: String)](./predicatepartkey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Providing Data
- [func ruleEditor(NSRuleEditor, child: Int, forCriterion: Any?, with: NSRuleEditor.RowType) -> Any](../nsruleeditordelegate/ruleeditor%28_,child,forcriterion,with%29.md)
  Returns the child of a given item at a given index.
- [func ruleEditor(NSRuleEditor, displayValueForCriterion: Any, inRow: Int) -> Any](../nsruleeditordelegate/ruleeditor%28_,displayvalueforcriterion,inrow%29.md)
  Returns the value for a given criterion.
- [func ruleEditor(NSRuleEditor, numberOfChildrenForCriterion: Any?, with: NSRuleEditor.RowType) -> Int](../nsruleeditordelegate/ruleeditor%28_,numberofchildrenforcriterion,with%29.md)
  Returns the number of child items of a given criterion or row type.
- [func ruleEditor(NSRuleEditor, predicatePartsForCriterion: Any, withDisplayValue: Any, inRow: Int) -> [NSRuleEditor.PredicatePartKey : Any]?](../nsruleeditordelegate/ruleeditor%28_,predicatepartsforcriterion,withdisplayvalue,inrow%29.md)
  Returns a dictionary representing the parts of the predicate determined by the given criterion and value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/predicatepartkey)*