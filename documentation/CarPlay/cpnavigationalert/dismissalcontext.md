# CPNavigationAlert.DismissalContext

**Framework**: CarPlay  
**Kind**: enum

A set of reasons for dismissing a navigation alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum DismissalContext
```

## Topics

### Dismissal Reasons
- [CPNavigationAlert.DismissalContext.timeout](cpnavigationalert/dismissalcontext/timeout.md)
  The system dismissed the navigation alert due to a timeout.
- [CPNavigationAlert.DismissalContext.systemDismissed](cpnavigationalert/dismissalcontext/systemdismissed.md)
  The system dismissed the navigation alert.
- [CPNavigationAlert.DismissalContext.userDismissed](cpnavigationalert/dismissalcontext/userdismissed.md)
  The user dismissed the navigation alert.
### Initializers
- [init?(rawValue: UInt)](cpnavigationalert/dismissalcontext/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func mapTemplate(CPMapTemplate, willShow: CPNavigationAlert)](cpmaptemplatedelegate/maptemplate(_:willshow:).md)
  Tells the delegate that the system will show the navigation alert.
- [func mapTemplate(CPMapTemplate, didShow: CPNavigationAlert)](cpmaptemplatedelegate/maptemplate(_:didshow:).md)
  Tells the delegate that the system showed the navigation alert.
- [func mapTemplate(CPMapTemplate, willDismiss: CPNavigationAlert, dismissalContext: CPNavigationAlert.DismissalContext)](cpmaptemplatedelegate/maptemplate(_:willdismiss:dismissalcontext:).md)
  Tells the delegate that the system is preparing to dismiss the navigation alert.
- [func mapTemplate(CPMapTemplate, didDismiss: CPNavigationAlert, dismissalContext: CPNavigationAlert.DismissalContext)](cpmaptemplatedelegate/maptemplate(_:diddismiss:dismissalcontext:).md)
  Tells the delegate that the system dismissed the navigation alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/dismissalcontext)*