# tryFilter(_:)

**Framework**: Swift  
**Kind**: method

Republishes all elements that match a provided error-throwing closure.

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
func tryFilter(_ isIncluded: @escaping (Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>
```

#### Return Value

A publisher that republishes all elements that satisfy the closure.

#### Discussion

Use [`tryFilter(_:)`](result/publisher-swift.struct/tryfilter(_:).md) to filter elements evaluated in an error-throwing closure. If the `isIncluded` closure throws an error, the publisher fails with that error.

In the example below, [`tryFilter(_:)`](result/publisher-swift.struct/tryfilter(_:).md) checks to see if the element provided by the publisher is zero, and throws a `ZeroError` before terminating the publisher with the thrown error. Otherwise, it republishes the element only if it’s even:

```swift
struct ZeroError: Error {}

let numbers: [Int] = [1, 2, 3, 4, 0, 5]
cancellable = numbers.publisher
    .tryFilter{
        if $0 == 0 {
            throw ZeroError()
        } else {
            return $0 % 2 == 0
        }
    }
    .sink(
        receiveCompletion: { print ("\($0)") },
        receiveValue: { print ("\($0)", terminator: " ") }
     )

// Prints: "2 4 failure(DivisionByZeroError())".
```

## Parameters

- `isIncluded`: A closure that takes one element and returns a Boolean value that indicated whether to republish the element or throws an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/tryfilter(_:))*