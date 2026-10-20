# delegate

**Framework**: Notification Center  
**Kind**: property  
**Role**: Instance Property

The search view controller’s delegate or `nil` if the receiver doesn’t have a delegate.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
@IBOutlet
weak var delegate: (any NCWidgetSearchViewDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NCWidgetSearchViewDelegate> delegate;
```

#### Discussion

A search view controller’s delegate performs a search on the input term and updates the controller’s [`searchResults`](./searchresults.md) property with the results.

## See Also

### Enabling Search
- [protocol NCWidgetSearchViewDelegate](../ncwidgetsearchviewdelegate.md)
  The interface for enabling user searches in the search view controller of a macOS Today widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller/delegate)*