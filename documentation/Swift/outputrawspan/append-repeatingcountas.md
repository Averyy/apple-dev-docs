# append(repeating:count:as:)

**Framework**: Swift  
**Kind**: method

Appends the given value’s bytes repeatedly to this span’s bytes.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
mutating func append<T>(repeating repeatedValue: T, count: Int, as type: T.Type) where T : BitwiseCopyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/outputrawspan/append(repeating:count:as:))*