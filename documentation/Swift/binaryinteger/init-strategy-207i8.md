# init(_:strategy:)

**Framework**: Swift  
**Kind**: init

Initialize an instance by parsing `value` with the given `strategy`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init<S>(_ value: S.ParseInput, strategy: S) throws where S : ParseStrategy, S.ParseOutput : BinaryInteger
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryinteger/init(_:strategy:)-207i8)*