# delegate

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The cloud service view controller’s delegate.

**Availability**:
- iOS 10.1+ - Deprecated in 18.0
- iPadOS 10.1+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0

> **Deprecated**: Use the musicSubscriptionOffer(isPresented:options:onLoadCompletion:) SwiftUI View Modifier from MusicKit.

## Declaration

```swift
weak var delegate: (any SKCloudServiceSetupViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<SKCloudServiceSetupViewControllerDelegate> delegate;
```

#### Discussion

You can identify a delegate to get informed when the cloud service setup view controller is dismissed.

## See Also

### Setting a delegate
- [protocol SKCloudServiceSetupViewControllerDelegate](../skcloudservicesetupviewcontrollerdelegate.md)
  A protocol that defines the methods a cloud service setup view controller can use to get the status of the view, including when it is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicesetupviewcontroller/delegate)*