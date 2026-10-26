# CTFontOptions

**Framework**: Core Text  
**Kind**: struct  
**Role**: Structure

Options for font creation and descriptor matching.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct CTFontOptions
```

```c
enum CTFontOptions : CFOptionFlags;
```

#### Overview

Use these options with the functions [`CTFontCreateWithNameAndOptions(_:_:_:_:)`](./ctfontcreatewithnameandoptions%28_,_,_,_%29.md) and [`CTFontCreateWithFontDescriptorAndOptions(_:_:_:_:)`](./ctfontcreatewithfontdescriptorandoptions%28_,_,_,_%29.md).

## Topics

### Constants
- [static var preventAutoActivation: CTFontOptions](./ctfontoptions/preventautoactivation.md)
  Prevents automatic font activation.
- [static var preferSystemFont: CTFontOptions](./ctfontoptions/prefersystemfont.md)
  Font matching prefers to match Apple system fonts.
- [kCTFontOptionsDefault](./ctfontoptions/kctfontoptionsdefault.md)
  Default options are used.
### Initializers
- [init(rawValue: CFOptionFlags)](./ctfontoptions/init%28rawvalue%29.md)
  Creates a font options structure with the specified raw value.
### Type Properties
- [static var preventAutoDownload: CTFontOptions](./ctfontoptions/preventautodownload.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Enumerations
- [enum CTFontUIFontType](./ctfontuifonttype.md)
  Constants that represent the specific user-interface purpose to specify for font creation.
- [typealias CTFontTableTag](./ctfonttabletag.md)
  Font table tags provide access to font table data.
- [struct CTFontTableOptions](./ctfonttableoptions.md)
  Constants that describe font table options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontoptions)*