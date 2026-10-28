# eventStore

**Framework**: EventKit UI  
**Kind**: property  
**Role**: Instance Property

The event store used to save the event.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var eventStore: EKEventStore! { get set }
```

```objc
@property (nonatomic, retain, null_unspecified) EKEventStore * eventStore;
```

## Discussion

This property must be set before displaying the view.

## See Also

### Creating and Saving Events
- [var event: EKEvent?](./event.md)
  The event the user creates or edits using this view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller/eventstore)*