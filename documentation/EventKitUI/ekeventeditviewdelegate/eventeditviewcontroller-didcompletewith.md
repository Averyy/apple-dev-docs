# eventEditViewController(_:didCompleteWith:)

**Framework**: EventKit UI  
**Kind**: method  
**Required**: Yes

Invoked when the user finishes editing an event.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func eventEditViewController(_ controller: EKEventEditViewController, didCompleteWith action: EKEventEditViewAction)
```

#### Discussion

Implement this method to dismiss the modal event edit view controller.

## Parameters

- `controller`: The edit view controller presenting the event.
- `action`: The action the user took to end editing.

## See Also

- [enum EKEventEditViewAction](ekeventeditviewaction.md)
  The action taken by the user after editing an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventeditviewdelegate/eventeditviewcontroller(_:didcompletewith:))*