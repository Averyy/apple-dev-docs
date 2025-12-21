# receiveCompletion

**Framework**: Combine  
**Kind**: property

The closure to execute on completion.

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
final var receiveCompletion: (Subscribers.Completion<Failure>) -> Void { get }
```

## See Also

- [var receiveValue: (Input) -> Void](subscribers/sink/receivevalue.md)
  The closure to execute on receipt of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/sink/receivecompletion)*