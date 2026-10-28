# INNotebookDomainHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface for adopting all of the protocols in the lists and notes domain.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 6.0

> **Deprecated**: Please conform to INCreateNoteIntentHandling, INAppendToNoteIntentHandling, INAddTasksIntentHandling, INCreateTaskListIntentHandling, INSetTaskAttributeIntentHandling and INSearchForNotebookItemsIntentHandling instead

## Declaration

```swift
protocol INNotebookDomainHandling : INAddTasksIntentHandling, INAppendToNoteIntentHandling, INCreateNoteIntentHandling, INCreateTaskListIntentHandling, INSearchForNotebookItemsIntentHandling, INSetTaskAttributeIntentHandling
```

```objc
@protocol INNotebookDomainHandling <INCreateNoteIntentHandling, INAppendToNoteIntentHandling, INAddTasksIntentHandling, INCreateTaskListIntentHandling, INSetTaskAttributeIntentHandling, INSearchForNotebookItemsIntentHandling>
```

## Overview

The [`INNotebookDomainHandling`](./innotebookdomainhandling.md) protocol is a convenience protocol that adopts all of the protocols used to handle list, note, and reminder-related intents. When your app adopts all of the protocols associated with notes and reminders, you can adopt this one protocol instead of adopting the [`INCreateNoteIntentHandling`](./increatenoteintenthandling.md), [`INAppendToNoteIntentHandling`](./inappendtonoteintenthandling.md), [`INSearchForNotebookItemsIntentHandling`](./insearchfornotebookitemsintenthandling.md), [`INCreateTaskListIntentHandling`](./increatetasklistintenthandling.md), [`INAddTasksIntentHandling`](./inaddtasksintenthandling.md), and [`INSetTaskAttributeIntentHandling`](./insettaskattributeintenthandling.md) protocols separately.

An object that adopts this protocol must be able to respond to the following intents:

- [`INCreateNoteIntent`](./increatenoteintent.md), a request to create a new note.
- [`INAppendToNoteIntent`](./inappendtonoteintent.md), a request to modify an existing note.
- [`INSearchForNotebookItemsIntent`](./insearchfornotebookitemsintent.md), a request to search for existing notes.
- [`INCreateTaskListIntent`](./increatetasklistintent.md), a request to create a new list of tasks or reminders.
- [`INAddTasksIntent`](./inaddtasksintent.md), a request to add tasks to an existing task list.
- [`INSetTaskAttributeIntent`](./insettaskattributeintent.md), a request to modify a task.

Your handler object must be prepared to resolve any parameters associated with these intents and to confirm and handle the requests. When confirming and handling a request, you provide the response object that matches the specified intent.

## Relationships

### Inherits From
- [INAddTasksIntentHandling](./inaddtasksintenthandling.md)
- [INAppendToNoteIntentHandling](./inappendtonoteintenthandling.md)
- [INCreateNoteIntentHandling](./increatenoteintenthandling.md)
- [INCreateTaskListIntentHandling](./increatetasklistintenthandling.md)
- [INSearchForNotebookItemsIntentHandling](./insearchfornotebookitemsintenthandling.md)
- [INSetTaskAttributeIntentHandling](./insettaskattributeintenthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Domain-Handling Protocols
- [protocol INMessagesDomainHandling](./inmessagesdomainhandling.md)
  An interface for adopting all of the protocols in the messages domain.
- [protocol INWorkoutsDomainHandling](./inworkoutsdomainhandling.md)
  An interface for adopting all of the protocols in the workouts domain.
- [protocol INPaymentsDomainHandling](./inpaymentsdomainhandling.md)
  An interface for adopting all of the protocols in the payments domain.
- [protocol INCallsDomainHandling](./incallsdomainhandling.md)
  Provides a convenient way to adopt all of the protocols in the VoIP calling domain.
- [protocol INVisualCodeDomainHandling](./invisualcodedomainhandling.md)
  An interface for adopting all of the protocols in the visual codes domain.
- [protocol INPhotosDomainHandling](./inphotosdomainhandling.md)
  An interface for adopting all of the protocols in the photos domain.
- [protocol INRidesharingDomainHandling](./inridesharingdomainhandling.md)
  An interface for adopting all of the protocols in the ride-booking domain.
- [protocol INCarCommandsDomainHandling](./incarcommandsdomainhandling.md)
  An interface for adopting all the handling protocols in the car commands domain.
- [protocol INCarPlayDomainHandling](./incarplaydomainhandling.md)
  An interface for adopting all of the protocols in the CarPlay domain.
- [protocol INRadioDomainHandling](./inradiodomainhandling.md)
  An interface for adopting all of the protocols in the radio domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innotebookdomainhandling)*