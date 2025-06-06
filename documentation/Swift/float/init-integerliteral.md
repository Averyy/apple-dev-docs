# init(integerLiteral:)

**Framework**: Swift  
**Kind**: init

Creates an instance initialized to the specified integer value.

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
init(integerLiteral value: Int64)
```

#### Discussion

Do not call this initializer directly. Instead, initialize a variable or constant using an integer literal. For example:

```swift
let x = 23
```

In this example, the assignment to the `x` constant calls this integer literal initializer behind the scenes.

## Parameters

- `value`: The value to create.

## See Also

- [init()](float/init.md)
- [init(floatLiteral: Float)](float/init(floatliteral:).md)
  Creates an instance initialized to the specified floating-point value.
- [init(integerLiteral: Self)](float/init(integerliteral:)-6hc7h.md)
- [func advanced(by: Float) -> Float](float/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Float) -> Float](float/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func write<Target>(to: inout Target)](float/write(to:).md)
  Writes a textual representation of this instance into the given output stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/init(integerliteral:))*