# init(clamping:)

**Framework**: Swift  
**Kind**: init

Creates a new instance with the representable value that’s closest to the given integer.

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
init<Other>(clamping source: Other) where Other : BinaryInteger
```

#### Discussion

If the value passed as `source` is greater than the maximum representable value in this type, the result is the type’s `max` value. If `source` is less than the smallest representable value in this type, the result is the type’s `min` value.

In this example, `x` is initialized as an `Int8` instance by clamping `500` to the range `-128...127`, and `y` is initialized as a `UInt` instance by clamping `-500` to the range `0...UInt.max`.

```swift
let x = Int8(clamping: 500)
// x == 127
// x == Int8.max

let y = UInt(clamping: -500)
// y == 0
```

## Parameters

- `source`: An integer to convert to this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int8/init(clamping:))*