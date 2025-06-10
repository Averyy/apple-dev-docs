# tryPrefix(while:)

**Framework**: Swift  
**Kind**: method

Republishes elements while an error-throwing predicate closure indicates publishing should continue.

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
func tryPrefix(while predicate: @escaping (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>
```

#### Return Value

A publisher that passes through elements until the predicate throws or indicates publishing should finish.

#### Discussion

Use [`tryPrefix(while:)`](optional/publisher-swift.struct/tryprefix(while:).md) to emit values from the upstream publisher that meet a condition you specify in an error-throwing closure. The publisher finishes when the closure returns `false`. If the closure throws an error, the publisher fails with that error.

```swift
struct OutOfRangeError: Error {}

let numbers = (0...10).reversed()
cancellable = numbers.publisher
    .tryPrefix {
        guard $0 != 0 else {throw OutOfRangeError()}
        return $0 <= numbers.max()!
    }
    .sink(
        receiveCompletion: { print ("completion: \($0)", terminator: " ") },
        receiveValue: { print ("\($0)", terminator: " ") }
    )

// Prints: "10 9 8 7 6 5 4 3 2 1 completion: failure(OutOfRangeError()) "
```

## Parameters

- `predicate`: A closure that takes an element as its parameter and returns a Boolean value indicating whether publishing should continue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/tryprefix(while:))*