# NSView.DefinitionOptionKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Keys to include in your definition.

**Availability**:
- macOS

## Declaration

```swift
struct DefinitionOptionKey
```

```c
typedef NSString * NSDefinitionOptionKey;
```

## Topics

### Option Key
- [static let presentationType: NSView.DefinitionOptionKey](./definitionoptionkey/presentationtype.md)
  An optional key in the options dictionary that specifies the presentation type of the definition display.
### Initializers
- [init(rawValue: String)](./definitionoptionkey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Displaying Definition Windows
- [func showDefinition(for: NSAttributedString?, at: NSPoint)](./showdefinition%28for,at%29.md)
  Shows a window displaying the definition of the attributed string at the specified point.
- [func showDefinition(for: NSAttributedString?, range: NSRange, options: [NSView.DefinitionOptionKey : Any]?, baselineOriginProvider: ((NSRange) -> NSPoint)?)](./showdefinition%28for,range,options,baselineoriginprovider%29.md)
  Shows a window displaying the definition of the specified range of the attributed string.
- [NSView.DefinitionPresentationType](./definitionpresentationtype.md)
  Presentation options for the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/definitionoptionkey)*