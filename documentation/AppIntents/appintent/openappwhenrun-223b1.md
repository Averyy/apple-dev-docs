# openAppWhenRun

**Framework**: App Intents  
**Kind**: property  
**Role**: Type Property

A Boolean property that tells the system to consider the app intent even if its app is not in the foreground.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS
- watchOS 10.2+

## Declaration

```swift
static var openAppWhenRun: Bool { get }
```

#### Discussion

This property is deprecated. Use [`supportedModes`](./supportedmodes.md) instead. Setting this property to `true` generates an error if the app intent runs in an app extension. For backward compatability, you can set this property to `true` for app intents you run inside your app. For example:

```swift
@available(*, deprecated)
extension OrderSoupIntent {
    static var openAppWhenRun: Bool { true }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/openappwhenrun-223b1)*