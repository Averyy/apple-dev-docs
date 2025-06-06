# send()

**Framework**: Combine  
**Kind**: method

Sends a void value to the subscriber.

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
func send()
```

## Mentions

- [Using Combine for Your App’s Asynchronous Code](using-combine-for-your-app-s-asynchronous-code.md)

#### Discussion

Use `Void` inputs and outputs when you want to signal that an event has occurred, but don’t need to send the event itself.

## See Also

- [func send(Self.Output)](subject/send(_:).md)
  Sends a value to the subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subject/send())*