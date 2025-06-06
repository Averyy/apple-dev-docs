# delegate

**Framework**: Notification Center  
**Kind**: property

The search view controller’s delegate or `nil` if the receiver doesn’t have a delegate.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@IBOutlet
@MainActor weak var delegate: (any NCWidgetSearchViewDelegate)? { get set }
```

#### Discussion

A search view controller’s delegate performs a search on the input term and updates the controller’s [`searchResults`](ncwidgetsearchviewcontroller/searchresults.md) property with the results.

## See Also

- [protocol NCWidgetSearchViewDelegate](ncwidgetsearchviewdelegate.md)
  The interface for enabling user searches in the search view controller of a macOS Today widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller/delegate)*