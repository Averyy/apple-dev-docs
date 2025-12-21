# init(_:)

**Framework**: Combine  
**Kind**: init

Initializes the cancellable object with the given cancel-time closure.

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
init(_ cancel: @escaping () -> Void)
```

## Parameters

- `cancel`: A closure that the   method executes.

## See Also

- [init<C>(C)](anycancellable/init(_:)-48fh3.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/anycancellable/init(_:)-3icn3)*