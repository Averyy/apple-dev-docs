# OptionSet

**Framework**: Swift  
**Kind**: protocol

A type that presents a mathematical set interface to a bit set.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol OptionSet : RawRepresentable, SetAlgebra
```

#### Overview

You use the `OptionSet` protocol to represent bitset types, where individual bits represent members of a set. Adopting this protocol in your custom types lets you perform set-related operations such as membership tests, unions, and intersections on those types. What’s more, when implemented using specific criteria, adoption of this protocol requires no extra work on your part.

When creating an option set, include a `rawValue` property in your type declaration. For your type to automatically receive default implementations for set-related operations, the `rawValue` property must be of a type that conforms to the `FixedWidthInteger` protocol, such as `Int` or `UInt8`. Next, create unique options as static properties of your custom type using unique powers of two (1, 2, 4, 8, 16, and so forth) for each individual property’s raw value so that each property can be represented by a single bit of the type’s raw value.

For example, consider a custom type called `ShippingOptions` that is an option set of the possible ways to ship a customer’s purchase. `ShippingOptions` includes a `rawValue` property of type `Int` that stores the bit mask of available shipping options. The static members `nextDay`, `secondDay`, `priority`, and `standard` are unique, individual options.

```swift
struct ShippingOptions: OptionSet {
    let rawValue: Int

    static let nextDay    = ShippingOptions(rawValue: 1 << 0)
    static let secondDay  = ShippingOptions(rawValue: 1 << 1)
    static let priority   = ShippingOptions(rawValue: 1 << 2)
    static let standard   = ShippingOptions(rawValue: 1 << 3)

    static let express: ShippingOptions = [.nextDay, .secondDay]
    static let all: ShippingOptions = [.express, .priority, .standard]
}
```

Declare additional preconfigured option set values as static properties initialized with an array literal containing other option values. In the example, because the `express` static property is assigned an array literal with the `nextDay` and `secondDay` options, it will contain those two elements.

### Using an Option Set Type

When you need to create an instance of an option set, assign one of the type’s static members to your variable or constant. Alternatively, to create an option set instance with multiple members, assign an array literal with multiple static members of the option set. To create an empty instance, assign an empty array literal to your variable.

```swift
let singleOption: ShippingOptions = .priority
let multipleOptions: ShippingOptions = [.nextDay, .secondDay, .priority]
let noOptions: ShippingOptions = []
```

Use set-related operations to check for membership and to add or remove members from an instance of your custom option set type. The following example shows how you can determine free shipping options based on a customer’s purchase price:

```swift
let purchasePrice = 87.55

var freeOptions: ShippingOptions = []
if purchasePrice > 50 {
    freeOptions.insert(.priority)
}

if freeOptions.contains(.priority) {
    print("You've earned free priority shipping!")
} else {
    print("Add more to your cart for free priority shipping!")
}
// Prints "You've earned free priority shipping!"
```

## Topics

### Required Initializer
- [init(rawValue: Self.RawValue)](optionset/init(rawvalue:).md)
  Creates a new option set from the given raw value.
### Element
- [associatedtype Element = Self](optionset/element.md)
  The element type of the option set.

## Relationships

### Inherits From
- [Equatable](equatable.md)
- [ExpressibleByArrayLiteral](expressiblebyarrayliteral.md)
- [RawRepresentable](rawrepresentable.md)
- [SetAlgebra](setalgebra.md)
### Conforming Types
- [ClockTraits](clocktraits.md)

## See Also

- [struct Set](set.md)
  An unordered collection of unique elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optionset)*