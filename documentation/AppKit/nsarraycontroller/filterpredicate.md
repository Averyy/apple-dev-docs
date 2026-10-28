# filterPredicate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A predicate used by the receiver to filter the array controller contents

**Availability**:
- macOS

## Declaration

```swift
var filterPredicate: NSPredicate? { get set }
```

```objc
@property (strong, nullable) NSPredicate * filterPredicate;
```

## Discussion

This property is observable using key-value observing.

## See Also

### Filtering Content
- [var clearsFilterPredicateOnInsertion: Bool](./clearsfilterpredicateoninsertion.md)
  A Boolean value that indicates whether the receiver automatically clears an existing filter predicate when new items are inserted or added to the content


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/filterpredicate)*