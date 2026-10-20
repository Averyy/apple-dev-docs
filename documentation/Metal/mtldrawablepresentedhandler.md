# MTLDrawablePresentedHandler

**Framework**: Metal  
**Kind**: typealias  
**Role**: Type Alias

A block of code invoked after a drawable is presented.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias MTLDrawablePresentedHandler = @Sendable (any MTLDrawable) -> Void
```

```c
typedef void (^)(id<MTLDrawable>) MTLDrawablePresentedHandler;
```

## See Also

### Render pass outputs
- [protocol MTLDrawable](./mtldrawable.md)
  A displayable resource that can be rendered or written to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldrawablepresentedhandler)*