# NSSaveOptions

**Framework**: Foundation  
**Kind**: enum

The [`saveOptions`](nsclosecommand/saveoptions.md) method returns one of the following constants to indicate how to deal with saving any modified documents:

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum NSSaveOptions
```

## Topics

### Constants
- [NSSaveOptions.yes](nssaveoptions/yes.md)
  Indicates a modified document should be saved on closing without asking the user.
- [NSSaveOptions.no](nssaveoptions/no.md)
  Indicates a modified document should not be saved on closing.
- [NSSaveOptions.ask](nssaveoptions/ask.md)
  Indicates the user should be asked before saving any modified documents on closing. When no option is specified, this is the default.
### Initializers
- [init?(rawValue: UInt)](nssaveoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssaveoptions)*