# write(to:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Writes a textual representation of this instance into the given output stream.

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
func write<Target>(to target: inout Target) where Target : TextOutputStream
```

## See Also

### Infrequently Used Functionality
- [init()](./init%28%29.md)
- [init(integerLiteral: Int64)](./init%28integerliteral%29.md)
  Creates an instance initialized to the specified integer value.
- [init(floatLiteral: Float)](./init%28floatliteral%29.md)
  Creates an instance initialized to the specified floating-point value.
- [init(integerLiteral: Self)](./init%28integerliteral%29-6hc7h.md)
- [func advanced(by: Float) -> Float](./advanced%28by%29.md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Float) -> Float](./distance%28to%29.md)
  Returns the distance from this value to the given value, expressed as a stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/write(to:))*