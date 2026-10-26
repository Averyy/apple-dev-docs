# Lists and Notes

**Framework**: SiriKit  
**Role**: API Collection

Create and manage notes and to-do list items.

#### Overview

> **Note**: The SiriKit domain for lists and notes provides legacy support for past operating systems releases, and doesn’t support Siri interactions in Apple Intelligence and Siri AI. To let people manage notes and to-do lists with these features, you must adopt the [App Intents](../AppIntents/AppIntents.md) framework and its app schema domains for [Notes](../AppIntents/app-schema-domain-notes.md) and [Reminders](../AppIntents/app-schema-domain-reminders.md).

With the lists and notes domain, people can create to-do lists, mark to-do list items as complete, or ask Siri to create or modify notes in their favorite note-taking app. When creating items in a to-do list, the person may also ask your app to set up a reminder based on their location or a specific date. Your intents app extension takes the information provided to it and creates the corresponding tasks, notes, and reminders either directly in your app or by communicating that information to your servers.

## Topics

### Note Creation
- [protocol INCreateNoteIntentHandling](../Intents/increatenoteintenthandling.md)
  The handler interface for creating notes.
- [class INCreateNoteIntent](../Intents/increatenoteintent.md)
  A request to create a new note.
- [class INCreateNoteIntentResponse](../Intents/increatenoteintentresponse.md)
  Your app’s response to a request to create a note.
### Notebook Search
- [protocol INSearchForNotebookItemsIntentHandling](../Intents/insearchfornotebookitemsintenthandling.md)
  The handler interface for searching for notes, tasks, and reminders.
- [class INSearchForNotebookItemsIntent](../Intents/insearchfornotebookitemsintent.md)
  A request to search for notes, tasks, and reminders.
- [class INSearchForNotebookItemsIntentResponse](../Intents/insearchfornotebookitemsintentresponse.md)
  Your app’s response to a request to search for notes, tasks, or reminders.
### Task Addition
- [protocol INAddTasksIntentHandling](../Intents/inaddtasksintenthandling.md)
  The handler interface for adding tasks to a task list.
- [class INAddTasksIntent](../Intents/inaddtasksintent.md)
  A request to add tasks to an existing task list.
- [class INAddTasksIntentResponse](../Intents/inaddtasksintentresponse.md)
  Your response to a request to add tasks to a task list.
### Task Attributes
- [protocol INSetTaskAttributeIntentHandling](../Intents/insettaskattributeintenthandling.md)
  The handler interface for updating the attributes of an existing task.
- [class INSetTaskAttributeIntent](../Intents/insettaskattributeintent.md)
  A request to modify the attributes of a task.
- [class INSetTaskAttributeIntentResponse](../Intents/insettaskattributeintentresponse.md)
  Your response to a request to modify the attributes of an existing task.
### Task Deferral
- [protocol INSnoozeTasksIntentHandling](../Intents/insnoozetasksintenthandling.md)
  The handler interface that snoozes tasks in a task list.
- [class INSnoozeTasksIntent](../Intents/insnoozetasksintent.md)
  A request to snooze one or more tasks.
- [class INSnoozeTasksIntentResponse](../Intents/insnoozetasksintentresponse.md)
  Your response to a delete tasks request.
### Note Objects
- [class INNote](../Intents/innote.md)
  The content and metadata associated with a single note entry in your app.
- [class INNoteContent](../Intents/innotecontent.md)
  An abstract class that defines the types of content contained in notes.
- [class INTextNoteContent](../Intents/intextnotecontent.md)
  The textual content of a note.
- [class INImageNoteContent](../Intents/inimagenotecontent.md)
  An image contained in a note.
### Task Objects
- [class INTaskList](../Intents/intasklist.md)
  A collection of individual tasks.
- [class INTask](../Intents/intask.md)
  An individual task the user needs to complete.
### Event Triggers
- [class INSpatialEventTrigger](../Intents/inspatialeventtrigger.md)
  A trigger condition based on the user’s arrival or departure from a given location.
- [class INTemporalEventTrigger](../Intents/intemporaleventtrigger.md)
  A trigger condition based on a date or time.
- [class INTemporalEventTriggerTypeOptionsResolutionResult](../Intents/intemporaleventtriggertypeoptionsresolutionresult.md)
  A resolution result that adds a temporal event trigger.
- [struct INDayOfWeekOptions](../Intents/indayofweekoptions.md)
  Days of the week.
### Resolution Results
- [class INAddTasksTargetTaskListResolutionResult](../Intents/inaddtaskstargettasklistresolutionresult.md)
  A resolution result that adds tasks to a target task list.
- [class INAddTasksTemporalEventTriggerResolutionResult](../Intents/inaddtaskstemporaleventtriggerresolutionresult.md)
  A resolution result for a temporal event trigger.
- [class INDateSearchTypeResolutionResult](../Intents/indatesearchtyperesolutionresult.md)
  A resolution result for the types of dates supported by a search.
- [class INLocationSearchTypeResolutionResult](../Intents/inlocationsearchtyperesolutionresult.md)
  A resolution result for location-based searches.
- [class INNoteResolutionResult](../Intents/innoteresolutionresult.md)
  A resolution result for notes.
- [class INNoteContentResolutionResult](../Intents/innotecontentresolutionresult.md)
  A resolution result for the content of notes.
- [class INNotebookItemTypeResolutionResult](../Intents/innotebookitemtyperesolutionresult.md)
  A resolution result for the type of items to look for during a search of notes and tasks.
- [class INSetTaskAttributeTemporalEventTriggerResolutionResult](../Intents/insettaskattributetemporaleventtriggerresolutionresult.md)
  A resolution result for a temporal event trigger.
- [class INSnoozeTasksTaskResolutionResult](../Intents/insnoozetaskstaskresolutionresult.md)
  A resolution result for snoozing a task.
- [class INSpatialEventTriggerResolutionResult](../Intents/inspatialeventtriggerresolutionresult.md)
  A resolution result for the location-based trigger associated with a task.
- [class INTaskListResolutionResult](../Intents/intasklistresolutionresult.md)
  A resolution result for a list of tasks.
- [class INTaskResolutionResult](../Intents/intaskresolutionresult.md)
  A resolution result for a single task within a task list.
- [class INTaskStatusResolutionResult](../Intents/intaskstatusresolutionresult.md)
  A resolution result for the status of a task.
- [class INTemporalEventTriggerResolutionResult](../Intents/intemporaleventtriggerresolutionresult.md)
  A resolution result for the time-based trigger associated with a task.
- [class INTaskPriorityResolutionResult](../Intents/intaskpriorityresolutionresult.md)
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