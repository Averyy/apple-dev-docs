# ruleEditor(_:child:forCriterion:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the child of a given item at a given index.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func ruleEditor(_ editor: NSRuleEditor, child index: Int, forCriterion criterion: Any?, with rowType: NSRuleEditor.RowType) -> Any
```

```objc
- (id) ruleEditor:(NSRuleEditor *) editor child:(NSInteger) index forCriterion:(id) criterion withRowType:(NSRuleEditorRowType) rowType;
```

#### Return Value

An object representing the requested child (or root) criterion. This object is used by the delegate to represent that position in the tree, and is passed as a parameter in subsequent calls to the delegate.

#### Discussion

The delegate must implement this method.

## Parameters

- `editor`: The rule editor that sent the message.
- `index`: The index of the requested child criterion. This value must be in the range from `0` up to (but not including) the number of children, as reported by the delegate in [`ruleEditor(_:numberOfChildrenForCriterion:with:)`](./ruleeditor%28_,numberofchildrenforcriterion,with%29.md).
- `criterion`: The parent of the requested child, or `nil` if the rule editor is requesting a root criterion.
- `rowType`: The type of the row.

## See Also

### Related Documentation
- [class NSRuleEditor](../nsruleeditor.md)
  An interface for configuring a rule-based list of options.
### Providing Data
- [func ruleEditor(NSRuleEditor, displayValueForCriterion: Any, inRow: Int) -> Any](./ruleeditor%28_,displayvalueforcriterion,inrow%29.md)
  Returns the value for a given criterion.
- [func ruleEditor(NSRuleEditor, numberOfChildrenForCriterion: Any?, with: NSRuleEditor.RowType) -> Int](./ruleeditor%28_,numberofchildrenforcriterion,with%29.md)
  Returns the number of child items of a given criterion or row type.
- [func ruleEditor(NSRuleEditor, predicatePartsForCriterion: Any, withDisplayValue: Any, inRow: Int) -> [NSRuleEditor.PredicatePartKey : Any]?](./ruleeditor%28_,predicatepartsforcriterion,withdisplayvalue,inrow%29.md)
  Returns a dictionary representing the parts of the predicate determined by the given criterion and value.
- [NSRuleEditor.PredicatePartKey](../nsruleeditor/predicatepartkey.md)
  These strings are used as keys to the dictionary returned from the delegate’s [`ruleEditor(_:predicatePartsForCriterion:withDisplayValue:inRow:)`](./ruleeditor%28_,predicatepartsforcriterion,withdisplayvalue,inrow%29.md) optional method. To construct a valid predicate, the union of the dictionaries for each item in the row must contain the required parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditordelegate/ruleeditor(_:child:forcriterion:with:))*