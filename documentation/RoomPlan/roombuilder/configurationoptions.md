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
- [let rawValue: Int](roombuilder/configurationoptions/rawvalue-swift.property.md)
  A raw value for a configuration option.
### Choosing a configuration option
- [static let beautifyObjects: RoomBuilder.ConfigurationOptions](roombuilder/configurationoptions/beautifyobjects.md)
  An option that instructs the captured room to enhance its look.
### Type Aliases
- [RoomBuilder.ConfigurationOptions.ArrayLiteralElement](roombuilder/configurationoptions/arrayliteralelement.md)
  The type of the elements of an array literal.
- [RoomBuilder.ConfigurationOptions.Element](roombuilder/configurationoptions/element.md)
  The element type of the option set.
- [RoomBuilder.ConfigurationOptions.RawValue](roombuilder/configurationoptions/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](roombuilder/configurationoptions/equatable-implementations.md)
- [OptionSet Implementations](roombuilder/configurationoptions/optionset-implementations.md)
- [SetAlgebra Implementations](roombuilder/configurationoptions/setalgebra-implementations.md)

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