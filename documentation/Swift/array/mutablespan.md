# mutableSpan

**Framework**: Swift  
**Kind**: property

A mutable span over the elements of this array.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var mutableSpan: MutableSpan<Element> { mutating get }
```

#### Return Value

A `MutableSpan` over the elements of this array.

#### Discussion

> **Note**: O(1) when the array’s storage is uniquely referenced, O(*n*) otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/mutablespan)*