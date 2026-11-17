# listHeader

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An optional header to display between the navigation bar and first section of content.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var listHeader: CPListTemplateDetailsHeader? { get set }
```

```objc
@property (nonatomic, strong, nullable) CPListTemplateDetailsHeader * listHeader;
```

## Discussion

The list header displays additional context or summary information above the sections of the list. Use this property to retrieve the previously configured header. If you modify this property when the list is visible, CarPlay refreshes the appearance of the header to reflect the new content.

## See Also

### Managing the supplemental content
- [var title: String?](./title.md)
  The title to display in the navigation bar when the list is visible.
- [var headerGridButtons: [CPGridButton]?](./headergridbuttons.md)
  Buttons to display in the header area above the list content.
- [var assistantCellConfiguration: CPAssistantCellConfiguration?](./assistantcellconfiguration.md)
  The object that provides the configuration attributes for the assistant cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/listheader)*