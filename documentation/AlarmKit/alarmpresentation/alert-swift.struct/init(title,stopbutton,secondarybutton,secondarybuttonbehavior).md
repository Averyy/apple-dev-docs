# init(title:stopButton:secondaryButton:secondaryButtonBehavior:)

**Framework**: AlarmKit  
**Kind**: init  
**Role**: Initializer

Creates an alert for an alarm.

**Availability**:
- iOS 26.0+ - Deprecated in 26.1
- iPadOS 26.0+ - Deprecated in 26.1
- Mac Catalyst 26.0+ - Deprecated in 26.1

> **Deprecated**: stopButton is deprecated and will no longer be used

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

### Deprecated
- [var stopButton: AlarmButton](./stopbutton.md)
  The appearance of the stop button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentation/alert-swift.struct/init(title:stopbutton:secondarybutton:secondarybuttonbehavior:))*