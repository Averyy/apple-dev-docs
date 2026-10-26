# SLComposeServiceViewController

**Framework**: Social  
**Kind**: class  
**Role**: Class

A view controller that you present from your share app extension, allowing the user to compose social media posts.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
class SLComposeServiceViewController
```

*iOS, iPadOS, Mac Catalyst*

```objc
@interface SLComposeServiceViewController : UIViewController
```

*macOS*

```objc
@interface SLComposeServiceViewController : NSViewController
```

#### Overview

The [`SLComposeServiceViewController`](./slcomposeserviceviewcontroller.md) class provides a standard compose view, and you can present it for social sharing extensions on iOS and macOS. By default, the compose view includes items such as an editable text view and an indication of remaining characters, in addition to support for previewing attachments and displaying configuration items, such as an account or privacy picker.

The compose view controller gets items for the content and preview areas from the [`extensionContext`](../UIKit/uiviewcontroller/extensioncontext.md) property of the extension’s [`NSExtensionContext`](../Foundation/nsextensioncontext.md) object.

## Topics

### Configuring the Post Details
- [func configurationItems() -> [Any]!](./slcomposeserviceviewcontroller/configurationitems%28%29.md)
  Returns configuration items to display in the compose view.
- [class SLComposeSheetConfigurationItem](./slcomposesheetconfigurationitem.md)
  An object that provides additional configuration details to use when configuring a composition interface.
- [func reloadConfigurationItems()](./slcomposeserviceviewcontroller/reloadconfigurationitems%28%29.md)
  Reloads the list of configuration items.
### Managing the Contents of the Post
- [var contentText: String!](./slcomposeserviceviewcontroller/contenttext.md)
  A string that represents the text which the user entered into the compose view’s text view.
- [var placeholder: String!](./slcomposeserviceviewcontroller/placeholder.md)
  A string that’s displayed in the compose view’s text view when the text view is empty.
- [var textView: UITextView!](./slcomposeserviceviewcontroller/textview.md)
  The editable text view in the compose view.
### Presenting the View Controller
- [func pushConfigurationViewController(UIViewController!)](./slcomposeserviceviewcontroller/pushconfigurationviewcontroller%28_%29.md)
  Presents a configuration view controller that lets the user configure the post.
- [func popConfigurationViewController()](./slcomposeserviceviewcontroller/popconfigurationviewcontroller%28%29.md)
  Dismisses the current configuration view controller.
### Responding to Lifecycle Events
- [func presentationAnimationDidFinish()](./slcomposeserviceviewcontroller/presentationanimationdidfinish%28%29.md)
  Tells the compose view controller that the presentation animation is finished.
- [func didSelectCancel()](./slcomposeserviceviewcontroller/didselectcancel%28%29.md)
  Sent to the compose view after the cancel animation finishes.
- [func didSelectPost()](./slcomposeserviceviewcontroller/didselectpost%28%29.md)
  Sent to the compose view after the post animation finishes.
### Canceling a Post
- [func cancel()](./slcomposeserviceviewcontroller/cancel%28%29.md)
  Starts the animated dismissal of the compose view.
### Validating Content
- [var charactersRemaining: NSNumber!](./slcomposeserviceviewcontroller/charactersremaining.md)
  The number of characters remaining in a custom character limit.
- [func isContentValid() -> Bool](./slcomposeserviceviewcontroller/iscontentvalid%28%29.md)
  A Boolean value that indicates whether the current content and attachments are valid.
- [func validateContent()](./slcomposeserviceviewcontroller/validatecontent%28%29.md)
  Performs validation of the current content and updates the state of the Post button, if appropriate.
### Previewing Attachments
- [func loadPreviewView() -> UIView!](./slcomposeserviceviewcontroller/loadpreviewview%28%29.md)
  Loads a view that displays a preview of the attachments in the extension context.
### Enabling Text Autocompletion
- [var autoCompletionViewController: UIViewController!](./slcomposeserviceviewcontroller/autocompletionviewcontroller.md)
  The view controller that manages an autocompletion view for suggesting common text completions while users type.

## Relationships

### Inherits From
- [NSViewController](../AppKit/nsviewcontroller.md)
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSEditor](../AppKit/nseditor.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSeguePerforming](../AppKit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTextDelegate](../AppKit/nstextdelegate.md)
- [NSTextViewDelegate](../AppKit/nstextviewdelegate.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIScrollViewDelegate](../UIKit/uiscrollviewdelegate.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITextViewDelegate](../UIKit/uitextviewdelegate.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Composition Interfaces
- [class SLComposeViewController](./slcomposeviewcontroller.md)
  A view controller that allows the user to compose social media posts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller)*