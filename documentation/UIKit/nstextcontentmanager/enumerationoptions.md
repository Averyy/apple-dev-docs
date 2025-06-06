# NSTextContentManager.EnumerationOptions

**Framework**: UIKit  
**Kind**: struct

Values that control the order in which the framework enumerates text elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

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
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var delegate: (any NSTextContentManagerDelegate)?](nstextcontentmanager/delegate.md)
  The delegate for the content manager object.
- [protocol NSTextContentManagerDelegate](nstextcontentmanagerdelegate.md)
  The optional methods that delegates of content manager objects implement for customizing or validating text elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontentmanager/enumerationoptions)*