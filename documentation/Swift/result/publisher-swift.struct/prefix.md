# prefix(_:)

**Framework**: Swift  
**Kind**: method

Republishes elements up to the specified maximum count.

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
func prefix(_ maxLength: Int) -> Publishers.Output<Self>
```

#### Return Value

A publisher that publishes up to the specified number of elements.

#### Discussion

Use [`prefix(_:)`](result/publisher-swift.struct/prefix(_:).md) to limit the number of elements republished to the downstream subscriber.

In the example below, the [`prefix(_:)`](result/publisher-swift.struct/prefix(_:).md) operator limits its output to the first two elements before finishing normally:

```swift
let numbers = (0...10)
cancellable = numbers.publisher
    .prefix(2)
    .sink { print("\($0)", terminator: " ") }

// Prints: "0 1"
```

## Parameters

- `maxLength`: The maximum number of elements to republish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/prefix(_:))*