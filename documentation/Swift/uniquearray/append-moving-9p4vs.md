# append(moving:)

**Framework**: Swift  
**Kind**: method

Moves the elements of a output span to the end of this array, leaving the span empty.

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
mutating func append(moving items: inout OutputSpan<Element>)
```

#### Discussion

If the array does not have sufficient capacity to hold all new items, then this reallocates the array’s storage to grow its capacity, using a geometric growth rate.

> **Note**: O(`items.count`)

## Parameters

- `items`: An output span whose contents need to be appended to this array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/append(moving:)-9p4vs)*