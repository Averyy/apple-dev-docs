# isRefreshing

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether a refresh operation has been triggered and is in progress.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var isRefreshing: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isRefreshing) BOOL refreshing;
```

## See Also

### Managing the refresh status
- [func beginRefreshing()](./beginrefreshing%28%29.md)
  Tells the control that a refresh operation was started programmatically.
- [func endRefreshing()](./endrefreshing%28%29.md)
  Tells the control that a refresh operation has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uirefreshcontrol/isrefreshing)*