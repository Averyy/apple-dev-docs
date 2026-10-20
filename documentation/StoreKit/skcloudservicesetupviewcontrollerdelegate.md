# SKCloudServiceSetupViewControllerDelegate

**Framework**: StoreKit  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines the methods a cloud service setup view controller can use to get the status of the view, including when it is dismissed.

**Availability**:
- iOS 10.1+ - Deprecated in 18.0
- iPadOS 10.1+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0

> **Deprecated**: Use the musicSubscriptionOffer(isPresented:options:onLoadCompletion:) SwiftUI View Modifier from MusicKit.

## Declaration

```swift
protocol SKCloudServiceSetupViewControllerDelegate : NSObjectProtocol
```

```objc
@protocol SKCloudServiceSetupViewControllerDelegate <NSObject>
```

## Topics

### Receiving Notification of Dismissal
- [func cloudServiceSetupViewControllerDidDismiss(SKCloudServiceSetupViewController)](./skcloudservicesetupviewcontrollerdelegate/cloudservicesetupviewcontrollerdiddismiss%28_%29.md)
  Tells the delegate that the cloud service setup view controller was dismissed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Setting a delegate
- [var delegate: (any SKCloudServiceSetupViewControllerDelegate)?](./skcloudservicesetupviewcontroller/delegate.md)
  The cloud service view controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicesetupviewcontrollerdelegate)*