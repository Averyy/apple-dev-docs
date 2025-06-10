# dropFirst(_:)

**Framework**: Swift  
**Kind**: method

Omits the specified number of elements before republishing subsequent elements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func dropFirst(_ count: Int = 1) -> Publishers.Drop<Self>
```

#### Return Value

A publisher that doesn’t republish the first `count` elements.

#### Discussion

Use [`dropFirst(_:)`](result/publisher-swift.struct/dropfirst(_:).md) when you want to drop the first `n` elements from the upstream publisher, and republish the remaining elements.

The example below drops the first five elements from the stream:

```swift
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cancellable = numbers.publisher
    .dropFirst(5)
    .sink { print("\($0)", terminator: " ") }

// Prints: "6 7 8 9 10 "
```

## Parameters

- `count`: The number of elements to omit. The default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/dropfirst(_:))*