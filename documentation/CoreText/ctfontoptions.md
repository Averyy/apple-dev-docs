# CTFontOptions

**Framework**: Core Text  
**Kind**: struct

Options for font creation and descriptor matching.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CTFontOptions
```

#### Overview

Use these options with the functions [`CTFontCreateWithNameAndOptions(_:_:_:_:)`](ctfontcreatewithnameandoptions(_:_:_:_:).md) and [`CTFontCreateWithFontDescriptorAndOptions(_:_:_:_:)`](ctfontcreatewithfontdescriptorandoptions(_:_:_:_:).md).

## Topics

### Constants
- [static var preventAutoActivation: CTFontOptions](ctfontoptions/preventautoactivation.md)
  Prevents automatic font activation.
- [static var preferSystemFont: CTFontOptions](ctfontoptions/prefersystemfont.md)
  Font matching prefers to match Apple system fonts.
### Initializers
- [init(rawValue: CFOptionFlags)](ctfontoptions/init(rawvalue:).md)
  Creates a font options structure with the specified raw value.
### Type Properties
- [static var preventAutoDownload: CTFontOptions](ctfontoptions/preventautodownload.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [enum CTFontUIFontType](ctfontuifonttype.md)
  Constants that represent the specific user-interface purpose to specify for font creation.
- [typealias CTFontTableTag](ctfonttabletag.md)
  Font table tags provide access to font table data.
- [struct CTFontTableOptions](ctfonttableoptions.md)
  Constants that describe font table options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontoptions)*