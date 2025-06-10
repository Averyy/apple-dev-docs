# scan(_:_:)

**Framework**: Swift  
**Kind**: method

Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.

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
func scan<T>(_ initialResult: T, _ nextPartialResult: @escaping (T, Self.Output) -> T) -> Publishers.Scan<Self, T>
```

#### Return Value

A publisher that transforms elements by applying a closure that receives its previous return value and the next element from the upstream publisher.

#### Discussion

Use [`scan(_:_:)`](result/publisher-swift.struct/scan(_:_:).md) to accumulate all previously-published values into a single value, which you then combine with each newly-published value.

The following example logs a running total of all values received from the sequence publisher.

```swift
let range = (0...5)
cancellable = range.publisher
    .scan(0) { return $0 + $1 }
    .sink { print ("\($0)", terminator: " ") }
 // Prints: "0 1 3 6 10 15 ".
```

## Parameters

- `initialResult`: The previous result returned by the   closure.
- `nextPartialResult`: A closure that takes as its arguments the previous value returned by the closure and the next element emitted from the upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/scan(_:_:)-6pykh)*