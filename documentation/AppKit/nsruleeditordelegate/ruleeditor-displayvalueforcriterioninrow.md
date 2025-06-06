# ruleEditor(_:displayValueForCriterion:inRow:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the value for a given criterion.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func ruleEditor(_ editor: NSRuleEditor, displayValueForCriterion criterion: Any, inRow row: Int) -> Any
```

#### Return Value

The value for `criterion`.

#### Discussion

The value should be an instance of `NSString`, `NSView`, or `NSMenuItem`. If the value is an `NSView` or `NSMenuItem`, you must ensure it is unique for every invocation of this method; that is, do not return a particular instance of `NSView` or `NSMenuItem` more than once.

##### Special Considerations

The delegate must implement this method.

## Parameters

- `editor`: The rule editor that sent the message.
- `criterion`: The criterion for which the value is required.
- `row`: The row number of  .

## See Also

- [func ruleEditor(NSRuleEditor, child: Int, forCriterion: Any?, with: NSRuleEditor.RowType) -> Any](nsruleeditordelegate/ruleeditor(_:child:forcriterion:with:).md)
  Returns the child of a given item at a given index.
- [func ruleEditor(NSRuleEditor, numberOfChildrenForCriterion: Any?, with: NSRuleEditor.RowType) -> Int](nsruleeditordelegate/ruleeditor(_:numberofchildrenforcriterion:with:).md)
  Returns the number of child items of a given criterion or row type.
- [func ruleEditor(NSRuleEditor, predicatePartsForCriterion: Any, withDisplayValue: Any, inRow: Int) -> [NSRuleEditor.PredicatePartKey : Any]?](nsruleeditordelegate/ruleeditor(_:predicatepartsforcriterion:withdisplayvalue:inrow:).md)
  Returns a dictionary representing the parts of the predicate determined by the given criterion and value.
- [NSRuleEditor.PredicatePartKey](nsruleeditor/predicatepartkey.md)
  These strings are used as keys to the dictionary returned from the delegate’s [`ruleEditor(_:predicatePartsForCriterion:withDisplayValue:inRow:)`](nsruleeditordelegate/ruleeditor(_:predicatepartsforcriterion:withdisplayvalue:inrow:).md) optional method. To construct a valid predicate, the union of the dictionaries for each item in the row must contain the required parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditordelegate/ruleeditor(_:displayvalueforcriterion:inrow:))*