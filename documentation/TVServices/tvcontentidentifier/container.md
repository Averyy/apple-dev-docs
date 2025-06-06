# container

**Framework**: TV Services  
**Kind**: property

The container that this content item is contained in.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
@NSCopying
var container: TVContentIdentifier? { get }
```

#### Discussion

Typically, this is the content identifier for the next larger grouping that this item is part of. For example, a podcast episode could be part of a larger podcast season, which could in turn be part of an entire podcast series. In this case, all three layers—episodes, seasons, and the series—would need their own unique identifiers.

The container value may be `nil`, in which case this item represents a top-level content item.

## See Also

- [var identifier: String](tvcontentidentifier/identifier.md)
  The string that identifies this content item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentidentifier/container)*