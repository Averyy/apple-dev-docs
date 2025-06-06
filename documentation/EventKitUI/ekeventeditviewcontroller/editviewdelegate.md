# editViewDelegate

**Framework**: EventKit UI  
**Kind**: property

The delegate to notify when editing an event.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var editViewDelegate: (any EKEventEditViewDelegate)? { get set }
```

## See Also

- [protocol EKEventEditViewDelegate](ekeventeditviewdelegate.md)
  A notification sent to the delegate when the user finishes editing an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller/editviewdelegate)*