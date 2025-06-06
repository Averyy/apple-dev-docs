# prefix(while:)

**Framework**: Combine  
**Kind**: method

Republishes elements while a predicate closure indicates publishing should continue.

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
func prefix(while predicate: @escaping (Self.Output) -> Bool) -> Publishers.PrefixWhile<Self>
```

#### Return Value

A publisher that passes through elements until the predicate indicates publishing should finish.

#### Discussion

Use [`prefix(while:)`](publisher/prefix(while:).md) to emit values while elements from the upstream publisher meet a condition you specify. The publisher finishes when the closure returns `false`.

In the example below, the [`prefix(while:)`](publisher/prefix(while:).md) operator emits values while the element it receives is less than five:

```swift
let numbers = (0...10)
numbers.publisher
    .prefix { $0 < 5 }
    .sink { print("\($0)", terminator: " ") }

// Prints: "0 1 2 3 4"
```

## Parameters

- `predicate`: A closure that takes an element as its parameter and returns a Boolean value that indicates whether publishing should continue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/prefix(while:)-1k391)*