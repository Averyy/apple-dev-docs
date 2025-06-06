# setPredicate(_:)

**Framework**: AppKit  
**Kind**: method

Sets the value of the views according to the given predicate.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setPredicate(_ predicate: NSPredicate)
```

#### Discussion

This method is only called if [`match(for:)`](nspredicateeditorrowtemplate/match(for:).md) returned a positive value for the receiver.

You can override this to set the values of custom views.

## Parameters

- `predicate`: The predicate value for the receiver.

## See Also

- [func match(for: NSPredicate) -> Double](nspredicateeditorrowtemplate/match(for:).md)
  Returns a positive number if the receiver can represent a given predicate, and `0` if it cannot.
- [var templateViews: [NSView]](nspredicateeditorrowtemplate/templateviews.md)
  Returns the views that display this template’s predicate.
- [func displayableSubpredicates(of: NSPredicate) -> [NSPredicate]?](nspredicateeditorrowtemplate/displayablesubpredicates(of:).md)
  Returns the subpredicates that should be made sub-rows of a given predicate.
- [func predicate(withSubpredicates: [NSPredicate]?) -> NSPredicate](nspredicateeditorrowtemplate/predicate(withsubpredicates:).md)
  Returns the predicate represented by the receiver’s views’ values and the given sub-predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/setpredicate(_:))*