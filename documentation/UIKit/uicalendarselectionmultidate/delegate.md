# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A delegate object that a calendar view asks for selectable dates and informs of changes to the selection of multiple dates.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UICalendarSelectionMultiDateDelegate)? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) id<UICalendarSelectionMultiDateDelegate> delegate;
```

## See Also

### Setting the selection delegate
- [protocol UICalendarSelectionMultiDateDelegate](../uicalendarselectionmultidatedelegate.md)
  A set of methods you implement to provide selectable dates and handle changes to the selection of multiple dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionmultidate/delegate)*