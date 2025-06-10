# update(from:)

**Framework**: Swift  
**Kind**: method

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.1+
- watchOS 5.2+

## Declaration

```swift
mutating func update<S>(from source: S) -> (unwritten: S.Iterator, byteOffset: Int) where S : Sequence, S.Element : BitwiseCopyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablerawspan/update(from:)-16nqv)*