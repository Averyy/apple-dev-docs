# append(copying:)

**Framework**: Swift  
**Kind**: method

Copies the elements of a sequence to the end of this array.

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
mutating func append(copying newElements: some Sequence<Element>)
```

#### Discussion

If the array does not have sufficient capacity to hold enough elements, then this reallocates the array’s storage to extend its capacity, using a geometric growth rate. If the input sequence does not provide a precise estimate of its count, then the array’s storage may need to be resized more than once.

> **Note**: O(*m*), where *m* is the length of `newElements`, when amortized over many invocations over the same array.

## Parameters

- `newElements`: The new elements to copy into the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/append(copying:)-7ntgb)*