# isProtectedDataAvailable

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether content protection is active.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
nonisolated
var isProtectedDataAvailable: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isProtectedDataAvailable) BOOL protectedDataAvailable;
```

## Discussion

The value of this property is [`false`](../../Swift/false.md) if data protection is enabled and the device is currently locked. The value of this property is set to [`true`](../../Swift/true.md) if the device is unlocked or if content protection is not enabled.

When the value of this property is [`false`](../../Swift/false.md), files that were assigned the [`complete`](../../Foundation/fileprotectiontype/complete.md) or [`completeUnlessOpen`](../../Foundation/fileprotectiontype/completeunlessopen.md) protection key cannot be read or written by your app. The user must unlock the device before your app can access them.

## See Also

### Accessing protected content
- [class let protectedDataDidBecomeAvailableNotification: NSNotification.Name](./protecteddatadidbecomeavailablenotification.md)
  A notification that posts when the protected files become available for your code to access.
- [class let protectedDataWillBecomeUnavailableNotification: NSNotification.Name](./protecteddatawillbecomeunavailablenotification.md)
  A notification that posts shortly before protected files are locked down and become inaccessible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/isprotecteddataavailable)*