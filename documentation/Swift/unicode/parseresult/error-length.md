# Unicode.ParseResult.error(length:)

**Framework**: Swift  
**Kind**: case

An encoding error was detected.

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
case error(length: Int)
```

#### Discussion

`length` is the number of underlying code units consumed by this error, guaranteed to be greater than 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/parseresult/error(length:))*