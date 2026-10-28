# hide()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Attempts to hide or the application.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func hide() -> Bool
```

```objc
- (BOOL) hide;
```

## Mentions

- [Passing control from one app to another with cooperative activation](../passing-control-from-one-app-to-another-with-cooperative-activation.md)

## Return Value

[`true`](../../Swift/true.md) if the application was successfully hidden, otherwise [`false`](../../Swift/false.md).

## Discussion

The property of this value will be [`false`](../../Swift/false.md) if the application has already quit, or if of a type that is unable to be hidden.

## See Also

### Hiding and unhiding applications
- [func unhide() -> Bool](./unhide%28%29.md)
  Attempts to unhide or the application.
- [var isHidden: Bool](./ishidden.md)
  Indicates whether the application is currently hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/hide())*