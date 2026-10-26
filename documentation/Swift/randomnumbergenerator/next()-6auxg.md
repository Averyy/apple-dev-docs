# next()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns a value from a uniform, independent distribution of binary data.

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
mutating func next<T>() -> T where T : FixedWidthInteger, T : UnsignedInteger
```

#### Return Value

A random value of `T`. Bits are randomly distributed so that every value of `T` is equally likely to be returned.

#### Discussion

Use this method when you need random binary data to generate another value. If you need an integer value within a specific range, use the static `random(in:using:)` method on that integer type instead of this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/randomnumbergenerator/next()-6auxg)*