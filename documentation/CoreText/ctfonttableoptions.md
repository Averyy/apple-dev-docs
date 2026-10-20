# CTFontTableOptions

**Framework**: Core Text  
**Kind**: struct  
**Role**: Structure

Constants that describe font table options.

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
struct CTFontTableOptions
```

```c
enum CTFontTableOptions : uint32_t;
```

## Topics

### Constants
- [init(rawValue: UInt32)](./ctfonttableoptions/init%28rawvalue%29.md)
  Creates a font table options structure with the specified raw value.
- [static var excludeSynthetic: CTFontTableOptions](./ctfonttableoptions/excludesynthetic.md)
  The font table excludes synthetic font data.

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
- [struct CTFontOptions](./ctfontoptions.md)
  Options for font creation and descriptor matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfonttableoptions)*