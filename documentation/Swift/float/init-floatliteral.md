# init(floatLiteral:)

**Framework**: Swift  
**Kind**: init

Creates an instance initialized to the specified floating-point value.

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
init(floatLiteral value: Float)
```

#### Discussion

Do not call this initializer directly. Instead, initialize a variable or constant using a floating-point literal. For example:

```swift
let x = 21.5
```

In this example, the assignment to the `x` constant calls this floating-point literal initializer behind the scenes.

## Parameters

- `value`: The value to create.

## See Also

- [init()](float/init.md)
- [init(integerLiteral: Int64)](float/init(integerliteral:).md)
  Creates an instance initialized to the specified integer value.
- [init(integerLiteral: Self)](float/init(integerliteral:)-6hc7h.md)
- [func advanced(by: Float) -> Float](float/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Float) -> Float](float/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func write<Target>(to: inout Target)](float/write(to:).md)
  Writes a textual representation of this instance into the given output stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/init(floatliteral:))*