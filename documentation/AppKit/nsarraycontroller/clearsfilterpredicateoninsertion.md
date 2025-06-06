# clearsFilterPredicateOnInsertion

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the receiver automatically clears an existing filter predicate when new items are inserted or added to the content

**Availability**:
- macOS ?+

## Declaration

```swift
var clearsFilterPredicateOnInsertion: Bool { get set }
```

#### Discussion

The default is [`true`](https://developer.apple.com/documentation/swift/true). This property is observable using key-value observing.

## See Also

- [var filterPredicate: NSPredicate?](nsarraycontroller/filterpredicate.md)
  A predicate used by the receiver to filter the array controller contents


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/clearsfilterpredicateoninsertion)*