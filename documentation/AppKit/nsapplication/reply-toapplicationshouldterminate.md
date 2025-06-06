# reply(toApplicationShouldTerminate:)

**Framework**: AppKit  
**Kind**: method

Responds to `NSTerminateLater` once the app knows whether it can terminate.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func reply(toApplicationShouldTerminate shouldTerminate: Bool)
```

#### Discussion

If your app delegate returns `NSTerminateLater` from its [`applicationShouldTerminate(_:)`](nsapplicationdelegate/applicationshouldterminate(_:).md) method, your code must subsequently call this method to let the `NSApplication` object know whether it can actually terminate itself.

## Parameters

- `shouldTerminate`: Specify   if you want the app to terminate; otherwise, specify  .

## See Also

- [func terminate(Any?)](nsapplication/terminate(_:).md)
  Terminates the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/reply(toapplicationshouldterminate:))*