# RoomBuilder.ConfigurationOptions

**Framework**: RoomPlan  
**Kind**: struct

Options that configure a room builder.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
struct ConfigurationOptions
```

#### Overview

The `options` argument to the [`RoomBuilder`](roombuilder.md) initializer [`init(options:)`](roombuilder/init(options:).md) is of this type.

## Topics

### Creating a configuration option
- [init(rawValue: Int)](roombuilder/configurationoptions/init(rawvalue:).md)
  Creates a configuration option with the specified raw value.
- [let rawValue: Int](roombuilder/configurationoptions/rawvalue.md)
  A raw value for a configuration option.
### Choosing a configuration option
- [static let beautifyObjects: RoomBuilder.ConfigurationOptions](roombuilder/configurationoptions/beautifyobjects.md)
  An option that instructs the captured room to enhance its look.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [init(options: RoomBuilder.ConfigurationOptions)](roombuilder/init(options:).md)
  Creates a room builder using the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roombuilder/configurationoptions)*