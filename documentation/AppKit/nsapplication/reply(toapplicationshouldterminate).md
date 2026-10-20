# reply(toApplicationShouldTerminate:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Responds to `NSTerminateLater` once the app knows whether it can terminate.

**Availability**:
- macOS

## Declaration

```swift
func reply(toApplicationShouldTerminate shouldTerminate: Bool)
```

```objc
- (void) replyToApplicationShouldTerminate:(BOOL) shouldTerminate;
```

#### Discussion

If your app delegate returns `NSTerminateLater` from its [`applicationShouldTerminate(_:)`](../nsapplicationdelegate/applicationshouldterminate%28_%29.md) method, your code must subsequently call this method to let the `NSApplication` object know whether it can actually terminate itself.

## Parameters

- `shouldTerminate`: Specify [`true`](../../Swift/true.md) if you want the app to terminate; otherwise, specify [`false`](../../Swift/false.md).

## See Also

### Terminating the app
- [func terminate(Any?)](./terminate%28_%29.md)
  Terminates the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/reply(toapplicationshouldterminate:))*