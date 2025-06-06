# eventViewController(_:didCompleteWith:)

**Framework**: EventKit UI  
**Kind**: method  
**Required**: Yes

Invoked when closing the event view controller.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func eventViewController(_ controller: EKEventViewController, didCompleteWith action: EKEventViewAction)
```

## Parameters

- `controller`: The event view controller to close.
- `action`: The action taken to prompt closing the event view controller. See   for a list of possible values.

## See Also

- [enum EKEventViewAction](ekeventviewaction.md)
  Describes the action taken to close the event view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventviewdelegate/eventviewcontroller(_:didcompletewith:))*