# PersonNameComponentsFormatter.Options

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Options for formatting person name components.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct Options
```

```c
enum NSPersonNameComponentsFormatterOptions : NSUInteger;
```

## Topics

### Constants
- [static var phonetic: PersonNameComponentsFormatter.Options](./options/phonetic.md)
  The formatter should format the component object’s `phoneticRepresentation` components instead of its own components.
### Initializers
- [init(rawValue: UInt)](./options/init%28rawvalue%29.md)

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

### Constants
- [PersonNameComponentsFormatter.Style](./style-swift.enum.md)
  The formatting styles for person name components.
- [Attributed String Key](../attributed-string-key.md)
  This constant is used as a key for person name component attributes in attributed strings returned by the [`annotatedString(from:)`](./annotatedstring%28from%29.md) method
- [Attributed String Components](../attributed-string-components.md)
  These constants are used to identify individual components of attributed strings returned by the [`annotatedString(from:)`](./annotatedstring%28from%29.md) method.
- [Component Delimiter](../component-delimiter.md)
  This constant defines the delimiter used to separate name components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/options)*