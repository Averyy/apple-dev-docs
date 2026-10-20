# templateViews

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the views that display this template’s predicate.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var templateViews: [NSView] { get }
```

```objc
@property (copy, readonly) NSArray<NSView *> * templateViews;
```

#### Return Value

The views for an [`NSPredicateEditor`](../nspredicateeditor.md) to display in a row that represents the predicate from [`setPredicate(_:)`](./setpredicate%28_%29.md).

#### Discussion

[`NSPredicateEditor`](../nspredicateeditor.md) treats instances of [`NSPopUpButton`](../nspopupbutton.md) specially by merging their menu items into a single popup button, and by combining menu items with matching titles. In this way, the editor builds a single tree from the separate templates.

## See Also

### Primitive Methods
- [func match(for: NSPredicate) -> Double](./match%28for%29.md)
  Returns a positive number if the receiver can represent a given predicate, and `0` if it cannot.
- [func setPredicate(NSPredicate)](./setpredicate%28_%29.md)
  Sets the value of the views according to the given predicate.
- [func displayableSubpredicates(of: NSPredicate) -> [NSPredicate]?](./displayablesubpredicates%28of%29.md)
  Returns the subpredicates that should be made sub-rows of a given predicate.
- [func predicate(withSubpredicates: [NSPredicate]?) -> NSPredicate](./predicate%28withsubpredicates%29.md)
  Returns the predicate represented by the receiver’s views’ values and the given sub-predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/templateviews)*