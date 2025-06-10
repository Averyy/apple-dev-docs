# leadingZeroBitCount

**Framework**: Swift  
**Kind**: property

The number of leading zeros in this value’s binary representation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var leadingZeroBitCount: Int { get }
```

#### Discussion

For example, in a fixed-width integer type with a `bitWidth` value of 8, the number  has three leading zeros.

```swift
let x: Int8 = 0b0001_1111
// x == 31
// x.leadingZeroBitCount == 3
```

If the value is zero, then `leadingZeroBitCount` is equal to `bitWidth`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int128/leadingzerobitcount)*