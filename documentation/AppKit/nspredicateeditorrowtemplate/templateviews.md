# templateViews

**Framework**: AppKit  
**Kind**: property

Returns the views that display this template’s predicate.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var templateViews: [NSView] { get }
```

#### Return Value

The views for an [`NSPredicateEditor`](nspredicateeditor.md) to display in a row that represents the predicate from [`setPredicate(_:)`](nspredicateeditorrowtemplate/setpredicate(_:).md).

#### Discussion

[`NSPredicateEditor`](nspredicateeditor.md) treats instances of [`NSPopUpButton`](nspopupbutton.md) specially by merging their menu items into a single popup button, and by combining menu items with matching titles. In this way, the editor builds a single tree from the separate templates.

## See Also

- [func match(for: NSPredicate) -> Double](nspredicateeditorrowtemplate/match(for:).md)
  Returns a positive number if the receiver can represent a given predicate, and `0` if it cannot.
- [func setPredicate(NSPredicate)](nspredicateeditorrowtemplate/setpredicate(_:).md)
  Sets the value of the views according to the given predicate.
- [func displayableSubpredicates(of: NSPredicate) -> [NSPredicate]?](nspredicateeditorrowtemplate/displayablesubpredicates(of:).md)
  Returns the subpredicates that should be made sub-rows of a given predicate.
- [func predicate(withSubpredicates: [NSPredicate]?) -> NSPredicate](nspredicateeditorrowtemplate/predicate(withsubpredicates:).md)
  Returns the predicate represented by the receiver’s views’ values and the given sub-predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/templateviews)*