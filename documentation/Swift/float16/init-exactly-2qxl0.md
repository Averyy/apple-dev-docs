# init(exactly:)

**Framework**: Swift  
**Kind**: init

Creates a new value, if the given integer can be represented exactly.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init?<Source>(exactly value: Source) where Source : BinaryInteger
```

#### Discussion

If the given integer cannot be represented exactly, the result is `nil`.

## Parameters

- `value`: The integer to convert to a floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/init(exactly:)-2qxl0)*