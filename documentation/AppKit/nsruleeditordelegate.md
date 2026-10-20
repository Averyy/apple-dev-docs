# NSRuleEditorDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

The `NSRuleEditorDelegate` protocol defines the optional methods implemented by delegates of [`NSRuleEditor`](./nsruleeditor.md) objects.

**Availability**:
- macOS

## Declaration

```swift
protocol NSRuleEditorDelegate : NSObjectProtocol
```

```objc
@protocol NSRuleEditorDelegate <NSObject>
```

## Topics

### Providing Data
- [func ruleEditor(NSRuleEditor, child: Int, forCriterion: Any?, with: NSRuleEditor.RowType) -> Any](./nsruleeditordelegate/ruleeditor%28_,child,forcriterion,with%29.md)
  Returns the child of a given item at a given index.
- [func ruleEditor(NSRuleEditor, displayValueForCriterion: Any, inRow: Int) -> Any](./nsruleeditordelegate/ruleeditor%28_,displayvalueforcriterion,inrow%29.md)
  Returns the value for a given criterion.
- [func ruleEditor(NSRuleEditor, numberOfChildrenForCriterion: Any?, with: NSRuleEditor.RowType) -> Int](./nsruleeditordelegate/ruleeditor%28_,numberofchildrenforcriterion,with%29.md)
  Returns the number of child items of a given criterion or row type.
- [func ruleEditor(NSRuleEditor, predicatePartsForCriterion: Any, withDisplayValue: Any, inRow: Int) -> [NSRuleEditor.PredicatePartKey : Any]?](./nsruleeditordelegate/ruleeditor%28_,predicatepartsforcriterion,withdisplayvalue,inrow%29.md)
  Returns a dictionary representing the parts of the predicate determined by the given criterion and value.
- [NSRuleEditor.PredicatePartKey](./nsruleeditor/predicatepartkey.md)
  These strings are used as keys to the dictionary returned from the delegate’s [`ruleEditor(_:predicatePartsForCriterion:withDisplayValue:inRow:)`](./nsruleeditordelegate/ruleeditor%28_,predicatepartsforcriterion,withdisplayvalue,inrow%29.md) optional method. To construct a valid predicate, the union of the dictionaries for each item in the row must contain the required parts.
### Monitoring Row Changes
- [func ruleEditorRowsDidChange(Notification)](./nsruleeditordelegate/ruleeditorrowsdidchange%28_%29.md)
  Notifies the receiver that a rule editor’s rows changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuring the Delegate
- [var delegate: (any NSRuleEditorDelegate)?](./nsruleeditor/delegate.md)
  The rule editor’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditordelegate)*