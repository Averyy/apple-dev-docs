# EKEventViewDelegate

**Framework**: EventKit UI  
**Kind**: protocol  
**Role**: Protocol

Delegates used to display details for calendar events.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol EKEventViewDelegate : NSObjectProtocol
```

```objc
@protocol EKEventViewDelegate <NSObject>
```

#### Overview

Delegates of an [`EKEventViewController`](./ekeventviewcontroller.md) object conform to this protocol. Notifies the event view controller’s delegate when closing the event view controller. It is your responsibility to close the event view controller and perform any additional tasks within this protocol’s method.

## Topics

### Responding to the Interface’s Dismissal
- [enum EKEventViewAction](./ekeventviewaction.md)
  Describes the action taken to close the event view controller.
- [func eventViewController(EKEventViewController, didCompleteWith: EKEventViewAction)](./ekeventviewdelegate/eventviewcontroller%28_,didcompletewith%29.md)
  Invoked when closing the event view controller.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Dismissing the Event Interface
- [var delegate: (any EKEventViewDelegate)?](./ekeventviewcontroller/delegate.md)
  The event view controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventviewdelegate)*