# RoomBuilder.ConfigurationOptions

**Framework**: RoomPlan  
**Kind**: struct  
**Role**: Structure

Options that configure a room builder.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct ConfigurationOptions
```

## Overview

The `options` argument to the [`RoomBuilder`](../roombuilder.md) initializer [`init(options:)`](./init%28options%29.md) is of this type.

## Topics

### Creating a configuration option
- [init(rawValue: Int)](./configurationoptions/init%28rawvalue%29.md)
  Creates a configuration option with the specified raw value.
- [let rawValue: Int](./configurationoptions/rawvalue.md)
  A raw value for a configuration option.
### Choosing a configuration option
- [static let beautifyObjects: RoomBuilder.ConfigurationOptions](./configurationoptions/beautifyobjects.md)
  An option that instructs the captured room to enhance its look.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Creating a room builder
- [init(options: RoomBuilder.ConfigurationOptions)](./init%28options%29.md)
  Creates a room builder using the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roombuilder/configurationoptions)*