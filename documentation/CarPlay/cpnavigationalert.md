# CPNavigationAlert

**Framework**: CarPlay  
**Kind**: class

An alert that displays map- or navigation-related information to the user.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPNavigationAlert
```

#### Overview

To display a navigation alert, create an instance of [`CPNavigationAlert`](cpnavigationalert.md) and pass it to the map template’s [`present(navigationAlert:animated:)`](cpmaptemplate/present(navigationalert:animated:).md) method. When creating an alert, you must provide a title, action, and duration. The duration tells the system how long to show the alert before automatically dismissing it. You can also include a subtitle and secondary action when needed.

The system displays the primary and secondary actions as buttons on the alert. After the user taps the button, the system calls the action’s [`handler`](cpalertaction/handler.md) block, which is where your app performs the requested action. The system also dismisses the alert after the user taps the button. However, your app can dismiss the alert without any user interaction by calling [`dismissNavigationAlert(animated:completion:)`](cpmaptemplate/dismissnavigationalert(animated:completion:).md).

## Topics

### Creating a Navigation Alert
- [init(titleVariants: [String], subtitleVariants: [String]?, image: UIImage?, primaryAction: CPAlertAction, secondaryAction: CPAlertAction?, duration: TimeInterval)](cpnavigationalert/init(titlevariants:subtitlevariants:image:primaryaction:secondaryaction:duration:).md)
  Creates a navigation alert.
- [init(titleVariants: [String], subtitleVariants: [String]?, imageSet: CPImageSet?, primaryAction: CPAlertAction, secondaryAction: CPAlertAction?, duration: TimeInterval)](cpnavigationalert/init(titlevariants:subtitlevariants:imageset:primaryaction:secondaryaction:duration:).md)
  Creates a navigation alert.
### Getting Titles
- [var titleVariants: [String]](cpnavigationalert/titlevariants.md)
  An array of title strings.
- [var subtitleVariants: [String]](cpnavigationalert/subtitlevariants.md)
  An array of subtitle strings.
- [func updateTitleVariants([String], subtitleVariants: [String])](cpnavigationalert/updatetitlevariants(_:subtitlevariants:).md)
  Updates title and subtitle variants.
### Getting the Alert Image
- [var image: UIImage?](cpnavigationalert/image.md)
  An image displayed in the navigation alert.
- [var imageSet: CPImageSet?](cpnavigationalert/imageset.md)
  An image set displayed in the navigation alert.
### Getting the Actions
- [var primaryAction: CPAlertAction](cpnavigationalert/primaryaction.md)
  The primary action, and button, for the navigation alert.
- [var secondaryAction: CPAlertAction?](cpnavigationalert/secondaryaction.md)
  An optional secondary action, and button, for the navigation alert.
### Getting the Alert Duration
- [var duration: TimeInterval](cpnavigationalert/duration.md)
  The amount of time, in seconds, that the alert is visible.
- [let CPNavigationAlertMinimumDuration: TimeInterval](cpnavigationalertminimumduration.md)
  A constant that defines the minimum amount of time that an alert is visible.
### Enumerations
- [CPNavigationAlert.DismissalContext](cpnavigationalert/dismissalcontext.md)
  A set of reasons for dismissing a navigation alert.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [func present(navigationAlert: CPNavigationAlert, animated: Bool)](cpmaptemplate/present(navigationalert:animated:).md)
  Displays a navigation alert on the map template.
- [func dismissNavigationAlert(animated: Bool, completion: (Bool) -> Void)](cpmaptemplate/dismissnavigationalert(animated:completion:).md)
  Tells the map template to dismiss the visable navigation alert.
- [var currentNavigationAlert: CPNavigationAlert?](cpmaptemplate/currentnavigationalert.md)
  The visible navigation alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert)*