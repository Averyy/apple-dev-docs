# onInterruption

**Framework**: ExtensionFoundation  
**Kind**: property

The closure to run if the app extension’s process exits unexpectedly.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+
- tvOS 26.0+
- visionOS 1.1+
- watchOS 26.0+

## Declaration

```swift
var onInterruption: () -> Void
```

#### Discussion

Use your closure to respond to the loss of the app extension process. For example, use it to try and reestablish connection to the app extension or to remove the app extension from the list of active extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess/configuration/oninterruption)*