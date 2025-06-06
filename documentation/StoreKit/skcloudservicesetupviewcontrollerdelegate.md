# SKCloudServiceSetupViewControllerDelegate

**Framework**: StoreKit  
**Kind**: protocol

A protocol that defines the methods a cloud service setup view controller can use to get the status of the view, including when it is dismissed.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol SKCloudServiceSetupViewControllerDelegate : NSObjectProtocol
```

## Topics

### Receiving Notification of Dismissal
- [func cloudServiceSetupViewControllerDidDismiss(SKCloudServiceSetupViewController)](skcloudservicesetupviewcontrollerdelegate/cloudservicesetupviewcontrollerdiddismiss(_:).md)
  Tells the delegate that the cloud service setup view controller was dismissed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any SKCloudServiceSetupViewControllerDelegate)?](skcloudservicesetupviewcontroller/delegate.md)
  The cloud service view controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicesetupviewcontrollerdelegate)*