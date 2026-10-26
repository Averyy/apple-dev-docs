# init(title:content:itemType:status:location:locationSearchType:dateTime:dateSearchType:notebookItemIdentifier:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with the specified search parameters.

**Availability**:
- iOS 11.2+ - Deprecated in 13.0
- iPadOS 11.2+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.2+ - Deprecated in 6.0

> **Deprecated**: Use the designated initializer instead

## Declaration

```swift
convenience init(title: INSpeakableString?, content: String?, itemType: INNotebookItemType, status: INTaskStatus, location: CLPlacemark?, locationSearchType: INLocationSearchType, dateTime: INDateComponentsRange?, dateSearchType: INDateSearchType, notebookItemIdentifier: String?)
```

```objc
- (instancetype) initWithTitle:(INSpeakableString *) title content:(NSString *) content itemType:(INNotebookItemType) itemType status:(INTaskStatus) status location:(CLPlacemark *) location locationSearchType:(INLocationSearchType) locationSearchType dateTime:(INDateComponentsRange *) dateTime dateSearchType:(INDateSearchType) dateSearchType notebookItemIdentifier:(NSString *) notebookItemIdentifier;
```

#### Return Value

An initialized intent object or `nil` if the object could not be created.

#### Discussion

Normally, you do not create instances of this class yourself. Instead, SiriKit creates instances when the user asks to search for notes, task lists, tasks, or reminders. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths. When doing so, specify only the search parameters that you want to include and provide `nil` or unknown values for other parameters.

## Parameters

- `title`: The text to search for in the title of the note, task, or task list.
- `content`: The text to search for in the content of a note.
- `itemType`: The type of items to search. Use this parameter to restrict your search to items of the specified type.
- `status`: The completion status of the task. Use this parameter to restrict your search to tasks whose status matches the specified value.
- `location`: The location value to use during your search. When the `locationSearchType` parameter is [`INLocationSearchType.byLocationTrigger`](../inlocationsearchtype/bylocationtrigger.md), use this parameter to restrict your search to reminders that are triggered near the specified location.
- `locationSearchType`: The type of location search to perform. Use this parameter to specify when a search for location-based reminders should occur.
- `dateTime`: The time value to use during your search. Use the value of the `dateSearchType` parameter to determine how to apply the value of this parameter.
- `dateSearchType`: The type of date-based search to perform. Use this parameter to specify when to search for notes with the specified creation or modification date or when to search for reminders based on the date on which they are delivered.
- `notebookItemIdentifier`: The unique string that your app uses to identify the notebook item.

## See Also

### Initializing the Intent Object
- [init(title: INSpeakableString?, content: String?, itemType: INNotebookItemType, status: INTaskStatus, location: CLPlacemark?, locationSearchType: INLocationSearchType, dateTime: INDateComponentsRange?, dateSearchType: INDateSearchType, temporalEventTriggerTypes: INTemporalEventTriggerTypeOptions, taskPriority: INTaskPriority, notebookItemIdentifier: String?)](./init%28title,content,itemtype,status,location,locationsearchtype,datetime,datesearchtype,temporaleventtriggertypes,taskpriority,notebookitemidentifier%29.md)
- [convenience init(title: INSpeakableString?, content: String?, itemType: INNotebookItemType, status: INTaskStatus, location: CLPlacemark?, locationSearchType: INLocationSearchType, dateTime: INDateComponentsRange?, dateSearchType: INDateSearchType)](./init%28title,content,itemtype,status,location,locationsearchtype,datetime,datesearchtype%29.md)
  Initializes the intent object with the specified search parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintent/init(title:content:itemtype:status:location:locationsearchtype:datetime:datesearchtype:notebookitemidentifier:))*