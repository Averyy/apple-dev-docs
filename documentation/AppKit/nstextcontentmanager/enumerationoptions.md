# NSTextContentManager.EnumerationOptions

**Framework**: AppKit  
**Kind**: struct

Values that control the order in which the framework enumerates text elements.

**Availability**:
- macOS 12.0+

## Declaration

```swift
struct EnumerationOptions
```

## Topics

### Creating text element provider enumeration options
- [init(rawValue: UInt)](nstextcontentmanager/enumerationoptions/init(rawvalue:).md)
  Creates a new text element provider with the provided raw value.
### Accessing the enumeration setting
- [static var reverse: NSTextContentManager.EnumerationOptions](nstextcontentmanager/enumerationoptions/reverse.md)
  Returns whether enumerations start from the end of the text element.

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

- [var delegate: (any NSTextContentManagerDelegate)?](nstextcontentmanager/delegate.md)
  The delegate for the content manager object.
- [protocol NSTextContentManagerDelegate](nstextcontentmanagerdelegate.md)
  The optional methods that delegates of content manager objects implement for customizing or validating text elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentmanager/enumerationoptions)*