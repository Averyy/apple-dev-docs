# INCreateTaskListIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to create a new task list.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INCreateTaskListIntent
```

```objc
@interface INCreateTaskListIntent : INIntent
```

## Overview

Siri creates an [`INCreateTaskListIntent`](./increatetasklistintent.md) object when the user asks to create a new task list. The intent object can contain the title of the task list, a set of initial tasks, and possibly the group in which to create the task list.

To handle this intent, the handler object in your Intents extension must adopt the [`INCreateTaskListIntentHandling`](./increatetasklistintenthandling.md) protocol. Your handler should confirm the request and create an [`INCreateTaskListIntentResponse`](./increatetasklistintentresponse.md) object with the updated task list.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents |
| Always requires unlocked device | No |

### Example Phrases

Users can ask Siri to create task lists in a variety of ways. The table below provides a few sample phrases in different languages. You can use these phrases during testing to trigger your intents. This list isn’t exhaustive and Siri may recognize many other phrases.

| Locale | Example 1 | Example 2 |
| --- | --- | --- |
| en | Create a shopping list with bananas on `<appName>` | Start a list called Wedding Prep |
| zh_CN | 建立一个购物列表添加香蕉 (在 `<appName>` 上) | 创建一个列表叫做婚礼准备 |
| zh_HK | (喺 `<appName>` 入面)新增一個購物清單內容係香蕉 | 新增一個叫做準備婚禮嘅列表 |
| zh_TW | 新增一個購物清單香蕉(在 `<appName>` 上) | 新增一個叫做婚禮準備的列表 |
| yue_CN | (喺 `<appName>` 入面)新增一个购物清单内容系香蕉 | 新增一个叫做准备婚礼嘅列表 |
| ar | `<appName>` أنشئ قائمة تسوق بالموز على | إبدأ قائمة باسم التحضير للعرس |
| da | opret en indkøbsliste med bananer (i `<appName>`) | start en liste kaldet bryllupsforberedelse |
| de | Erstelle eine Einkaufsliste mit Bananen (auf `<appName>` ) | Erstelle eine Liste mit dem Namen Hochzeitsvorbereitung |
| es | Crea una lista de la compra con plátanos (con `<appName>` ) | Crea una lista que se llame Preparativos de la boda |
| fi | Luo ostoslista ja lisää siihen banaaneja (apissa `<appName>`) | Luo uusi lista nimeltä Häävalmistelut |
| fr | Créer une liste de courses avec des bananes (sur `<appName>`) | Commence une liste nommée Préparation du mariage |
| he | `<appName>`תצרי רשימת קניות עם בננות ב | תתחילי רשימה שנקראת הכנות לחתונה |
| it | Crea una lista shopping con banane (su `<appName>`) | Inizia una lista chiamata preparazione matrimonio |
| ja | (で)ショッピングリストを作成してバナナと書いて | 結婚式の準備というリストを作成 |
| ko | (`<appName>` 에) 바나나로 쇼핑 리스트 만들어줘 | 웨딩 준비라는 이름의 리스트 생성해줘 |
| ms | Cipta senarai beli belah dengan pisang (pada `<appName>`) | Mulakan senarai bernama Persediaan Perkahwinan |
| nb | Lag en handleliste med bananer (i `<appName>`) | Start en liste som heter forberedelser til bryllup |
| nl | Maak een boodschappenlijst met bananen (in `<appName>`) | Start een lijst genaamd huwelijksvoorbereidingen |
| pt | Crie uma lista de compras com bananas (no `<appName>`) | Iniciar uma lista chamada Preparação para o Casamento |
| ru | Создать список покупок содержащий бананы (в `<appName>`) | Создать список под названием Подготовка к свадьбе |
| sv | Skapa en inköpslista med bananer (i `<appName>`) | Starta en lista som heter bröllopsplanering |
| th | สร้างลิสต์รายการสิ่งของที่ต้องซื้อแล้วเพิ่มผลไม้ (บนแอพ `<appName>`) | สร้างลิสต์ชื่อว่าสิ่งที่ต้องเตรียมสำหรับงานแต่งงาน |
| tr | (’de) Alınacaklar listesi yarat | Düğün hazırlıkları adlı bir liste oluştur |

In the preceding examples, `<appName>` represents the name of the app whose Intents extension handles the request.

## Topics

### Initializing the Intent Object
- [init(title: INSpeakableString?, taskTitles: [INSpeakableString]?, groupName: INSpeakableString?)](./increatetasklistintent/init%28title,tasktitles,groupname%29.md)
  Initializes the intent object with the specified task list details.
### Getting the Task List Details
- [var title: INSpeakableString?](./increatetasklistintent/title.md)
  The title of the task list.
- [var taskTitles: [INSpeakableString]?](./increatetasklistintent/tasktitles.md)
  An array of strings containing the titles for individual tasks to add to the new task list.
- [var groupName: INSpeakableString?](./increatetasklistintent/groupname.md)
  The group that contains the task list.

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

### Task List Creation
- [protocol INCreateTaskListIntentHandling](./increatetasklistintenthandling.md)
  The handler interface for creating task lists.
- [class INCreateTaskListIntentResponse](./increatetasklistintentresponse.md)
  Your app’s response to a request to create a task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatetasklistintent)*