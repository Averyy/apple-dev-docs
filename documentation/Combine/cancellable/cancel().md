# cancel()

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Cancel the activity.

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
func cancel()
```

## Mentions

- [Receiving and Handling Events with Combine](../receiving-and-handling-events-with-combine.md)
- [Controlling Publishing with Connectable Publishers](../controlling-publishing-with-connectable-publishers.md)

#### Discussion

When implementing [`Cancellable`](../cancellable.md) in support of a custom publisher, implement `cancel()` to request that your publisher stop calling its downstream subscribers. Combine doesn’t require that the publisher stop immediately, but the `cancel()` call should take effect quickly. Canceling should also eliminate any strong references it currently holds.

After you receive one call to `cancel()`, subsequent calls shouldn’t do anything. Additionally, your implementation must be thread-safe, and it shouldn’t block the caller.

> 💡 **Tip**: Keep in mind that your `cancel()` may execute concurrently with another call to `cancel()` — including the scenario where an [`AnyCancellable`](../anycancellable.md) is deallocating — or to [`request(_:)`](../subscription/request%28_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/cancellable/cancel())*