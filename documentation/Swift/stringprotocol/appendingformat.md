# appendingFormat(_:_:)

**Framework**: Swift  
**Kind**: method

Returns a string created by appending a string constructed from a given format string and the following arguments.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func appendingFormat<T>(_ format: T, _ arguments: any CVarArg...) -> String where T : StringProtocol
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/appendingformat(_:_:))*