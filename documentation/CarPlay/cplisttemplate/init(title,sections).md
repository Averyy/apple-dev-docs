# init(title:sections:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a list template with a title and sections to display.

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

- `title`: The text to display in the navigation bar while the template is visible.
- `sections`: An array of sections, each with zero or more items. This initializer copies the array, trimming sections and items as needed to fit within the limits in the [`maximumSectionCount`](./maximumsectioncount.md) and [`maximumItemCount`](./maximumitemcount.md) properties. The initializer trims sections from the end of the array, and keeps adding items section by section until it reaches the maximum.

## See Also

### Creating a list template
- [init(title: String?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?)](./init%28title,sections,assistantcellconfiguration%29.md)
  Creates a list template with a title, sections, and an assistant cell.
- [init(title: String?, listHeader: CPListTemplateDetailsHeader?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?)](./init%28title,listheader,sections,assistantcellconfiguration%29.md)
  Creates a list template with a title, sections, and a header and assistant cell with optional details.
- [init(title: String?, sections: [CPListSection], assistantCellConfiguration: CPAssistantCellConfiguration?, headerGridButtons: [CPGridButton]?)](./init%28title,sections,assistantcellconfiguration,headergridbuttons%29.md)
  Creates a list template with a title, sections, an optional assistant cell, and one or more buttons to display in the header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/init(title:sections:))*