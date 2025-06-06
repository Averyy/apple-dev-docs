# cancelEditing()

**Framework**: EventKit UI  
**Kind**: method

Ends the editing session and discards any changes that were made to the event.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func cancelEditing()
```

#### Discussion

This method is the programmatic equivalent of the user tapping Cancel. The delegate won’t receive the [`eventEditViewController(_:didCompleteWith:)`](ekeventeditviewdelegate/eventeditviewcontroller(_:didcompletewith:).md) message, so you must dismiss the controller after calling this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller/cancelediting())*