# INAddTasksIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to add tasks to an existing task list.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class INAddTasksIntent
```

```objc
@interface INAddTasksIntent : INIntent
```

## Overview

Siri creates an instance of [`INAddTasksIntent`](./inaddtasksintent.md) when the user asks to add one or more tasks to a task list. Alternatively, if the user asks to create a note, and your app or Intents extension doesn’t support [`INCreateNoteIntent`](./increatenoteintent.md), SiriKit uses this intent instead. The intent contains the tasks to add and the target task list, and can also include location or time triggers that you assign to each of the new tasks. To process the request, your handler must adopt the [`INAddTasksIntentHandling`](./inaddtasksintenthandling.md) protocol.

[`INAddTasksIntent`](./inaddtasksintent.md) is available to both Siri Intents and Siri Suggestions and doesn’t require an unlocked device before processing.

### Example Phrases

Users can ask Siri to add tasks to a task list in a variety of ways. Although not exhaustive, the following table provides a few sample phrases, in different languages, that you can use when testing your intents.

| Locale | Example 1 | Example 2 |
| --- | --- | --- |
| `en` | Add persimmons to my shopping list | Remind me to buy dog food |
| `zh_CN` | 在我的购物列表里添加柿子 | 提醒我买狗食 |
| `zh_HK` | 喺我嘅購物清單入面加入柿餅 | 提醒我買狗糧 |
| `zh_TW` | 新增柿子到我的購物清單 | 提醒我要買狗食 |
| `yue_CN` | 喺我嘅购物清单入面加入柿饼 | 提醒我买狗粮 |
| `ar` | أضف الخوخ إلى قائمة التسوق | ذكرني بشراء طعام للكلب |
| `da` | tilføj sharonfrugt til min indkøbsliste | mind mig om at købe hundemad |
| `de` | Füge Äpfel zu meiner Einkaufsliste hinzu | Erinnere mich daran Hundefutter kaufen |
| `es` | Añade melocotones a la lista de la compra | Recuérdame comprar comida de perro |
| `fi` | Lisää ostoslistaan banaaneja | Muistuta että ostan koiranruokaa |
| `fr` | Ajoute kiwi à ma liste de courses | Rappelle-moi d’acheter de la nourriture pour chien |
| `he` | תוסיפי אפרסמונים לרשימת קניות שלי | תזכירי לי לקנות אוכל לכלבים |
| `it` | Aggiungi prezzemolo alla mia lista della spesa | Ricordami di comprare cibo per cani |
| `ja` | 買い物リストに柿を追加して | ドッグフードを買うのをリマインドして |
| `ko` | 내 쇼핑 리스트에 단감 추가해줘 | 강아지 사료 사라고 미리 알려줘 |
| `ms` | Tambah oren ke senarai beli-belah saya | Ingatkan saya untuk beli makanan anjing |
| `nb` | Legg til bananer i handlelista | Minn meg på å kjøpe hundemat |
| `nl` | Voeg sinaasappelen toe aan mijn boodschappenlijst | Herinner me eraan hondenvoer te kopen |
| `pt` | Adiciona tomate à minha lista de compras | Me lembre de comprar comida de cachorro |
| `ru` | Добавить хурму в список покупок | Напомни мне купить корм для собак |
| `sv` | Lägg till clementiner i min inköpslista | Påminn mig att köpa hundmat |
| `th` | เพิ่มขนมปังไปที่ลิสต์รายการซื้อของ | เตือนฉันให้ซื้ออาหารแมวด้วย |
| `tr` | Alışveriş listeme salatalık ekle | Köpek maması almamı anımsat |

## Topics

### Initializing the Intent Object
- [init(targetTaskList: INTaskList?, taskTitles: [INSpeakableString]?, spatialEventTrigger: INSpatialEventTrigger?, temporalEventTrigger: INTemporalEventTrigger?, priority: INTaskPriority)](./inaddtasksintent/init%28targettasklist,tasktitles,spatialeventtrigger,temporaleventtrigger,priority%29.md)
  Initializes the intent object with the specified task details.
- [convenience init(targetTaskList: INTaskList?, taskTitles: [INSpeakableString]?, spatialEventTrigger: INSpatialEventTrigger?, temporalEventTrigger: INTemporalEventTrigger?)](./inaddtasksintent/init%28targettasklist,tasktitles,spatialeventtrigger,temporaleventtrigger%29.md)
  Initializes the intent object with the specified task details.
### Getting the Task Details
- [var targetTaskList: INTaskList?](./inaddtasksintent/targettasklist.md)
  The task list to receive the new tasks.
- [var taskTitles: [INSpeakableString]?](./inaddtasksintent/tasktitles.md)
  An array of strings containing the titles of the new tasks.
- [var priority: INTaskPriority](./inaddtasksintent/priority.md)
  The priority for the new task.
### Getting the Trigger Information
- [var spatialEventTrigger: INSpatialEventTrigger?](./inaddtasksintent/spatialeventtrigger.md)
  The location-based trigger to associate with each of the new tasks.
- [var temporalEventTrigger: INTemporalEventTrigger?](./inaddtasksintent/temporaleventtrigger.md)
  The time-based trigger to associate with each of the new tasks.

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

### Task Addition
- [protocol INAddTasksIntentHandling](./inaddtasksintenthandling.md)
  The handler interface for adding tasks to a task list.
- [class INAddTasksIntentResponse](./inaddtasksintentresponse.md)
  Your response to a request to add tasks to a task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintent)*