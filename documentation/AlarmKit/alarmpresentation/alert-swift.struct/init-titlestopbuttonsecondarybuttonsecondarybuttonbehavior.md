# init(title:stopButton:secondaryButton:secondaryButtonBehavior:)

**Framework**: AlarmKit  
**Kind**: init

Creates an alert for an alarm.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
init(title: LocalizedStringResource, stopButton: AlarmButton, secondaryButton: AlarmButton? = nil, secondaryButtonBehavior: AlarmPresentation.Alert.SecondaryButtonBehavior? = nil)
```

## Parameters

- `title`: The title of the alert.
- `stopButton`: The end button for an alarm.
- `secondaryButton`: The customizable second button for an alarm.
- `secondaryButtonBehavior`: The defined behavior of the secondary button.

## See Also

- [var stopButton: AlarmButton](alarmpresentation/alert-swift.struct/stopbutton.md)
  The appearance of the stop button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentation/alert-swift.struct/init(title:stopbutton:secondarybutton:secondarybuttonbehavior:))*