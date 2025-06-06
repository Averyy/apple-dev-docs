# ruleEditor(_:predicatePartsForCriterion:withDisplayValue:inRow:)

**Framework**: AppKit  
**Kind**: method

Returns a dictionary representing the parts of the predicate determined by the given criterion and value.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func ruleEditor(_ editor: NSRuleEditor, predicatePartsForCriterion criterion: Any, withDisplayValue value: Any, inRow row: Int) -> [NSRuleEditor.PredicatePartKey : Any]?
```

#### Return Value

A dictionary representing the parts of the predicate determined by the given criterion and value. The keys of the dictionary should be the string constants specified in Predicate Part Keys with corresponding appropriate values.

## Parameters

- `editor`: The rule editor that sent the message.
- `criterion`: The criterion for which the predicate parts are required.
- `value`: The display value.
- `row`: The row number of  .

## See Also

- [func ruleEditor(NSRuleEditor, child: Int, forCriterion: Any?, with: NSRuleEditor.RowType) -> Any](nsruleeditordelegate/ruleeditor(_:child:forcriterion:with:).md)
  Returns the child of a given item at a given index.
- [func ruleEditor(NSRuleEditor, displayValueForCriterion: Any, inRow: Int) -> Any](nsruleeditordelegate/ruleeditor(_:displayvalueforcriterion:inrow:).md)
  Returns the value for a given criterion.
- [func ruleEditor(NSRuleEditor, numberOfChildrenForCriterion: Any?, with: NSRuleEditor.RowType) -> Int](nsruleeditordelegate/ruleeditor(_:numberofchildrenforcriterion:with:).md)
  Returns the number of child items of a given criterion or row type.
- [NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey.md)
  These strings are used as keys to the dictionary returned from the delegate’s [`ruleEditor(_:predicatePartsForCriterion:withDisplayValue:inRow:)`](nsruleeditordelegate/ruleeditor(_:predicatepartsforcriterion:withdisplayvalue:inrow:).md) optional method. To construct a valid predicate, the union of the dictionaries for each item in the row must contain the required parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditordelegate/ruleeditor(_:predicatepartsforcriterion:withdisplayvalue:inrow:))*