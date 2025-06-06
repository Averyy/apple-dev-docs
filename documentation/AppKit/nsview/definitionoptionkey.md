# NSView.DefinitionOptionKey

**Framework**: AppKit  
**Kind**: struct

Keys to include in your definition.

**Availability**:
- macOS ?+

## Declaration

```swift
struct DefinitionOptionKey
```

## Topics

### Option Key
- [static let presentationType: NSView.DefinitionOptionKey](nsview/definitionoptionkey/presentationtype.md)
  An optional key in the options dictionary that specifies the presentation type of the definition display.
### Initializers
- [init(rawValue: String)](nsview/definitionoptionkey/init(rawvalue:).md)

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
- [NSView.DefinitionPresentationType](nsview/definitionpresentationtype.md)
  Presentation options for the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/definitionoptionkey)*