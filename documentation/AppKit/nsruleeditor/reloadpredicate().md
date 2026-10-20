# reloadPredicate()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Instructs the receiver to regenerate its predicate by invoking the corresponding delegate method.

**Availability**:
- macOS

## Declaration

```swift
func reloadPredicate()
```

```objc
- (void) reloadPredicate;
```

#### Discussion

You typically invoke this method because something has changed (for example, a view’s value).

## See Also

### Working with Predicates
- [var predicate: NSPredicate?](./predicate.md)
  The rule editor’s predicate.
- [func predicate(forRow: Int) -> NSPredicate?](./predicate%28forrow%29.md)
  Returns the predicate for a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/reloadpredicate())*