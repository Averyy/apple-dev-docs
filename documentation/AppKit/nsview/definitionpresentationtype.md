# NSView.DefinitionPresentationType

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Presentation options for the window.

**Availability**:
- macOS

## Declaration

```swift
struct DefinitionPresentationType
```

```c
typedef NSString * NSDefinitionPresentationType;
```

## Topics

### Presentation Values
- [static let dictionaryApplication: NSView.DefinitionPresentationType](./definitionpresentationtype/dictionaryapplication.md)
  A possible value of the [`presentationType`](./definitionoptionkey/presentationtype.md) dictionary key that invokes Dictionary application to display the definition.
- [static let overlay: NSView.DefinitionPresentationType](./definitionpresentationtype/overlay.md)
  A possible value of the [`presentationType`](./definitionoptionkey/presentationtype.md) dictionary key that produces a small overlay window at the string location,
### Initializers
- [init(rawValue: String)](./definitionpresentationtype/init%28rawvalue%29.md)

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
- [NSView.DefinitionOptionKey](./definitionoptionkey.md)
  Keys to include in your definition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/definitionpresentationtype)*