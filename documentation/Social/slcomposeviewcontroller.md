# SLComposeViewController

**Framework**: Social  
**Kind**: class

A view controller that allows the user to compose social media posts.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class SLComposeViewController
```

#### Overview

Use the [`isAvailable(forServiceType:)`](slcomposeviewcontroller/isavailable(forservicetype:).md) class method to check if a service account, such as Twitter, is set up and reachable before presenting this view to the user.

Set the initial content before presenting the view controller to the user. All the methods that set the content of a post return a Boolean value. They return [`false`](https://developer.apple.com/documentation/swift/false) if the content doesn’t fit in the post or if the view controller has already been presented to the user. You must set all of the content in the post before presenting the view controller to the user. After presenting the view controller, only the user can edit the post.

You can set a handler—using the [`completionHandler`](slcomposeviewcontroller/completionhandler.md) property—to be notified when the user is done composing a post. Note that completion handlers are not called on any particular thread.

## Topics

### Creating a Social Compose View Controller
- [init!(forServiceType: String!)](slcomposeviewcontroller/init(forservicetype:).md)
  Creates a new social compose view controller.
### Checking the Social Service Type
- [class func isAvailable(forServiceType: String!) -> Bool](slcomposeviewcontroller/isavailable(forservicetype:).md)
  Returns A Boolean value that indicates whether you can send a request for a particular service type.
- [var serviceType: String!](slcomposeviewcontroller/servicetype.md)
  Specifies the social-networking service.
### Specifying the Contents of the Post
- [func setInitialText(String!) -> Bool](slcomposeviewcontroller/setinitialtext(_:).md)
  Sets the initial text to be posted.
- [func add(UIImage!) -> Bool](slcomposeviewcontroller/add(_:)-1z68a.md)
  Adds an image to the post.
- [func add(URL!) -> Bool](slcomposeviewcontroller/add(_:)-3mn1w.md)
  Adds a URL to the post.
- [func removeAllImages() -> Bool](slcomposeviewcontroller/removeallimages.md)
  Removes all images from the post.
- [func removeAllURLs() -> Bool](slcomposeviewcontroller/removeallurls.md)
  Removes all URLs from the post.
### Processing the Results
- [var completionHandler: SLComposeViewControllerCompletionHandler!](slcomposeviewcontroller/completionhandler.md)
  The handler to call when the user is done composing a post.
- [typealias SLComposeViewControllerCompletionHandler](slcomposeviewcontrollercompletionhandler.md)
  Defines a handler to call when the user finishes composing a post.
- [enum SLComposeViewControllerResult](slcomposeviewcontrollerresult.md)
  Possible values for the `result` parameter of the [`completionHandler`](slcomposeviewcontroller/completionhandler.md) property.

## Relationships

### Inherits From
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class SLComposeServiceViewController](slcomposeserviceviewcontroller.md)
  A view controller that you present from your share app extension, allowing the user to compose social media posts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeviewcontroller)*