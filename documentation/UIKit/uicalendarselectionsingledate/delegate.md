# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A delegate object that a calendar view asks about selectable dates and informs of changes to the selection of a single date.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UICalendarSelectionSingleDateDelegate)? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) id<UICalendarSelectionSingleDateDelegate> delegate;
```

## See Also

### Setting the selection delegate
- [protocol UICalendarSelectionSingleDateDelegate](../uicalendarselectionsingledatedelegate.md)
  A set of methods you implement to provide selectable dates and handle changes to the selection of a single date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionsingledate/delegate)*