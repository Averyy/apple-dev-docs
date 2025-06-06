# init(exactly:)

**Framework**: Swift  
**Kind**: init  
**Required**: Yes

Creates a new value, if the given integer can be represented exactly.

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
init?<Source>(exactly value: Source) where Source : BinaryInteger
```

#### Discussion

If the given integer cannot be represented exactly, the result is `nil`.

## Parameters

- `value`: The integer to convert to a floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floatingpoint/init(exactly:))*