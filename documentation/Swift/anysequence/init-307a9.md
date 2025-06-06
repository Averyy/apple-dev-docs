# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new sequence that wraps and forwards operations to `base`.

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
init<S>(_ base: S) where Element == S.Element, S : Sequence
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anysequence/init(_:)-307a9)*