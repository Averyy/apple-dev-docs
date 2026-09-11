# append(copying:)

**Framework**: Swift  
**Kind**: method

Copies the elements of a span to the end of this array.

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
mutating func append(copying newElements: Span<Element>)
```

#### Discussion

If the array does not have sufficient capacity to hold enough elements, then this reallocates the array’s storage to extend its capacity, using a geometric growth rate.

> **Note**: O(`newElements.count`) when amortized over many invocations on the same array.

## Parameters

- `newElements`: A span whose contents to copy into the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/append(copying:)-3aouw)*