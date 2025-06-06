# delegate

**Framework**: EventKit UI  
**Kind**: property

The calendar chooser’s delegate.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any EKCalendarChooserDelegate)? { get set }
```

#### Discussion

This object should conform to [`EKCalendarChooserDelegate`](ekcalendarchooserdelegate.md).

## See Also

- [protocol EKCalendarChooserDelegate](ekcalendarchooserdelegate.md)
  Methods a calendar chooser’s delegate may use to receive notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser/delegate)*