# EKEventEditViewDelegate

**Framework**: EventKit UI  
**Kind**: protocol  
**Role**: Protocol

A notification sent to the delegate when the user finishes editing an event.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol EKEventEditViewDelegate : NSObjectProtocol
```

```objc
@protocol EKEventEditViewDelegate <NSObject>
```

## Overview

Delegates of an [`EKEventEditViewController`](./ekeventeditviewcontroller.md) object conform to this protocol. Use `EKEventEditViewController` to allow the user to either create an event or edit an existing event. To be notified when the user finishes editing the event, set the delegate to an object conforming to this protocol.

## Topics

### Getting the Default Calendar
- [func eventEditViewControllerDefaultCalendar(forNewEvents: EKEventEditViewController) -> EKCalendar](./ekeventeditviewdelegate/eventeditviewcontrollerdefaultcalendar%28fornewevents%29.md)
  The default calendar to use when creating new events.
### Finishing an Edit
- [func eventEditViewController(EKEventEditViewController, didCompleteWith: EKEventEditViewAction)](./ekeventeditviewdelegate/eventeditviewcontroller%28_,didcompletewith%29.md)
  Invoked when the user finishes editing an event.
- [enum EKEventEditViewAction](./ekeventeditviewaction.md)
  The action taken by the user after editing an event.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Managing the Event Editing Interface
- [var editViewDelegate: (any EKEventEditViewDelegate)?](./ekeventeditviewcontroller/editviewdelegate.md)
  The delegate to notify when editing an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventeditviewdelegate)*