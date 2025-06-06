# reloadPredicate()

**Framework**: AppKit  
**Kind**: method

Instructs the receiver to regenerate its predicate by invoking the corresponding delegate method.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func reloadPredicate()
```

#### Discussion

You typically invoke this method because something has changed (for example, a view’s value).

## See Also

- [var predicate: NSPredicate?](nsruleeditor/predicate.md)
  The rule editor’s predicate.
- [func predicate(forRow: Int) -> NSPredicate?](nsruleeditor/predicate(forrow:).md)
  Returns the predicate for a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/reloadpredicate())*