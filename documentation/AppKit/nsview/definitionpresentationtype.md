# NSView.DefinitionPresentationType

**Framework**: AppKit  
**Kind**: struct

Presentation options for the window.

**Availability**:
- macOS ?+

## Declaration

```swift
struct DefinitionPresentationType
```

## Topics

### Presentation Values
- [static let dictionaryApplication: NSView.DefinitionPresentationType](nsview/definitionpresentationtype/dictionaryapplication.md)
  A possible value of the [`presentationType`](nsview/definitionoptionkey/presentationtype.md) dictionary key that invokes Dictionary application to display the definition.
- [static let overlay: NSView.DefinitionPresentationType](nsview/definitionpresentationtype/overlay.md)
  A possible value of the [`presentationType`](nsview/definitionoptionkey/presentationtype.md) dictionary key that produces a small overlay window at the string location,
### Initializers
- [init(rawValue: String)](nsview/definitionpresentationtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func showDefinition(for: NSAttributedString?, at: NSPoint)](nsview/showdefinition(for:at:).md)
  Shows a window displaying the definition of the attributed string at the specified point.
- [func showDefinition(for: NSAttributedString?, range: NSRange, options: [NSView.DefinitionOptionKey : Any]?, baselineOriginProvider: ((NSRange) -> NSPoint)?)](nsview/showdefinition(for:range:options:baselineoriginprovider:).md)
  Shows a window displaying the definition of the specified range of the attributed string.
- [NSView.DefinitionOptionKey](nsview/definitionoptionkey.md)
  Keys to include in your definition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/definitionpresentationtype)*