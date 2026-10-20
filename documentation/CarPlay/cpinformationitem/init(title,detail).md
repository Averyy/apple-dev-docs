# init(title:detail:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates an information item with a title and detail text.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(title: String?, detail: String?)
```

```objc
- (instancetype) initWithTitle:(NSString *) title detail:(NSString *) detail;
```

## Parameters

- `title`: The text that the template displays as the item’s title.
- `detail`: The text that the template displays below or beside the title, depending on the template’s layout. See [`CPInformationTemplateLayout`](../cpinformationtemplatelayout.md) for more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinformationitem/init(title:detail:))*