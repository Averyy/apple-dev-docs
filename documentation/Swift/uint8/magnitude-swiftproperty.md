# magnitude

**Framework**: Swift  
**Kind**: property

The magnitude of this value.

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
var magnitude: Self { get }
```

#### Discussion

Every unsigned integer is its own magnitude, so for any value `x`, `x == x.magnitude`.

The global `abs(_:)` function provides more familiar syntax when you need to find an absolute value. In addition, because `abs(_:)` always returns a value of the same type, even in a generic context, using the function instead of the `magnitude` property is encouraged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint8/magnitude-swift.property)*