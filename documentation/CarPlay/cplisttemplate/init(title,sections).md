# init(title:sections:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a list template with an array of list sections and optional title.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(title: String?, sections: [CPListSection])
```

```objc
- (instancetype) initWithTitle:(NSString *) title sections:(NSArray<CPListSection *> *) sections;
```

## Return Value

A newly initialized list template.

## Parameters

- `title`: A title that appears in the navigation bar while the template is visible.
- `sections`: An array of list sections, each with zero or more list items.

## See Also

### Creating a List Template
- [init(title: String?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?)](./init%28title,sections,assistantcellconfiguration%29.md)
  Creates a sectioned list template that optionally displays the assistant cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/init(title:sections:))*