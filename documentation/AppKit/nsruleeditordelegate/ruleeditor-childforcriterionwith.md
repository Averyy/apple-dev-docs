# ruleEditor(_:child:forCriterion:with:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the child of a given item at a given index.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func ruleEditor(_ editor: NSRuleEditor, child index: Int, forCriterion criterion: Any?, with rowType: NSRuleEditor.RowType) -> Any
```

#### Return Value

An object representing the requested child (or root) criterion. This object is used by the delegate to represent that position in the tree, and is passed as a parameter in subsequent calls to the delegate.

#### Discussion

The delegate must implement this method.

## Parameters

- `editor`: The rule editor that sent the message.
- `index`: The index of the requested child criterion. This value must be in the range from   up to (but not including) the number of children, as reported by the delegate in  .
- `criterion`: The parent of the requested child, or   if the rule editor is requesting a root criterion.
- `rowType`: The type of the row.

## See Also

- [Predicate Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789)
- [Control and Cell Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ControlCell/ControlCell.html#//apple_ref/doc/uid/10000015i)
- [func ruleEditor(NSRuleEditor, displayValueForCriterion: Any, inRow: Int) -> Any](nsruleeditordelegate/ruleeditor(_:displayvalueforcriterion:inrow:).md)
  Returns the value for a given criterion.
- [func ruleEditor(NSRuleEditor, numberOfChildrenForCriterion: Any?, with: NSRuleEditor.RowType) -> Int](nsruleeditordelegate/ruleeditor(_:numberofchildrenforcriterion:with:).md)
  Returns the number of child items of a given criterion or row type.
- [func ruleEditor(NSRuleEditor, predicatePartsForCriterion: Any, withDisplayValue: Any, inRow: Int) -> [NSRuleEditor.PredicatePartKey : Any]?](nsruleeditordelegate/ruleeditor(_:predicatepartsforcriterion:withdisplayvalue:inrow:).md)
  Returns a dictionary representing the parts of the predicate determined by the given criterion and value.
- [NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey.md)
  These strings are used as keys to the dictionary returned from the delegate’s [`ruleEditor(_:predicatePartsForCriterion:withDisplayValue:inRow:)`](nsruleeditordelegate/ruleeditor(_:predicatepartsforcriterion:withdisplayvalue:inrow:).md) optional method. To construct a valid predicate, the union of the dictionaries for each item in the row must contain the required parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditordelegate/ruleeditor(_:child:forcriterion:with:))*