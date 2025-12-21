# appExtensionIdentity

**Framework**: ExtensionFoundation  
**Kind**: property

The identifying information for the app extension you want to launch.

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
var appExtensionIdentity: AppExtensionIdentity
```

#### Discussion

Specify this value at initialization time. Fetch identity information from the [`AppExtensionPoint.Monitor`](appextensionpoint/monitor.md) type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess/configuration/appextensionidentity)*