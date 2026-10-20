# share

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A reference to the CloudKit share record used by the CloudKit sharing controller.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var share: CKShare? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) CKShare * share;
```

#### Discussion

This property provides a reference to the [`CKShare`](../../CloudKit/ckshare.md) record used by [`UICloudSharingController`](../uicloudsharingcontroller.md). The property is `nil` if the controller doesn’t have a share record. This can happen when the controller is initialized with the [`init(preparationHandler:)`](./init%28preparationhandler%29.md) method and the preparation handler hasn’t yet been called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/share)*