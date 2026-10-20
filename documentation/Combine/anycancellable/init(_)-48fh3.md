# init(_:)

**Framework**: Combine  
**Kind**: init  
**Role**: Initializer

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
init<C>(_ canceller: C) where C : Cancellable
```

## See Also

### Creating a type-erased cancellable
- [init(() -> Void)](./init%28_%29-3icn3.md)
  Initializes the cancellable object with the given cancel-time closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/anycancellable/init(_:)-48fh3)*