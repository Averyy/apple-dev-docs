# filter(_:)

**Framework**: Swift  
**Kind**: method

Republishes all elements that match a provided closure.

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
func filter(_ isIncluded: @escaping (Self.Output) -> Bool) -> Publishers.Filter<Self>
```

#### Return Value

A publisher that republishes all elements that satisfy the closure.

#### Discussion

Combine’s [`filter(_:)`](result/publisher-swift.struct/filter(_:).md) operator performs an operation similar to that of [`filter(_:)`](Sequence/filter(_:)-5y9d2.md) in the Swift Standard Library: it uses a closure to test each element to determine whether to republish the element to the downstream subscriber.

The following example, uses a filter operation that receives an `Int` and only republishes a value if it’s even.

```swift
let numbers: [Int] = [1, 2, 3, 4, 5]
cancellable = numbers.publisher
    .filter { $0 % 2 == 0 }
    .sink { print("\($0)", terminator: " ") }

// Prints: "2 4"
```

## Parameters

- `isIncluded`: A closure that takes one element and returns a Boolean value indicating whether to republish the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/filter(_:))*