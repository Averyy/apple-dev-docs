# publisher

**Framework**: Swift  
**Kind**: property

A Combine publisher that publishes this instance’s value to each subscriber exactly once, if it has any value at all.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var publisher: Optional<Wrapped>.Publisher { get }
```

#### Discussion

In the following example, the publisher for an `Int?` optional publishes its value once, then finishes normally:

```swift
let optional1: Int? = 1
    optional1.publisher
        .sink(receiveCompletion: { print("optional1 completed.") },
              receiveValue: { print("optional1 = \($0)") }
        )

// Prints:
// optional1 = 1.
// optional1 completed.
```

In contrast with the [`Just`](https://developer.apple.com/documentation/Combine/Just) publisher, which always publishes a single value, this publisher might not send any values and instead finish normally if the optional’s `output` is `nil`. In the next example, an `Int?` optional that’s `nil` immediately sends the [`Subscribers.Completion.finished`](https://developer.apple.com/documentation/Combine/Subscribers/Completion/finished) completion, without producing any values.

```swift
let optional2: Int? = nil
optional2.publisher
        .sink(receiveCompletion: { print("optional2 completed.") },
              receiveValue: { print("optional2 = \($0)") }
        )

// Prints:
// optional2 completed.
```

## See Also

- [Optional.Publisher](optional/publisher-swift.struct.md)
  The type of a Combine publisher that publishes the value of a Swift optional instance to each subscriber exactly once, if the instance has any value at all.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.property)*