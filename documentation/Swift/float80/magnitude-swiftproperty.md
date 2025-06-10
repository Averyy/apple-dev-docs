# magnitude

**Framework**: Swift  
**Kind**: property

The magnitude of this value.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var magnitude: Float80 { get }
```

#### Discussion

For any numeric value `x`, `x.magnitude` is the absolute value of `x`. You can use the `magnitude` property in operations that are simpler to implement in terms of unsigned values, such as printing the value of an integer, which is just printing a ‘-’ character in front of an absolute value.

```swift
let x = -200
// x.magnitude == 200
```

The global `abs(_:)` function provides more familiar syntax when you need to find an absolute value. In addition, because `abs(_:)` always returns a value of the same type, even in a generic context, using the function instead of the `magnitude` property is encouraged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/magnitude-swift.property)*