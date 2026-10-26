# INSnoozeTasksIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to snooze one or more tasks.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: INSnoozeTasksIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class INSnoozeTasksIntent
```

```objc
@interface INSnoozeTasksIntent : INIntent
```

#### Overview

Siri creates an [`INSnoozeTasksIntent`](./insnoozetasksintent.md) object when the user marks one or more tasks for snoozing. The intent object can contain the task information.

To handle this intent, the handler object in your Intents extension must adopt the [`INSnoozeTasksIntentHandling`](./insnoozetasksintenthandling.md) protocol. Your handler should confirm the request and create an [`INSnoozeTasksIntentResponse`](./insnoozetasksintentresponse.md) object with the updated task information.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents |
| Always requires unlocked device | No |

##### Example Phrases

Users can ask Siri to snooze tasks in a variety of ways. The table below provides a few sample phrases in different languages. You can use these phrases during testing to trigger your intents. This list isn’t exhaustive and Siri may recognize many other phrases.

| Locale | Example 1 | Example 2 |
| --- | --- | --- |
| en | Ignore my buy milk reminder | Snooze that reminder for 10 minutes |
| zh_CN | 忽略买牛奶的提醒事项 | 过10分钟后再提醒我这个 |
| zh_HK | 忽略買牛奶嘅提醒事項 | 延遲提醒事項10分鐘 |
| zh_TW | 忽略買牛奶的提醒事項 | 延後提醒事項10分鐘 |
| yue_CN | 忽略买牛奶嘅提醒事项 | 延迟提醒事项10分钟 |
| ar | تجاهل تذكير شراء الحليب | نبهني مرة ثانية بذلك التذكير بعد 10 دقائق |
| da | Ignorer min køb mælk påmindelse | Snooze den påmindelse i 10 minutter |
| de | Ignoriere meine Milch kaufen Erinnerung | Snooze die Erinnerung für 10 Minuten |
| es | Posponer mi recordatorio comprar leche | Pospón ese recordatorio por 10 minutos |
| fi | Hiljennä muistutus osta maitoa | Hiljennä muistutus kymmeneksi minuutiksi |
| fr | Ignore mon rappel pour acheter du lait | Rappelle-le moi encore dans 10 minutes |
| he | תתעלם מהתזכורת לקנות חלב | תשהי את התזכורת ב-10 דקות |
| it | Ignora il promemoria comprare il latte | Posticipa quel promemoria di 10 minuti |
| ja | 牛乳を買うというリマインダーを無視して | そのリマインダーを10分スヌーズして |
| ko | 우유 사기 미리 알림 다시  알려줘 | 이 미리 알림 10분동안 수느즈해줘 |
| ms | abaikan peringatan beli susu saya | tidurkan peringatan itu untuk 10 minit |
| nb | Ignorer min kjøpe melk påminnelse | Utsett den påminnelsen i 10 minutter |
| nl | Negeer de melk kopen herinnering | Sluimer die herinnering voor 10 minuten |
| pt | Ignorar meu lembrete para comprar leite | Adie aquele lembrete por 10 minutos |
| ru | Повтори напоминание купить молоко позже | Отложи это напоминание на 10 минут |
| sv | Ignorera min köp mjölk påminnelse | Snooza den påminnelsen i 10 minuter |
| th | เลื่อนเตือนซื้อนม | สนูซเตือนความจำอันนี้ไป 10 นาที |
| tr |  | Süt almayı 10 dakika sonra tekrar hatırlat |

## Topics

### Initializing the Intent Object
- [convenience init(tasks: [INTask]?, nextTriggerTime: INDateComponentsRange?, all: Bool?)](./insnoozetasksintent/init%28tasks,nexttriggertime,all%29.md)
  Initializes the intent object with information about the tasks to snooze and when to snooze them.
### Getting the Task Information
- [var nextTriggerTime: INDateComponentsRange?](./insnoozetasksintent/nexttriggertime.md)
  The next time after the current time that triggers a task to snooze.
- [var tasks: [INTask]?](./insnoozetasksintent/tasks.md)
  An array of tasks to snooze.
- [var all: Bool?](./insnoozetasksintent/all-spsb.md)
  A Boolean value that indicates whether to snooze all of the tasks.

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

### Task Deferral
- [protocol INSnoozeTasksIntentHandling](./insnoozetasksintenthandling.md)
  The handler interface that snoozes tasks in a task list.
- [class INSnoozeTasksIntentResponse](./insnoozetasksintentresponse.md)
  Your response to a delete tasks request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insnoozetasksintent)*