# hide()

**Framework**: AppKit  
**Kind**: method

Attempts to hide or the application.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func hide() -> Bool
```

## Mentions

- [Passing control from one app to another with cooperative activation](passing-control-from-one-app-to-another-with-cooperative-activation.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the application was successfully hidden, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The property of this value will be [`false`](https://developer.apple.com/documentation/swift/false) if the application has already quit, or if of a type that is unable to be hidden.

## See Also

- [func unhide() -> Bool](nsrunningapplication/unhide.md)
  Attempts to unhide or the application.
- [var isHidden: Bool](nsrunningapplication/ishidden.md)
  Indicates whether the application is currently hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/hide())*