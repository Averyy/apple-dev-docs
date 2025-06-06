# NSBundleResourceRequestLowDiskSpace

**Framework**: Foundation  
**Kind**: property

Posted after the system detects that the amount of available disk space is getting low. The notification is posted to the default notification center.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let NSBundleResourceRequestLowDiskSpace: NSNotification.Name
```

#### Discussion

After receiving this notification, the app should release any on-demand resources that are not required. Call [`endAccessingResources()`](nsbundleresourcerequest/endaccessingresources().md) to release the managed resources. If the app is in the background and the app does not free up enough space, it may be terminated.

> **Note**:  This notification is generated independently of any other iOS notifications for low disk space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsbundleresourcerequestlowdiskspace)*