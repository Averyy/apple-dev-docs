# NSScrubberDataSource

**Framework**: AppKit  
**Kind**: protocol

A set of methods that a scrubber data source object implements to provide items to the scrubber from an associated data collection in your app.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSScrubberDataSource : NSObjectProtocol
```

## Topics

### Getting the scrubber metrics
- [func numberOfItems(for: NSScrubber) -> Int](nsscrubberdatasource/numberofitems(for:).md)
  Asks the data source for the number of items in the scrubber.
### Getting views for items
- [func scrubber(NSScrubber, viewForItemAt: Int) -> NSScrubberItemView](nsscrubberdatasource/scrubber(_:viewforitemat:).md)
  Asks the data source object for the view the corresponds to the specified item in the scrubber.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSScrubber](nsscrubber.md)
  A customizable item picker control for the Touch Bar.
- [protocol NSScrubberDelegate](nsscrubberdelegate.md)
  A set of methods that a scrubber delegate implements to respond to user interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberdatasource)*