# cloudServiceSetupViewControllerDidDismiss(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the cloud service setup view controller was dismissed.

**Availability**:
- iOS 10.1+ - Deprecated in 18.0
- iPadOS 10.1+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0

> **Deprecated**: Use the musicSubscriptionOffer(isPresented:options:onLoadCompletion:) SwiftUI View Modifier from MusicKit.

## Declaration

```swift
optional func cloudServiceSetupViewControllerDidDismiss(_ cloudServiceSetupViewController: SKCloudServiceSetupViewController)
```

```objc
- (void) cloudServiceSetupViewControllerDidDismiss:(SKCloudServiceSetupViewController *) cloudServiceSetupViewController;
```

## Parameters

- `cloudServiceSetupViewController`: The cloud service view controller that was dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicesetupviewcontrollerdelegate/cloudservicesetupviewcontrollerdiddismiss(_:))*