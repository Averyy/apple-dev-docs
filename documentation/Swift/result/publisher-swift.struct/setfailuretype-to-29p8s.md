# setFailureType(to:)

**Framework**: Swift  
**Kind**: method

Changes the failure type declared by the upstream publisher.

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
func setFailureType<E>(to failureType: E.Type) -> Publishers.SetFailureType<Self, E> where E : Error
```

#### Return Value

A publisher that appears to send the specified failure type.

#### Discussion

Use [`setFailureType(to:)`](result/publisher-swift.struct/setfailuretype(to:).md) when you need set the error type of a publisher that cannot fail.

Conversely, if the upstream can fail, you would use [`mapError(_:)`](result/publisher-swift.struct/maperror(_:).md) to provide instructions on converting the error types to needed by the downstream publisher’s inputs.

The following example has two publishers with mismatched error types: `pub1`’s error type is [`Never`](Never.md), and `pub2`’s error type is [`Error`](Error.md). Because of the mismatch, the [`combineLatest(_:)`](result/publisher-swift.struct/combinelatest(_:).md) operator requires that `pub1` use [`setFailureType(to:)`](result/publisher-swift.struct/setfailuretype(to:).md) to make it appear that `pub1` can produce the [`Error`](Error.md) type, like `pub2` can.

```swift
let pub1 = [0, 1, 2, 3, 4, 5].publisher
let pub2 = CurrentValueSubject<Int, Error>(0)
let cancellable = pub1
    .setFailureType(to: Error.self)
    .combineLatest(pub2)
    .sink(
        receiveCompletion: { print ("completed: \($0)") },
        receiveValue: { print ("value: \($0)")}
     )

// Prints: "value: (5, 0)".
```

## Parameters

- `failureType`: The   type presented by this publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/setfailuretype(to:)-29p8s)*