# SLComposeServiceViewController

**Framework**: Social  
**Kind**: class

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

#### Overview

The [`SLComposeServiceViewController`](slcomposeserviceviewcontroller.md) class provides a standard compose view, and you can present it for social sharing extensions on iOS and macOS. By default, the compose view includes items such as an editable text view and an indication of remaining characters, in addition to support for previewing attachments and displaying configuration items, such as an account or privacy picker.

The compose view controller gets items for the content and preview areas from the [`extensionContext`](https://developer.apple.com/documentation/uikit/uiviewcontroller/extensioncontext) property of the extension’s [`NSExtensionContext`](https://developer.apple.com/documentation/foundation/nsextensioncontext) object.

## Topics

### Configuring the Post Details
- [func configurationItems() -> [Any]!](slcomposeserviceviewcontroller/configurationitems.md)
  Returns configuration items to display in the compose view.
- [class SLComposeSheetConfigurationItem](slcomposesheetconfigurationitem.md)
  An object that provides additional configuration details to use when configuring a composition interface.
- [func reloadConfigurationItems()](slcomposeserviceviewcontroller/reloadconfigurationitems.md)
  Reloads the list of configuration items.
### Managing the Contents of the Post
- [var contentText: String!](slcomposeserviceviewcontroller/contenttext.md)
  A string that represents the text which the user entered into the compose view’s text view.
- [var placeholder: String!](slcomposeserviceviewcontroller/placeholder.md)
  A string that’s displayed in the compose view’s text view when the text view is empty.
- [var textView: UITextView!](slcomposeserviceviewcontroller/textview.md)
  The editable text view in the compose view.
### Presenting the View Controller
- [func pushConfigurationViewController(UIViewController!)](slcomposeserviceviewcontroller/pushconfigurationviewcontroller(_:).md)
  Presents a configuration view controller that lets the user configure the post.
- [func popConfigurationViewController()](slcomposeserviceviewcontroller/popconfigurationviewcontroller.md)
  Dismisses the current configuration view controller.
### Responding to Lifecycle Events
- [func presentationAnimationDidFinish()](slcomposeserviceviewcontroller/presentationanimationdidfinish.md)
  Tells the compose view controller that the presentation animation is finished.
- [func didSelectCancel()](slcomposeserviceviewcontroller/didselectcancel.md)
  Sent to the compose view after the cancel animation finishes.
- [func didSelectPost()](slcomposeserviceviewcontroller/didselectpost.md)
  Sent to the compose view after the post animation finishes.
### Canceling a Post
- [func cancel()](slcomposeserviceviewcontroller/cancel.md)
  Starts the animated dismissal of the compose view.
### Validating Content
- [var charactersRemaining: NSNumber!](slcomposeserviceviewcontroller/charactersremaining.md)
  The number of characters remaining in a custom character limit.
- [func isContentValid() -> Bool](slcomposeserviceviewcontroller/iscontentvalid.md)
  A Boolean value that indicates whether the current content and attachments are valid.
- [func validateContent()](slcomposeserviceviewcontroller/validatecontent.md)
  Performs validation of the current content and updates the state of the Post button, if appropriate.
### Previewing Attachments
- [func loadPreviewView() -> UIView!](slcomposeserviceviewcontroller/loadpreviewview.md)
  Loads a view that displays a preview of the attachments in the extension context.
### Enabling Text Autocompletion
- [var autoCompletionViewController: UIViewController!](slcomposeserviceviewcontroller/autocompletionviewcontroller.md)
  The view controller that manages an autocompletion view for suggesting common text completions while users type.

## Relationships

### Inherits From
- [NSViewController](../appkit/nsviewcontroller.md)
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSEditor](../appkit/nseditor.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSeguePerforming](../appkit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTextDelegate](../appkit/nstextdelegate.md)
- [NSTextViewDelegate](../appkit/nstextviewdelegate.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIScrollViewDelegate](../uikit/uiscrollviewdelegate.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITextViewDelegate](../uikit/uitextviewdelegate.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class SLComposeViewController](slcomposeviewcontroller.md)
  A view controller that allows the user to compose social media posts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller)*