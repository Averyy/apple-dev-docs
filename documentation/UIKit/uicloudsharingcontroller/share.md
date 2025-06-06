# share

**Framework**: UIKit  
**Kind**: property

A reference to the CloudKit share record used by the CloudKit sharing controller.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var share: CKShare? { get }
```

#### Discussion

This property provides a reference to the [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) record used by [`UICloudSharingController`](uicloudsharingcontroller.md). The property is `nil` if the controller doesn’t have a share record. This can happen when the controller is initialized with the [`init(preparationHandler:)`](uicloudsharingcontroller/init(preparationhandler:).md) method and the preparation handler hasn’t yet been called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/share)*