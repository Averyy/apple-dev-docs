# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new instance from the given integer.

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
init<T>(_ source: T) where T : BinaryInteger
```

#### Discussion

Use this initializer to convert from another integer type when you know the value is within the bounds of this type. Passing a value that can’t be represented in this type results in a runtime error.

In the following example, the constant `y` is successfully created from `x`, an `Int` instance with a value of `100`. Because the `Int8` type can represent `127` at maximum, the attempt to create `z` with a value of `1000` results in a runtime error.

```swift
let x = 100
let y = Int8(x)
// y == 100
let z = Int8(x * 10)
// Error: Not enough bits to represent the given value
```

## Parameters

- `source`: A value to convert to this type of integer. The value   passed as   must be representable in this type.

## See Also

- [init?<T>(exactly: T)](int/init(exactly:)-b1dy.md)
- [init<Other>(clamping: Other)](int/init(clamping:).md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<T>(truncatingIfNeeded: T)](int/init(truncatingifneeded:).md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
- [init(bitPattern: UInt)](int/init(bitpattern:)-72037.md)
  Creates a new instance with the same memory representation as the given value.
- [init?(exactly: NSNumber)](int/init(exactly:)-177ax.md)
- [init(truncating: NSNumber)](int/init(truncating:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/init(_:)-4ekvl)*