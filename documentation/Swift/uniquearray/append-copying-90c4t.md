# append(copying:)

**Framework**: Swift  
**Kind**: method

Copies the elements of a buffer to the end of this array.

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
mutating func append(copying newElements: UnsafeMutableBufferPointer<Element>)
```

#### Discussion

If the array does not have sufficient capacity to hold enough elements, then this reallocates the array’s storage to extend its capacity, using a geometric growth rate.

> **Note**: O(`newElements.count`) when amortized over many invocations on the same array.

## Parameters

- `newElements`: A fully initialized buffer whose contents to copy into the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/append(copying:)-90c4t)*