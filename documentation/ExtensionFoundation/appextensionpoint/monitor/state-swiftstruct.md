# AppExtensionPoint.Monitor.State

**Framework**: ExtensionFoundation  
**Kind**: struct

The snapshot of the current Monitor state

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.1+
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct State
```

## Topics

### Instance Properties
- [var disabledCount: Int](appextensionpoint/monitor/state-swift.struct/disabledcount.md)
  The count of disabled app extensions that are bound to the monitored app extension points.
- [var identities: [AppExtensionIdentity]](appextensionpoint/monitor/state-swift.struct/identities.md)
  An array of `AppExtensionIdentity` objects representing available app extensions bound to the monitored app extension points.
- [var unapprovedCount: Int](appextensionpoint/monitor/state-swift.struct/unapprovedcount.md)
  The count of unapproved app extensions that are bound to the monitored app extension points.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/monitor/state-swift.struct)*