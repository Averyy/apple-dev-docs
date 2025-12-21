# state

**Framework**: ExtensionFoundation  
**Kind**: property

The current details about the available, disabled, and unapproved extensions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 1.1+
- watchOS 26.0+

## Declaration

```swift
final var state: AppExtensionPoint.Monitor.State { get }
```

## Mentions

- [Discovering app extensions from your app](discovering-app-extensions-from-your-app.md)

#### Discussion

This property provides the list of available app extensions plus the number of currently disabled and unapproved extensions. The property is observable, so you can monitor it for changes while your app runs.

## See Also

- [AppExtensionPoint.Monitor.State](appextensionpoint/monitor/state-swift.struct.md)
  A type that contains a snapshot of a monitor’s state information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/monitor/state-swift.property)*