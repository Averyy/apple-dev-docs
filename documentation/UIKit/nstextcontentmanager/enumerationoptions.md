# NSTextContentManager.EnumerationOptions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSTextContentManagerEnumerationOptions : NSUInteger;
```

## Topics

### Creating text element provider enumeration options
- [init(rawValue: UInt)](./enumerationoptions/init%28rawvalue%29.md)
  Creates a new text element provider with the provided raw value.
### Accessing the enumeration setting
- [static var reverse: NSTextContentManager.EnumerationOptions](./enumerationoptions/reverse.md)
  Returns whether enumerations start from the end of the text element.
### Enumeration options
- [NSTextContentManagerEnumerationOptionsNone](../nstextcontentmanagerenumerationoptions/nstextcontentmanagerenumerationoptionsnone.md)
  The value that represents no custom enumeration handing in text element enumerations.

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

### Customizing and validating text elements
- [var delegate: (any NSTextContentManagerDelegate)?](./delegate.md)
  The delegate for the content manager object.
- [protocol NSTextContentManagerDelegate](../nstextcontentmanagerdelegate.md)
  The optional methods that delegates of content manager objects implement for customizing or validating text elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontentmanager/enumerationoptions)*