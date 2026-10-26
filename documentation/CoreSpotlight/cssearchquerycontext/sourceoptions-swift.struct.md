# CSSearchQueryContext.SourceOptions

**Framework**: Core Spotlight  
**Kind**: struct  
**Role**: Structure

The query source options to allow or deny Mail messages in the search.

**Availability**:
- macOS 13.0+

## Declaration

```swift
struct SourceOptions
```

```c
enum CSSearchQuerySourceOptions : NSUInteger;
```

## Topics

### Search options
- [static var allowMail: CSSearchQueryContext.SourceOptions](./sourceoptions-swift.struct/allowmail.md)
  The query allows Mail messages in the search.
### Initializers
- [init(rawValue: UInt)](./sourceoptions-swift.struct/init%28rawvalue%29.md)
### Enumeration Cases
- [CSSearchQuerySourceOptionDefault](../cssearchquerysourceoptions/cssearchquerysourceoptiondefault.md)
  The query uses the default search option that excludes Mail messages.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Configuring search behavior
- [var fetchAttributes: [String]](./fetchattributes.md)
  The attributes the system fetches for the searchable items.
- [var keyboardLanguage: String?](./keyboardlanguage.md)
  The language used for the query.
- [var sourceOptions: CSSearchQueryContext.SourceOptions](./sourceoptions-swift.property.md)
  The query source options to allow or deny Mail messages in the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchquerycontext/sourceoptions-swift.struct)*