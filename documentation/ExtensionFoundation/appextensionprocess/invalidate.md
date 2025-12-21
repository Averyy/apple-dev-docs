# invalidate()

**Framework**: ExtensionFoundation  
**Kind**: method

Invalidates the host app’s connection to the app extension process.

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
func invalidate()
```

## Mentions

- [Adding support for app extensions to your app](adding-support-for-app-extensions-to-your-app.md)

#### Discussion

Call this method when you finish communicating with an app extension and no longer need it. If the current object represents the last connection to the app extension, the system terminates the app extension’s process. After calling this method, don’t try to communicate with the app extension using XPC. Instead, remove any references to the app extension and release this `AppExtensionProcess` type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess/invalidate())*