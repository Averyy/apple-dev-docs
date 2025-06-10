# init(exactly:)

**Framework**: Swift  
**Kind**: init

Creates a new value, if the given integer can be represented exactly.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init?<Source>(exactly value: Source) where Source : BinaryInteger
```

#### Discussion

If the given integer cannot be represented exactly, the result is `nil`.

## Parameters

- `value`: The integer to convert to a floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/init(exactly:)-2t92j)*