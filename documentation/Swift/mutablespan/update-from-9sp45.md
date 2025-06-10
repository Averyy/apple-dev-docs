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
mutating func update<S>(from source: S) -> (unwritten: S.Iterator, index: MutableSpan<Element>.Index) where Element == S.Element, S : Sequence
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablespan/update(from:)-9sp45)*