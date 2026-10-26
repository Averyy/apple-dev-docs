# init(title:content:itemType:status:location:locationSearchType:dateTime:dateSearchType:temporalEventTriggerTypes:taskPriority:notebookItemIdentifier:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
init(title: INSpeakableString?, content: String?, itemType: INNotebookItemType, status: INTaskStatus, location: CLPlacemark?, locationSearchType: INLocationSearchType, dateTime: INDateComponentsRange?, dateSearchType: INDateSearchType, temporalEventTriggerTypes: INTemporalEventTriggerTypeOptions = [], taskPriority: INTaskPriority, notebookItemIdentifier: String?)
```

```objc
- (instancetype) initWithTitle:(INSpeakableString *) title content:(NSString *) content itemType:(INNotebookItemType) itemType status:(INTaskStatus) status location:(CLPlacemark *) location locationSearchType:(INLocationSearchType) locationSearchType dateTime:(INDateComponentsRange *) dateTime dateSearchType:(INDateSearchType) dateSearchType temporalEventTriggerTypes:(INTemporalEventTriggerTypeOptions) temporalEventTriggerTypes taskPriority:(INTaskPriority) taskPriority notebookItemIdentifier:(NSString *) notebookItemIdentifier;
```

## See Also

### Initializing the Intent Object
- [convenience init(title: INSpeakableString?, content: String?, itemType: INNotebookItemType, status: INTaskStatus, location: CLPlacemark?, locationSearchType: INLocationSearchType, dateTime: INDateComponentsRange?, dateSearchType: INDateSearchType, notebookItemIdentifier: String?)](./init%28title,content,itemtype,status,location,locationsearchtype,datetime,datesearchtype,notebookitemidentifier%29.md)
  Initializes the intent object with the specified search parameters.
- [convenience init(title: INSpeakableString?, content: String?, itemType: INNotebookItemType, status: INTaskStatus, location: CLPlacemark?, locationSearchType: INLocationSearchType, dateTime: INDateComponentsRange?, dateSearchType: INDateSearchType)](./init%28title,content,itemtype,status,location,locationsearchtype,datetime,datesearchtype%29.md)
  Initializes the intent object with the specified search parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintent/init(title:content:itemtype:status:location:locationsearchtype:datetime:datesearchtype:temporaleventtriggertypes:taskpriority:notebookitemidentifier:))*