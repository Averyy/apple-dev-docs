# personViewController(_:shouldPerformDefaultActionForPerson:property:identifier:)

**Framework**: Address Book UI  
**Kind**: method  
**Required**: Yes

Sent when the user selects a property value of the person displayed in a person view controller.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func personViewController(_ personViewController: ABPersonViewController, shouldPerformDefaultActionForPerson person: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `personViewController` should perform its default action. Your application may quit as a result of this action. [`false`](https://developer.apple.com/documentation/swift/false): if `personViewController` should do nothing. The delegate may perform custom action processing.

## Parameters

- `personViewController`: The sender.
- `person`: The person   is displaying.
- `property`: The property whose value the user selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontrollerdelegate/personviewcontroller(_:shouldperformdefaultactionforperson:property:identifier:))*