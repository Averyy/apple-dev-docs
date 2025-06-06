# expirationDate

**Framework**: TV Services  
**Kind**: property

The date on which the item becomes unavailable.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var expirationDate: Date? { get set }
```

#### Discussion

Specify an expiration date when the content associated with the item has a limited lifespan. For example, use it to specify the date on which a rented movie expires. The system uses this property to remove items that have expired since you last provided data.

## See Also

- [var identifier: String](tvtopshelfitem/identifier.md)
  The unique identifier for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfitem/expirationdate)*