# match(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a positive number if the receiver can represent a given predicate, and `0` if it cannot.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func match(for predicate: NSPredicate) -> Double
```

```objc
- (double) matchForPredicate:(NSPredicate *) predicate;
```

#### Return Value

A positive number if the template can represent `predicate`, and `0` if it cannot.

#### Discussion

By default, returns values in the range `0` to `1`.

The highest match among all the templates determines which template is responsible for displaying the predicate. You can override this to determine which predicates your custom template handles.

## See Also

### Primitive Methods
- [var templateViews: [NSView]](./templateviews.md)
  Returns the views that display this template’s predicate.
- [func setPredicate(NSPredicate)](./setpredicate%28_%29.md)
  Sets the value of the views according to the given predicate.
- [func displayableSubpredicates(of: NSPredicate) -> [NSPredicate]?](./displayablesubpredicates%28of%29.md)
  Returns the subpredicates that should be made sub-rows of a given predicate.
- [func predicate(withSubpredicates: [NSPredicate]?) -> NSPredicate](./predicate%28withsubpredicates%29.md)
  Returns the predicate represented by the receiver’s views’ values and the given sub-predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditorrowtemplate/match(for:))*