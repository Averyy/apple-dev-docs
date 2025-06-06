# predicate(withSubpredicates:)

**Framework**: AppKit  
**Kind**: method

Returns the predicate represented by the receiver’s views’ values and the given sub-predicates.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func predicate(withSubpredicates subpredicates: [NSPredicate]?) -> NSPredicate
```

#### Return Value

The predicate represented by the values of the template’s views and the given subpredicates. You can override this method to return the predicate represented by your custom views.

#### Discussion

This method is only called if [`match(for:)`](nspredicateeditorrowtemplate/match(for:).md) returned a positive value for the receiver.

You can override this method to return the predicate represented by a custom view.

## Parameters

- `subpredicates`: An array of predicates.

## See Also

- [func match(for: NSPredicate) -> Double](nspredicateeditorrowtemplate/match(for:).md)
  Returns a positive number if the receiver can represent a given predicate, and `0` if it cannot.
- [var templateViews: [NSView]](nspredicateeditorrowtemplate/templateviews.md)
  Returns the views that display this template’s predicate.
- [func setPredicate(NSPredicate)](nspredicateeditorrowtemplate/setpredicate(_:).md)
  Sets the value of the views according to the given predicate.
- [func displayableSubpredicates(of: NSPredicate) -> [NSPredicate]?](nspredicateeditorrowtemplate/displayablesubpredicates(of:).md)
  Returns the subpredicates that should be made sub-rows of a given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/predicate(withsubpredicates:))*