# skip(by:)

**Framework**: Swift  
**Kind**: method

Advances the position of this iterator by the specified offset, or until the end of the underlying type’s elements.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
mutating func skip(by offset: Int) throws(Self.Failure) -> Int
```

#### Return Value

The number of items that were skipped. If the returned count is less than `maxOffset`, then the underlying type did not have enough elements left to skip the requested number of items. In that case, the iterator’s position is set to the end of the underlying type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/borrowingiteratoradapter/skip(by:))*