# INSearchForNotebookItemsIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to search for notes, tasks, and reminders.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class INSearchForNotebookItemsIntent
```

```objc
@interface INSearchForNotebookItemsIntent : INIntent
```

## Overview

Siri creates an [`INSearchForNotebookItemsIntent`](./insearchfornotebookitemsintent.md) object when the user asks to search for existing notes, tasks, and reminders. The intent object contains search parameters such as the type of items to return, strings to match against the title or content, the completion status of tasks, or the trigger conditions used to generate reminders.

To handle this intent, the handler object in your Intents extension must adopt the [`INSearchForNotebookItemsIntentHandling`](./insearchfornotebookitemsintenthandling.md) protocol. Your handler should confirm the request and create an [`INSearchForNotebookItemsIntentResponse`](./insearchfornotebookitemsintentresponse.md) object with the search results.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents |
| Always requires unlocked device | Yes |

### Example Phrases

Users can ask Siri to search for notebook items in a variety of ways. The table below provides a few sample phrases in different languages. You can use these phrases during testing to trigger your intents. This list isn’t exhaustive and Siri may recognize many other phrases.

| Locale | Example 1 | Example 2 |
| --- | --- | --- |
| en | Show me all my notes on `<appName>` | Show me what I created last week on `<appName>` |
| zh_CN | 显示我所有的便笺(在`<appName>` 上) | 显示我上个星期所有新建立的(在 appName> 上) |
| zh_HK | 顯示(`<appName>` 入面)所有嘅備忘錄 | 顯示我上星期(喺 `<appName>`)建立嘅項目 |
| zh_TW | 顯示我所有的備忘錄(在 `<appName>` 上) | 顯示我上週在 `<appName>` 上建立的東西 |
| yue_CN | 显示(`<appName>` 入面)所有嘅备忘录 | 显示我上星期(喺 `<appName>`)建立嘅项目 |
| ar | اعرض جميع ملاحظاتي على `<appName>` | اعرض ما تم إنشاؤه الأسبوع الماضي على  `<appName>` |
| da | vis mig alle mine noter i `<appName>` | vis mig hvad blev oprettet i `<appName>` sidste uge i |
| de | Zeige mir alle meine Notizen auf `<appName>` | Zeig mir die Notizen die ich letzte Woche in `<appName>` erstellt habe |
| es | Enséñame todas mis notas en `<appName>` | Muéstrame lo que creé en `<appName>` la semana pasada |
| fi | Näytä kaikki muistutukset apissa `<appName>` | Näytä viime viikolla apissa `<appName>` luomani muistutukset |
| fr | Montre-moi toutes mes notes sur `<appName>` | Montre-moi ce que j’ai créé la semaine dernière sur `<appName>` |
| he | תראי לי את כל הפתקים ב`<appName>` | תראי מה יצרתי שבוע שעבר ב`<appName>` |
| it | Mostrami tutte le mie note su `<appName>` | Mostrami cosa ho creato la scorsa settimana su `<appName>` |
| ja | `<appName>` のメモを全部見せて | `<appName>`  で先週作ったメモを全部見せて |
| ko | `<appName>` 에 있는 모든 노트 보여줘 | `<appName>`  에서 지난 주에 만든 것 보여줘 |
| ms | Tunjukkan semua nota saya pada `<appName>` | Tunjukkan item yang diciptakan minggu lepas pada `<appName>` |
| nb | Vis alle notatene mine i `<appName>` | Vis det jeg laget i forrige uke på `<appName>` |
| nl | Toon me alle notities in `<appName>` | Toon wat ik vorige week aangemaakt heb op `<appName>` |
| pt | Mostrar todas as minhas notas no `<appName>` | Mostre o que eu criei na semana passada no `<appName>` |
| ru | Покажи все мои заметки в `<appName>` | Покажи мне что я создал на прошлой неделе в `<appName>` |
| sv | Visa mig alla mina anteckningar i `<appName>` | Visa mig vad jag skapade förra veckan i `<appName>` |
| th | แสดงโน้ตทั้งหมดบนแอพ `<appName>` | แสดงสิ่งที่ฉันสร้างอาทิตย์ที่แล้วในแอพ `<appName>` |
| tr | `<appName>` ’deki tüm notlarımı göster | `<appName>` ’de geçen hafta oluşturduğum notları göster |

In the preceding examples, `<appName>` represents the name of the app whose Intents extension handles the request.

## Topics

### Initializing the Intent Object
- [init(title: INSpeakableString?, content: String?, itemType: INNotebookItemType, status: INTaskStatus, location: CLPlacemark?, locationSearchType: INLocationSearchType, dateTime: INDateComponentsRange?, dateSearchType: INDateSearchType, temporalEventTriggerTypes: INTemporalEventTriggerTypeOptions, taskPriority: INTaskPriority, notebookItemIdentifier: String?)](./insearchfornotebookitemsintent/init%28title,content,itemtype,status,location,locationsearchtype,datetime,datesearchtype,temporaleventtriggertypes,taskpriority,notebookitemidentifier%29.md)
- [convenience init(title: INSpeakableString?, content: String?, itemType: INNotebookItemType, status: INTaskStatus, location: CLPlacemark?, locationSearchType: INLocationSearchType, dateTime: INDateComponentsRange?, dateSearchType: INDateSearchType, notebookItemIdentifier: String?)](./insearchfornotebookitemsintent/init%28title,content,itemtype,status,location,locationsearchtype,datetime,datesearchtype,notebookitemidentifier%29.md)
  Initializes the intent object with the specified search parameters.
- [convenience init(title: INSpeakableString?, content: String?, itemType: INNotebookItemType, status: INTaskStatus, location: CLPlacemark?, locationSearchType: INLocationSearchType, dateTime: INDateComponentsRange?, dateSearchType: INDateSearchType)](./insearchfornotebookitemsintent/init%28title,content,itemtype,status,location,locationsearchtype,datetime,datesearchtype%29.md)
  Initializes the intent object with the specified search parameters.
### Searching by Type
- [var itemType: INNotebookItemType](./insearchfornotebookitemsintent/itemtype.md)
  The type of items to include in your search.
- [enum INNotebookItemType](./innotebookitemtype.md)
  Constants indicating the types of items to search.
### Searching by Content
- [var title: INSpeakableString?](./insearchfornotebookitemsintent/title.md)
  The title text to search for in a note, task, or task list.
- [var content: String?](./insearchfornotebookitemsintent/content.md)
  The text to search for in the body of a note.
### Searching for Tasks by Their Status
- [var status: INTaskStatus](./insearchfornotebookitemsintent/status.md)
  The completion state to look for when searching for tasks.
- [enum INTaskStatus](./intaskstatus.md)
  Constants indicating the completion state of a task.
### Searching for Tasks by Location
- [var location: CLPlacemark?](./insearchfornotebookitemsintent/location.md)
  The value to use when searching for location-triggered reminders.
- [var locationSearchType: INLocationSearchType](./insearchfornotebookitemsintent/locationsearchtype.md)
  An indicator of how to apply location values to your search.
- [enum INLocationSearchType](./inlocationsearchtype.md)
  Constants indicating the type of location-based search to perform.
### Searching by Date
- [var dateTime: INDateComponentsRange?](./insearchfornotebookitemsintent/datetime.md)
  The value to use when performing date-based searches.
- [var dateSearchType: INDateSearchType](./insearchfornotebookitemsintent/datesearchtype.md)
  An indicator of how to apply date values to your search.
- [enum INDateSearchType](./indatesearchtype.md)
  Constants indicating the type of date-based search to perform.
### Identifying the Notebook Item
- [var notebookItemIdentifier: String?](./insearchfornotebookitemsintent/notebookitemidentifier.md)
  The unique identifier that your app assigned to the item.
### Searching for Tasks by Their Priority
- [var taskPriority: INTaskPriority](./insearchfornotebookitemsintent/taskpriority.md)
- [enum INTaskPriority](./intaskpriority.md)
  Constants indicating the priority for a task.
- [var temporalEventTriggerTypes: INTemporalEventTriggerTypeOptions](./insearchfornotebookitemsintent/temporaleventtriggertypes.md)
- [struct INTemporalEventTriggerTypeOptions](./intemporaleventtriggertypeoptions.md)
  Constants indicating how often to trigger an event.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Notebook Search
- [protocol INSearchForNotebookItemsIntentHandling](./insearchfornotebookitemsintenthandling.md)
  The handler interface for searching for notes, tasks, and reminders.
- [class INSearchForNotebookItemsIntentResponse](./insearchfornotebookitemsintentresponse.md)
  Your app’s response to a request to search for notes, tasks, or reminders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintent)*