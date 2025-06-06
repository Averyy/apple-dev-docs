# value

**Framework**: Combine  
**Kind**: property

The published value of the future or an error, delivered asynchronously.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
final var value: Output { get async throws }
```

#### Discussion

This property subscribes to the `Future` and delivers the value asynchronously when the `Future` publishes it. If the `Future` terminates with an error, the awaiting caller receives the error instead. Use this property when you want to the `async`-`await` syntax with a `Future` whose [`Failure`](publisher/failure.md) type is not [`Never`](https://developer.apple.com/documentation/Swift/Never).

## See Also

- [var value: Output](future/value-9iwjz.md)
  The published value of the future, delivered asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/future/value-5iprp)*