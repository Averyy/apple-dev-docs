# remove(at:)

**Framework**: Swift  
**Kind**: method

Removes and returns the element at the specified position.

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
@discardableResult
mutating func remove(at index: Int) -> Element
```

#### Return Value

The removed element.

#### Discussion

All the elements following the specified position are moved to close the gap.

> **Note**: O(`self.count`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/remove(at:))*