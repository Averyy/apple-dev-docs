# skip(by:)

**Framework**: Swift  
**Kind**: method

Advances the position of this iterator by the specified offset, or until the end of the underlying type’s elements.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
mutating func skip(by offset: Int) -> Int
```

#### Return Value

The number of items that were skipped. If the returned count is less than `maximumOffset`, then the underlying type did not have enough elements left to skip the requested number of items. In that case, the iterator’s position is set to the end of the underlying type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/borrowingiteratoradapter/skip(by:))*