# nonzeroBitCount

**Framework**: Swift  
**Kind**: property

The number of bits equal to 1 in this value’s binary representation.

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
var nonzeroBitCount: Int { get }
```

#### Discussion

For example, in a fixed-width integer type with a `bitWidth` value of 8, the number  has five bits equal to .

```swift
let x: Int8 = 0b0001_1111
// x == 31
// x.nonzeroBitCount == 5
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int128/nonzerobitcount)*