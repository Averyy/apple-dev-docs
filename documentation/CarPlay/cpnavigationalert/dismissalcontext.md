# CPNavigationAlert.DismissalContext

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

A set of reasons for dismissing a navigation alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum DismissalContext
```

```c
enum CPNavigationAlertDismissalContext : NSUInteger;
```

## Topics

### Dismissal Reasons
- [CPNavigationAlert.DismissalContext.timeout](./dismissalcontext/timeout.md)
  The system dismissed the navigation alert due to a timeout.
- [CPNavigationAlert.DismissalContext.systemDismissed](./dismissalcontext/systemdismissed.md)
  The system dismissed the navigation alert.
- [CPNavigationAlert.DismissalContext.userDismissed](./dismissalcontext/userdismissed.md)
  The user dismissed the navigation alert.
### Initializers
- [init?(rawValue: UInt)](./dismissalcontext/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling Navigation Alerts
- [func mapTemplate(CPMapTemplate, willShow: CPNavigationAlert)](../cpmaptemplatedelegate/maptemplate%28_,willshow%29.md)
  Tells the delegate that the system will show the navigation alert.
- [func mapTemplate(CPMapTemplate, didShow: CPNavigationAlert)](../cpmaptemplatedelegate/maptemplate%28_,didshow%29.md)
  Tells the delegate that the system showed the navigation alert.
- [func mapTemplate(CPMapTemplate, willDismiss: CPNavigationAlert, dismissalContext: CPNavigationAlert.DismissalContext)](../cpmaptemplatedelegate/maptemplate%28_,willdismiss,dismissalcontext%29.md)
  Tells the delegate that the system is preparing to dismiss the navigation alert.
- [func mapTemplate(CPMapTemplate, didDismiss: CPNavigationAlert, dismissalContext: CPNavigationAlert.DismissalContext)](../cpmaptemplatedelegate/maptemplate%28_,diddismiss,dismissalcontext%29.md)
  Tells the delegate that the system dismissed the navigation alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/dismissalcontext)*