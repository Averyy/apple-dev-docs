# Lists and Notes

**Framework**: SiriKit  
**Role**: API Collection

Create and manage notes and to-do list items.

#### Overview

> **Note**: The SiriKit domain for lists and notes provides legacy support for past operating systems releases, and doesn’t support Siri interactions in Apple Intelligence and Siri AI. To let people manage notes and to-do lists with these features, you must adopt the [App Intents](../AppIntents/AppIntents.md) framework and its app schema domains for [Notes](../AppIntents/app-schema-domain-notes.md) and [Reminders](../AppIntents/app-schema-domain-reminders.md).

With the lists and notes domain, people can create to-do lists, mark to-do list items as complete, or ask Siri to create or modify notes in their favorite note-taking app. When creating items in a to-do list, the person may also ask your app to set up a reminder based on their location or a specific date. Your intents app extension takes the information provided to it and creates the corresponding tasks, notes, and reminders either directly in your app or by communicating that information to your servers.

## Topics

### Note Creation
- [protocol INCreateNoteIntentHandling](https://developer.apple.com/documentation/intents/increatenoteintenthandling)
  The handler interface for creating notes.
- [class INCreateNoteIntent](https://developer.apple.com/documentation/intents/increatenoteintent)
  A request to create a new note.
- [class INCreateNoteIntentResponse](https://developer.apple.com/documentation/intents/increatenoteintentresponse)
  Your app’s response to a request to create a note.
### Notebook Search
- [protocol INSearchForNotebookItemsIntentHandling](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintenthandling)
  The handler interface for searching for notes, tasks, and reminders.
- [class INSearchForNotebookItemsIntent](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintent)
  A request to search for notes, tasks, and reminders.
- [class INSearchForNotebookItemsIntentResponse](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintentresponse)
  Your app’s response to a request to search for notes, tasks, or reminders.
### Task Addition
- [protocol INAddTasksIntentHandling](https://developer.apple.com/documentation/intents/inaddtasksintenthandling)
  The handler interface for adding tasks to a task list.
- [class INAddTasksIntent](https://developer.apple.com/documentation/intents/inaddtasksintent)
  A request to add tasks to an existing task list.
- [class INAddTasksIntentResponse](https://developer.apple.com/documentation/intents/inaddtasksintentresponse)
  Your response to a request to add tasks to a task list.
### Task Attributes
- [protocol INSetTaskAttributeIntentHandling](https://developer.apple.com/documentation/intents/insettaskattributeintenthandling)
  The handler interface for updating the attributes of an existing task.
- [class INSetTaskAttributeIntent](https://developer.apple.com/documentation/intents/insettaskattributeintent)
  A request to modify the attributes of a task.
- [class INSetTaskAttributeIntentResponse](https://developer.apple.com/documentation/intents/insettaskattributeintentresponse)
  Your response to a request to modify the attributes of an existing task.
### Task Deferral
- [protocol INSnoozeTasksIntentHandling](https://developer.apple.com/documentation/intents/insnoozetasksintenthandling)
  The handler interface that snoozes tasks in a task list.
- [class INSnoozeTasksIntent](https://developer.apple.com/documentation/intents/insnoozetasksintent)
  A request to snooze one or more tasks.
- [class INSnoozeTasksIntentResponse](https://developer.apple.com/documentation/intents/insnoozetasksintentresponse)
  Your response to a delete tasks request.
### Note Objects
- [class INNote](https://developer.apple.com/documentation/intents/innote)
  The content and metadata associated with a single note entry in your app.
- [class INNoteContent](https://developer.apple.com/documentation/intents/innotecontent)
  An abstract class that defines the types of content contained in notes.
- [class INTextNoteContent](https://developer.apple.com/documentation/intents/intextnotecontent)
  The textual content of a note.
- [class INImageNoteContent](https://developer.apple.com/documentation/intents/inimagenotecontent)
  An image contained in a note.
### Task Objects
- [class INTaskList](https://developer.apple.com/documentation/intents/intasklist)
  A collection of individual tasks.
- [class INTask](https://developer.apple.com/documentation/intents/intask)
  An individual task the user needs to complete.
### Event Triggers
- [class INSpatialEventTrigger](https://developer.apple.com/documentation/intents/inspatialeventtrigger)
  A trigger condition based on the user’s arrival or departure from a given location.
- [class INTemporalEventTrigger](https://developer.apple.com/documentation/intents/intemporaleventtrigger)
  A trigger condition based on a date or time.
- [class INTemporalEventTriggerTypeOptionsResolutionResult](https://developer.apple.com/documentation/intents/intemporaleventtriggertypeoptionsresolutionresult)
  A resolution result that adds a temporal event trigger.
- [struct INDayOfWeekOptions](https://developer.apple.com/documentation/intents/indayofweekoptions)
  Days of the week.
### Resolution Results
- [class INAddTasksTargetTaskListResolutionResult](https://developer.apple.com/documentation/intents/inaddtaskstargettasklistresolutionresult)
  A resolution result that adds tasks to a target task list.
- [class INAddTasksTemporalEventTriggerResolutionResult](https://developer.apple.com/documentation/intents/inaddtaskstemporaleventtriggerresolutionresult)
  A resolution result for a temporal event trigger.
- [class INDateSearchTypeResolutionResult](https://developer.apple.com/documentation/intents/indatesearchtyperesolutionresult)
  A resolution result for the types of dates supported by a search.
- [class INLocationSearchTypeResolutionResult](https://developer.apple.com/documentation/intents/inlocationsearchtyperesolutionresult)
  A resolution result for location-based searches.
- [class INNoteResolutionResult](https://developer.apple.com/documentation/intents/innoteresolutionresult)
  A resolution result for notes.
- [class INNoteContentResolutionResult](https://developer.apple.com/documentation/intents/innotecontentresolutionresult)
  A resolution result for the content of notes.
- [class INNotebookItemTypeResolutionResult](https://developer.apple.com/documentation/intents/innotebookitemtyperesolutionresult)
  A resolution result for the type of items to look for during a search of notes and tasks.
- [class INSetTaskAttributeTemporalEventTriggerResolutionResult](https://developer.apple.com/documentation/intents/insettaskattributetemporaleventtriggerresolutionresult)
  A resolution result for a temporal event trigger.
- [class INSnoozeTasksTaskResolutionResult](https://developer.apple.com/documentation/intents/insnoozetaskstaskresolutionresult)
  A resolution result for snoozing a task.
- [class INSpatialEventTriggerResolutionResult](https://developer.apple.com/documentation/intents/inspatialeventtriggerresolutionresult)
  A resolution result for the location-based trigger associated with a task.
- [class INTaskListResolutionResult](https://developer.apple.com/documentation/intents/intasklistresolutionresult)
  A resolution result for a list of tasks.
- [class INTaskResolutionResult](https://developer.apple.com/documentation/intents/intaskresolutionresult)
  A resolution result for a single task within a task list.
- [class INTaskStatusResolutionResult](https://developer.apple.com/documentation/intents/intaskstatusresolutionresult)
  A resolution result for the status of a task.
- [class INTemporalEventTriggerResolutionResult](https://developer.apple.com/documentation/intents/intemporaleventtriggerresolutionresult)
  A resolution result for the time-based trigger associated with a task.
- [class INTaskPriorityResolutionResult](https://developer.apple.com/documentation/intents/intaskpriorityresolutionresult)
  A resolution result for the priority associated with a task.

## See Also

### Standard Intents
- [Car Commands](./car-commands.md)
  Manage vehicle door locks and get the vehicle’s status.
- [Media](./media.md)
  Listen and control audio through Siri Intents, or listen and watch media content from your app with shortcuts.
- [Messaging](./messaging.md)
  Send messages and search the user’s received messages.
- [Payments](./payments.md)
  Send payments between users or pay bills.
- [Restaurant Reservations](./restaurant-reservations.md)
  Create and manage restaurant reservations with help from the Maps app.
- [Ride Booking](./ride-booking.md)
  Book rides and report their status.
- [VoIP Calling](./voip-calling.md)
  Initiate calls and search the user’s call history.
- [Workouts](./workouts.md)
  Start, end, and manage fitness routines.
- [Intent Class Identifiers](./intent-class-identifiers.md)
  Identify intents that user notifications specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/lists-and-notes)*