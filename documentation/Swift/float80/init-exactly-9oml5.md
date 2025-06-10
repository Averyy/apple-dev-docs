# init(exactly:)

**Framework**: Swift  
**Kind**: init

Creates a new instance from the given value, if it can be represented exactly.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init?<Source>(exactly value: Source) where Source : BinaryFloatingPoint
```

#### Discussion

If the given floating-point value cannot be represented exactly, the result is `nil`.

## Parameters

- `value`: A floating-point value to be converted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/init(exactly:)-9oml5)*