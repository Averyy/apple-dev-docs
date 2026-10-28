# openAppWhenRun

**Framework**: App Intents  
**Kind**: property  
**Role**: Type Property  
**Required**: Yes

A Boolean property that tells the system to consider the app intent even if its app is not in the foreground.

**Availability**:
- iOS 16.0+ - Deprecated in 26.0
- iPadOS 16.0+ - Deprecated in 26.0
- Mac Catalyst 16.0+ - Deprecated in 26.0
- macOS 13.0+ - Deprecated in 26.0
- tvOS 16.0+ - Deprecated in 26.0
- visionOS - Deprecated in 26.0
- watchOS 9.0+ - Deprecated in 26.0

> **Deprecated**: Please provide 'supportedModes' instead

## Declaration

```swift
static var openAppWhenRun: Bool { get }
```

## Mentions

- [Responding to the Action button on Apple Watch Ultra](../actionbuttonarticle.md)

## Discussion

This property is deprecated. Use [`supportedModes`](./supportedmodes.md) instead. Setting this property to `true` generates an error if the app intent runs in an app extension. For backward compatability, you can set this property to `true` for app intents you run inside your app. For example:

```swift
@available(*, deprecated)
extension OrderSoupIntent {
    static var openAppWhenRun: Bool { true }
}
```

## Default Implementations

### AppIntent Implementations
- [static var openAppWhenRun: Bool](./openappwhenrun-223b1.md)
  A Boolean property that tells the system to consider the app intent even if its app is not in the foreground.
- [static var openAppWhenRun: Bool](./openappwhenrun-3ej7y.md)
  A Boolean property that tells the system to consider the app intent even if its app is not in the foreground.
- [static var openAppWhenRun: Bool](./openappwhenrun-475kn.md)
  A Boolean property that tells the system to consider the app intent even if its app is not in the foreground.
- [static var openAppWhenRun: Bool](./openappwhenrun-5iruo.md)
  A Boolean value that defines the presentation style for the intent.
- [static var openAppWhenRun: Bool](./openappwhenrun-7ggw4.md)
  A Boolean property that tells the system to consider the app intent even if its app is not in the foreground.

## See Also

### Deprecated
- [func requestConfirmation<Result>(result: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](./requestconfirmation%28result,confirmationactionname,showprompt%29.md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation<Result>(output: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](./requestconfirmation%28output,confirmationactionname,showprompt%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/openappwhenrun)*