# clearsFilterPredicateOnInsertion

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver automatically clears an existing filter predicate when new items are inserted or added to the content

**Availability**:
- macOS

## Declaration

```swift
var clearsFilterPredicateOnInsertion: Bool { get set }
```

```objc
@property BOOL clearsFilterPredicateOnInsertion;
```

## Discussion

The default is [`true`](../../Swift/true.md). This property is observable using key-value observing.

## See Also

### Filtering Content
- [var filterPredicate: NSPredicate?](./filterpredicate.md)
  A predicate used by the receiver to filter the array controller contents


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/clearsfilterpredicateoninsertion)*