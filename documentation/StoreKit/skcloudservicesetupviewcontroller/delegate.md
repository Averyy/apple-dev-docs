# delegate

**Framework**: StoreKit  
**Kind**: property

The cloud service view controller’s delegate.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
weak var delegate: (any SKCloudServiceSetupViewControllerDelegate)? { get set }
```

#### Discussion

You can identify a delegate to get informed when the cloud service setup view controller is dismissed.

## See Also

- [protocol SKCloudServiceSetupViewControllerDelegate](skcloudservicesetupviewcontrollerdelegate.md)
  A protocol that defines the methods a cloud service setup view controller can use to get the status of the view, including when it is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicesetupviewcontroller/delegate)*