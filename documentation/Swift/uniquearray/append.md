# append(_:)

**Framework**: Swift  
**Kind**: method

Adds an element to the end of the array.

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
mutating func append(_ item: consuming Element)
```

#### Discussion

If the array does not have sufficient capacity to hold any more elements, then this reallocates the array’s storage to grow its capacity, using a geometric growth rate.

> **Note**: O(1) as amortized over many invocations on the same array.

## Parameters

- `item`: The element to append to the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/append(_:))*