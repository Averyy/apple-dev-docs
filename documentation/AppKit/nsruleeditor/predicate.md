# predicate

**Framework**: AppKit  
**Kind**: property

The rule editor’s predicate.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var predicate: NSPredicate? { get }
```

#### Discussion

If the delegate implements [`NSRuleEditor`](nsruleeditor.md), this property contains the rule editor’s predicate. If the delegate does not implement [`NSRuleEditor`](nsruleeditor.md), or if the delegate does not return enough parts to construct a full predicate, this property contains `nil`.

## See Also

- [func reloadPredicate()](nsruleeditor/reloadpredicate.md)
  Instructs the receiver to regenerate its predicate by invoking the corresponding delegate method.
- [func predicate(forRow: Int) -> NSPredicate?](nsruleeditor/predicate(forrow:).md)
  Returns the predicate for a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/predicate)*