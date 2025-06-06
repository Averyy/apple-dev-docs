# ruleEditor(_:numberOfChildrenForCriterion:with:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the number of child items of a given criterion or row type.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func ruleEditor(_ editor: NSRuleEditor, numberOfChildrenForCriterion criterion: Any?, with rowType: NSRuleEditor.RowType) -> Int
```

#### Return Value

The number of child items of `criterion`. If `criterion` is `nil`, return the number of root criteria for the row type `rowType`.

#### Discussion

The delegate must implement this method.

## Parameters

- `editor`: The rule editor that sent the message.
- `criterion`: The criterion for which the number of children is required.
- `rowType`: The type of row of  .

## See Also

- [func ruleEditor(NSRuleEditor, child: Int, forCriterion: Any?, with: NSRuleEditor.RowType) -> Any](nsruleeditordelegate/ruleeditor(_:child:forcriterion:with:).md)
  Returns the child of a given item at a given index.
- [func ruleEditor(NSRuleEditor, displayValueForCriterion: Any, inRow: Int) -> Any](nsruleeditordelegate/ruleeditor(_:displayvalueforcriterion:inrow:).md)
  Returns the value for a given criterion.
- [func ruleEditor(NSRuleEditor, predicatePartsForCriterion: Any, withDisplayValue: Any, inRow: Int) -> [NSRuleEditor.PredicatePartKey : Any]?](nsruleeditordelegate/ruleeditor(_:predicatepartsforcriterion:withdisplayvalue:inrow:).md)
  Returns a dictionary representing the parts of the predicate determined by the given criterion and value.
- [NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey.md)
  These strings are used as keys to the dictionary returned from the delegate’s [`ruleEditor(_:predicatePartsForCriterion:withDisplayValue:inRow:)`](nsruleeditordelegate/ruleeditor(_:predicatepartsforcriterion:withdisplayvalue:inrow:).md) optional method. To construct a valid predicate, the union of the dictionaries for each item in the row must contain the required parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditordelegate/ruleeditor(_:numberofchildrenforcriterion:with:))*