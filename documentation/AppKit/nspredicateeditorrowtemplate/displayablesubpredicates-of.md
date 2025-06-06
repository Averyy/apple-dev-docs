# displayableSubpredicates(of:)

**Framework**: AppKit  
**Kind**: method

Returns the subpredicates that should be made sub-rows of a given predicate.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func displayableSubpredicates(of predicate: NSPredicate) -> [NSPredicate]?
```

#### Return Value

The subpredicates that should be made sub-rows of `predicate`. For compound predicates (instances of [`NSCompoundPredicate`](https://developer.apple.com/documentation/Foundation/NSCompoundPredicate)), the array of subpredicates; for other types of predicate, returns `nil`. If a template represents a predicate in its entirety, or if the predicate has no subpredicates, returns `nil`.

#### Discussion

You can override this method to create custom templates that handle complicated compound predicates.

## Parameters

- `predicate`: A predicate object.

## See Also

- [func match(for: NSPredicate) -> Double](nspredicateeditorrowtemplate/match(for:).md)
  Returns a positive number if the receiver can represent a given predicate, and `0` if it cannot.
- [var templateViews: [NSView]](nspredicateeditorrowtemplate/templateviews.md)
  Returns the views that display this template’s predicate.
- [func setPredicate(NSPredicate)](nspredicateeditorrowtemplate/setpredicate(_:).md)
  Sets the value of the views according to the given predicate.
- [func predicate(withSubpredicates: [NSPredicate]?) -> NSPredicate](nspredicateeditorrowtemplate/predicate(withsubpredicates:).md)
  Returns the predicate represented by the receiver’s views’ values and the given sub-predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/displayablesubpredicates(of:))*