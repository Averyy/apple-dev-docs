# predicate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The rule editor’s predicate.

**Availability**:
- macOS

## Declaration

```swift
var predicate: NSPredicate? { get }
```

```objc
@property (strong, readonly, nullable) NSPredicate * predicate;
```

## Discussion

If the delegate implements [`NSRuleEditor`](../nsruleeditor.md), this property contains the rule editor’s predicate. If the delegate does not implement [`NSRuleEditor`](../nsruleeditor.md), or if the delegate does not return enough parts to construct a full predicate, this property contains `nil`.

## See Also

### Working with Predicates
- [func reloadPredicate()](./reloadpredicate%28%29.md)
  Instructs the receiver to regenerate its predicate by invoking the corresponding delegate method.
- [func predicate(forRow: Int) -> NSPredicate?](./predicate%28forrow%29.md)
  Returns the predicate for a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/predicate)*