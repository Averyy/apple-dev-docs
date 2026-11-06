# cloudSharingControllerDelegate

**Framework**: Shared with You  
**Kind**: property  
**Role**: Instance Property

The delegate for the sharing controller that the button that manages the share presents.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
weak var cloudSharingControllerDelegate: (any UICloudSharingControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UICloudSharingControllerDelegate> cloudSharingControllerDelegate;
```

## Discussion

The item holds the delegate weakly, and the value can be `nil`. Keep a strong reference to the delegate elsewhere in your app.

The delegate receives callbacks from the [`UICloudSharingController`](../../UIKit/uicloudsharingcontroller.md) that the built-in manage share button presents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationbarbuttonitem/cloudsharingcontrollerdelegate)*