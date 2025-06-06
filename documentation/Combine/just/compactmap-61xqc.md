# compactMap(_:)

**Framework**: Combine  
**Kind**: method

Calls a closure with each received element and publishes any returned optional that has a value.

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
func compactMap<T>(_ transform: @escaping (Self.Output) -> T?) -> Publishers.CompactMap<Self, T>
```

#### Return Value

Any non-`nil` optional results of the calling the supplied closure.

#### Discussion

Combine’s [`compactMap(_:)`](publisher/compactmap(_:).md) operator performs a function similar to that of [`compactMap(_:)`](https://developer.apple.com/documentation/Swift/Sequence/compactMap(_:)) in the Swift standard library: the [`compactMap(_:)`](publisher/compactmap(_:).md) operator in Combine removes `nil` elements in a publisher’s stream and republishes non-`nil` elements to the downstream subscriber.

The example below uses a range of numbers as the source for a collection based publisher. The [`compactMap(_:)`](publisher/compactmap(_:).md) operator consumes each element from the `numbers` publisher attempting to access the dictionary using the element as the key. If the example’s dictionary returns a `nil`, due to a non-existent key, [`compactMap(_:)`](publisher/compactmap(_:).md) filters out the `nil` (missing) elements.

```swift
let numbers = (0...5)
let romanNumeralDict: [Int : String] =
    [1: "I", 2: "II", 3: "III", 5: "V"]

cancellable = numbers.publisher
    .compactMap { romanNumeralDict[$0] }
    .sink { print("\($0)", terminator: " ") }

// Prints: "I II III V"
```

## Parameters

- `transform`: A closure that receives a value and returns an optional value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/compactmap(_:)-61xqc)*