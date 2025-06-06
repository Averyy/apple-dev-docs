# NWConnection.SendCompletion.contentProcessed(_:)

**Framework**: Network  
**Kind**: case

Provide a completion handler that’s invoked when the sent data is processed by the stack.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@preconcurrency
case contentProcessed((NWError?) -> Void)
```

## See Also

- [NWConnection.SendCompletion.idempotent](nwconnection/sendcompletion/idempotent.md)
  Mark the sent data as idempotent—data that can be sent multiple times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/sendcompletion/contentprocessed(_:))*