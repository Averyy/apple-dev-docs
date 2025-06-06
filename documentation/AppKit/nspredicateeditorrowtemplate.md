# NSPredicateEditorRowTemplate

**Framework**: AppKit  
**Kind**: class

A template that describes available predicates and how to display them.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class NSPredicateEditorRowTemplate
```

#### Overview

You can create instances of `NSPredicateEditorRowTemplate` programmatically or in Interface Builder. By default, a noncompound row template has three views: a popup (or static text field) on the left, a popup or static text field for operators, and either a popup or other view on the right.  You can subclass `NSPredicateEditorRowTemplate` to create a row template with different numbers or types of views.

`NSPredicateEditorRowTemplate` is a concrete class, but it has five primitive methods that are called by [`NSPredicateEditor`](nspredicateeditor.md): [`templateViews`](nspredicateeditorrowtemplate/templateviews.md), [`match(for:)`](nspredicateeditorrowtemplate/match(for:).md), [`setPredicate(_:)`](nspredicateeditorrowtemplate/setpredicate(_:).md), [`displayableSubpredicates(of:)`](nspredicateeditorrowtemplate/displayablesubpredicates(of:).md), and [`predicate(withSubpredicates:)`](nspredicateeditorrowtemplate/predicate(withsubpredicates:).md). `NSPredicateEditorRowTemplate` implements all of these methods, but you can override them for custom templates. The primitive methods are used by an instance of `NSPredicateEditor` as follows.

First, an instance of `NSPredicateEditor` is created, and some row templates are set on it—either through a nib file or programmatically. The first thing predicate editor does is ask each of the templates for their views, using [`templateViews`](nspredicateeditorrowtemplate/templateviews.md).

After setting up the predicate editor, you typically send it a [`objectValue`](nscontrol/objectvalue.md) message to restore a saved predicate. `NSPredicateEditor` needs to determine which of its templates should display each predicate in the predicate tree. It does this by sending each of its row templates a [`match(for:)`](nspredicateeditorrowtemplate/match(for:).md) message and choosing the one that returns the highest value.

After finding the best match for a predicate, `NSPredicateEditor` copies that template to get fresh views, inserts them into the proper row, and then sets the predicate on the template using [`setPredicate(_:)`](nspredicateeditorrowtemplate/setpredicate(_:).md). Within that method, the `NSPredicateEditorRowTemplate` object must set its views’ values to represent that predicate.

`NSPredicateEditorRowTemplate` next asks the template for the “displayable sub-predicates” of the predicate by sending a [`displayableSubpredicates(of:)`](nspredicateeditorrowtemplate/displayablesubpredicates(of:).md) message. If a template represents a predicate in its entirety, or if the predicate has no subpredicates, it can return `nil` for this.  Otherwise, it should return a list of predicates to be made into sub-rows of that template’s row. The whole process repeats for each sub-predicate.

At this point, the user sees the predicate that was saved.  If the user then makes some changes to the views of the templates, this causes `NSPredicateEditor` to recompute its predicate by asking each of the templates to return the predicate represented by the new view values, passing in the subpredicates represented by the sub-rows (an empty array if there are none, or `nil` if they aren’t supported by that predicate type):

[`predicate(withSubpredicates:)`](nspredicateeditorrowtemplate/predicate(withsubpredicates:).md)

## Topics

### Initializing a Template
- [init(leftExpressions: [NSExpression], rightExpressions: [NSExpression], modifier: NSComparisonPredicate.Modifier, operators: [NSNumber], options: Int)](nspredicateeditorrowtemplate/init(leftexpressions:rightexpressions:modifier:operators:options:).md)
  Initializes and returns a “pop-up-pop-up-pop-up”–style row template.
- [init(leftExpressions: [NSExpression], rightExpressionAttributeType: NSAttributeType, modifier: NSComparisonPredicate.Modifier, operators: [NSNumber], options: Int)](nspredicateeditorrowtemplate/init(leftexpressions:rightexpressionattributetype:modifier:operators:options:).md)
  Initializes and returns a “pop-up-pop-up-view”–style row template.
- [init(compoundTypes: [NSNumber])](nspredicateeditorrowtemplate/init(compoundtypes:).md)
  Initializes and returns a row template suitable for displaying compound predicates.
### Core Data Integration
- [class func templates(withAttributeKeyPaths: [String], in: NSEntityDescription) -> [NSPredicateEditorRowTemplate]](nspredicateeditorrowtemplate/templates(withattributekeypaths:in:).md)
  Returns an array of predicate templates for the given attribute key paths for a given entity.
### Primitive Methods
- [func match(for: NSPredicate) -> Double](nspredicateeditorrowtemplate/match(for:).md)
  Returns a positive number if the receiver can represent a given predicate, and `0` if it cannot.
- [var templateViews: [NSView]](nspredicateeditorrowtemplate/templateviews.md)
  Returns the views that display this template’s predicate.
- [func setPredicate(NSPredicate)](nspredicateeditorrowtemplate/setpredicate(_:).md)
  Sets the value of the views according to the given predicate.
- [func displayableSubpredicates(of: NSPredicate) -> [NSPredicate]?](nspredicateeditorrowtemplate/displayablesubpredicates(of:).md)
  Returns the subpredicates that should be made sub-rows of a given predicate.
- [func predicate(withSubpredicates: [NSPredicate]?) -> NSPredicate](nspredicateeditorrowtemplate/predicate(withsubpredicates:).md)
  Returns the predicate represented by the receiver’s views’ values and the given sub-predicates.
### Information About a Row Template
- [var leftExpressions: [NSExpression]?](nspredicateeditorrowtemplate/leftexpressions.md)
  Returns the left hand expressions for the receiver.
- [var rightExpressions: [NSExpression]?](nspredicateeditorrowtemplate/rightexpressions.md)
  Returns the right hand expressions for the receiver.
- [var compoundTypes: [NSNumber]?](nspredicateeditorrowtemplate/compoundtypes.md)
  Returns the compound predicate types.
- [var modifier: NSComparisonPredicate.Modifier](nspredicateeditorrowtemplate/modifier.md)
  Returns the comparison predicate modifier for the receiver.
- [var operators: [NSNumber]?](nspredicateeditorrowtemplate/operators.md)
  Returns the array of comparison predicate operators.
- [var options: Int](nspredicateeditorrowtemplate/options.md)
  Returns the comparison predicate options.
- [var rightExpressionAttributeType: NSAttributeType](nspredicateeditorrowtemplate/rightexpressionattributetype.md)
  Returns the attribute type of the receiver’s right expression.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var rowTemplates: [NSPredicateEditorRowTemplate]](nspredicateeditor/rowtemplates.md)
  The row templates for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate)*