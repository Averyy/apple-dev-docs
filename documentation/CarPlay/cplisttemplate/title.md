# title

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The title to display in the navigation bar when the list is visible.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var title: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * title;
```

## See Also

### Managing the supplemental content
- [var listHeader: CPListTemplateDetailsHeader?](./listheader.md)
  An optional header to display between the navigation bar and first section of content.
- [var headerGridButtons: [CPGridButton]?](./headergridbuttons.md)
  Buttons to display in the header area above the list content.
- [var assistantCellConfiguration: CPAssistantCellConfiguration?](./assistantcellconfiguration.md)
  The object that provides the configuration attributes for the assistant cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/title)*