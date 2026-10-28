# SLComposeViewController

**Framework**: Social  
**Kind**: class  
**Role**: Class

A view controller that allows the user to compose social media posts.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class SLComposeViewController
```

```objc
@interface SLComposeViewController : UIViewController
```

## Overview

Use the [`isAvailable(forServiceType:)`](./slcomposeviewcontroller/isavailable%28forservicetype%29.md) class method to check if a service account, such as Twitter, is set up and reachable before presenting this view to the user.

Set the initial content before presenting the view controller to the user. All the methods that set the content of a post return a Boolean value. They return [`false`](../Swift/false.md) if the content doesn’t fit in the post or if the view controller has already been presented to the user. You must set all of the content in the post before presenting the view controller to the user. After presenting the view controller, only the user can edit the post.

You can set a handler—using the [`completionHandler`](./slcomposeviewcontroller/completionhandler.md) property—to be notified when the user is done composing a post. Note that completion handlers are not called on any particular thread.

## Topics

### Creating a Social Compose View Controller
- [init!(forServiceType: String!)](./slcomposeviewcontroller/init%28forservicetype%29.md)
  Creates a new social compose view controller.
### Checking the Social Service Type
- [class func isAvailable(forServiceType: String!) -> Bool](./slcomposeviewcontroller/isavailable%28forservicetype%29.md)
  Returns A Boolean value that indicates whether you can send a request for a particular service type.
- [var serviceType: String!](./slcomposeviewcontroller/servicetype.md)
  Specifies the social-networking service.
### Specifying the Contents of the Post
- [func setInitialText(String!) -> Bool](./slcomposeviewcontroller/setinitialtext%28_%29.md)
  Sets the initial text to be posted.
- [func add(UIImage!) -> Bool](./slcomposeviewcontroller/add%28_%29-1z68a.md)
  Adds an image to the post.
- [func add(URL!) -> Bool](./slcomposeviewcontroller/add%28_%29-3mn1w.md)
  Adds a URL to the post.
- [func removeAllImages() -> Bool](./slcomposeviewcontroller/removeallimages%28%29.md)
  Removes all images from the post.
- [func removeAllURLs() -> Bool](./slcomposeviewcontroller/removeallurls%28%29.md)
  Removes all URLs from the post.
### Processing the Results
- [var completionHandler: SLComposeViewControllerCompletionHandler!](./slcomposeviewcontroller/completionhandler.md)
  The handler to call when the user is done composing a post.
- [typealias SLComposeViewControllerCompletionHandler](./slcomposeviewcontrollercompletionhandler.md)
  Defines a handler to call when the user finishes composing a post.
- [enum SLComposeViewControllerResult](./slcomposeviewcontrollerresult.md)
  Possible values for the `result` parameter of the [`completionHandler`](./slcomposeviewcontroller/completionhandler.md) property.

## Relationships

### Inherits From
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Composition Interfaces
- [class SLComposeServiceViewController](./slcomposeserviceviewcontroller.md)
  A view controller that you present from your share app extension, allowing the user to compose social media posts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeviewcontroller)*