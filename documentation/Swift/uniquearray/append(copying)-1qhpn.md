# append(copying:)

**Framework**: Swift  
**Kind**: method

Copies the elements of a buffer to the end of this array.

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
mutating func append(copying newElements: UnsafeBufferPointer<Element>)
```

#### Discussion

If the array does not have sufficient capacity to hold all items in the source buffer, then this automatically grows the array’s capacity, using a geometric growth rate.

> **Note**: O(`newElements.count`) when amortized over many invocations on the same array.

## Parameters

- `newElements`: A fully initialized buffer whose contents to copy into the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/append(copying:)-1qhpn)*