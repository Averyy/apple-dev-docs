# INSetTaskAttributeIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to modify the attributes of a task.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSetTaskAttributeIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class INSetTaskAttributeIntent
```

```objc
@interface INSetTaskAttributeIntent : INIntent
```

#### Overview

Siri creates an [`INSetTaskAttributeIntent`](./insettaskattributeintent.md) object when the user marks a task as complete or changes the triggers used to generate reminders for the task. The intent object can contain the task information and values for any changed attributes.

To handle this intent, the handler object in your Intents extension must adopt the [`INSetTaskAttributeIntentHandling`](./insettaskattributeintenthandling.md) protocol. Your handler should confirm the request and create an [`INSetTaskAttributeIntentResponse`](./insettaskattributeintentresponse.md) object with the updated task information.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents |
| Always requires unlocked device | No |

##### Example Phrases

Users can ask Siri to modify task attributes in a variety of ways. The table below provides a few sample phrases in different languages. You can use these phrases during testing to trigger your intents. This list isn’t exhaustive and Siri may recognize many other phrases.

| Locale | Example 1 | Example 2 |
| --- | --- | --- |
| en | Mark dry cleaning as complete on `<appName>` | Check call dad off my to do list |
| zh_CN | 标记干洗为结束(在 `<appName>` 上) | 把给爸爸打电话从待办事项列表里面去掉 |
| zh_HK | 喺 `<appName>` 入面將乾洗標示為完成 | 剔咗待辦事項列表入面嘅打電話俾爸爸 |
| zh_TW | 標記乾洗為完成(在 `<appName>` 上) | 從我的待辦事項列表中刪除打電話給爸爸 |
| yue_CN | 喺 `<appName>` 入面将干洗标示为完成 | 剔咗待办事项列表入面嘅打电话俾爸爸 |
| ar | ضع علامة على تنظيف الملابس بأنه مكتمل  `<appName>`على | قم بإلغاء الاتصال على أبي من قائمة الأعمال |
| da | marker rensning som færdiggjort i `<appName>` | marker ring til far som færdig i min at gøre liste |
| de | Markiere Reinigung als erledigt auf `<appName>` | Hake Papa anrufen auf meiner Erinnerungsliste ab |
| es | Marca tintorería como completado en `<appName>` | Tacha llamar a papá de mi lista de cosas por hacer |
| fi | Merkitse auton pesu suoritetuksi apissa `<appName>` | Merkitse soita isälle suoritetuksi tehtävälistalla |
| fr | Marque laver le linge comme terminé sur `<appName>` | Supprime appeler papa de ma liste de choses à faire |
| he | תסמני ניקוי יבש כהושלם ב | תסמני את להתקשר לאבא ברשימת הדברים לעשות |
| it | Segna pulizia a secco come completato su `<appName>` | Segna chiamare papà come fatto sulla mia lista da fare |
| ja | `<appName>` でドライクリーニングを完了済みにして | Todoリストにある父に電話に完了のマークをつけて |
| ko | `<appName>` 에서 드라이 클리닝을 완료로 표시해줘 | 아빠에게 전화하기를 내 할 일 목록에서 체크하기 |
| ms | Tandakan cucian kering selesai pada `<appName>` | Tandakan panggil ayah sebagai selesai pada senarai tugasan |
| nb | Marker klesvask som utført i `<appName>` | Huk av ringe pappa på gjørelisten min |
| nl | Markeer stomerij als voltooid in `<appName>` | Vink papa bellen af op mijn takenlijst |
| pt | Marcar lavagem a seco como concluída no `<appName>` | Marcar ligar para o pai como concluído na minha lista de tarefas |
| ru | Пометить химчистку как завершенную в `<appName>` | Отметь позвонить папе в моём списке дел |
| sv | Markera tvätta som avklarad i `<appName>` | Bocka av ring pappa från min att göra-lista |
| th | ทำเครื่องหมายว่าเสร็จแล้วที่ซักแห้งบนแอพ `<appName>` | ทำเครื่องหมายโทรหาพ่อว่าเสร็จแล้วในรายการสิ่งที่ต้องทำ |
| tr | `<appName>`’de kuru temizlemeyi yapıldı olarak işaretle | Ödevlerim listesindeki son anımsatıcıyı yapıldı işaretle |

In table above, `<appName>` represents the name of the app whose Intents extension handles the request.

## Topics

### Initializing the Intent Object
- [init(targetTask: INTask?, taskTitle: INSpeakableString?, status: INTaskStatus, priority: INTaskPriority, spatialEventTrigger: INSpatialEventTrigger?, temporalEventTrigger: INTemporalEventTrigger?)](./insettaskattributeintent/init%28targettask,tasktitle,status,priority,spatialeventtrigger,temporaleventtrigger%29.md)
  Initializes the intent object with information about the task and the changes that you want to make.
- [convenience init(targetTask: INTask?, status: INTaskStatus, spatialEventTrigger: INSpatialEventTrigger?, temporalEventTrigger: INTemporalEventTrigger?)](./insettaskattributeintent/init%28targettask,status,spatialeventtrigger,temporaleventtrigger%29.md)
  Initializes the intent object with information about the task and the changes that you want to make.
### Getting the Task Information
- [var priority: INTaskPriority](./insettaskattributeintent/priority.md)
  The priority for the task.
- [var taskTitle: INSpeakableString?](./insettaskattributeintent/tasktitle.md)
  The title for the task.
- [var targetTask: INTask?](./insettaskattributeintent/targettask.md)
  The task targetted for modification.
- [var status: INTaskStatus](./insettaskattributeintent/status.md)
  The status to apply to the task.
- [enum INTaskStatus](./intaskstatus.md)
  Constants indicating the completion state of a task.
### Getting the Triggers
- [var temporalEventTrigger: INTemporalEventTrigger?](./insettaskattributeintent/temporaleventtrigger.md)
  The time-based trigger to apply to the task.
- [var spatialEventTrigger: INSpatialEventTrigger?](./insettaskattributeintent/spatialeventtrigger.md)
  The location-based trigger to apply to the task.

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

### Task Attributes
- [protocol INSetTaskAttributeIntentHandling](./insettaskattributeintenthandling.md)
  The handler interface for updating the attributes of an existing task.
- [class INSetTaskAttributeIntentResponse](./insettaskattributeintentresponse.md)
  Your response to a request to modify the attributes of an existing task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintent)*