# shared

**Framework**: PermissionKit  
**Kind**: property

The shared instance you use to send permission requests and receive responses.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- macOS 26.1+
- visionOS 26.2+

## Declaration

```swift
static let shared: AskCenter
```

#### Overview

Use this singleton instance to access all [`AskCenter`](askcenter.md) functionality. The system maintains this shared instance across your app’s lifecycle and ensures consistent handling of permission requests and responses.

```swift
 let center = AskCenter.shared
 try await center.ask(permissionQuestion)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/askcenter/shared)*