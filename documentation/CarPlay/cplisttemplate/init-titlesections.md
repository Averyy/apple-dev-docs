# init(title:sections:)

**Framework**: CarPlay  
**Kind**: init

Creates a list template with an array of list sections and optional title.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
init(title: String?, sections: [CPListSection])
```

#### Return Value

A newly initialized list template.

## Parameters

- `title`: A title that appears in the navigation bar while the template is visible.
- `sections`: An array of list sections, each with zero or more list items.

## See Also

- [init(title: String?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?)](cplisttemplate/init(title:sections:assistantcellconfiguration:).md)
  Creates a sectioned list template that optionally displays the assistant cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/init(title:sections:))*