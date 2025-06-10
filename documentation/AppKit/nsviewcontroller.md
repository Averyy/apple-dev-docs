# NSViewController

**Framework**: AppKit  
**Kind**: class

A controller that manages a view, typically loaded from a nib file.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
class NSViewController
```

#### Overview

View controller management includes:

- Memory management of top-level objects similar to that performed by the [`NSWindowController`](nswindowcontroller.md) class, taking the same care to prevent reference cycles when controls are bound to the nib file’s owner.
- Declaring a generic [`view`](nsviewcontroller/view.md) property, to make it easy to establish bindings in the nib to an object that isn’t yet known at nib-loading time or readily available to the code that’s doing the nib loading.
- Implementing the key-value binding NSEditor informal protocol, so that apps using a view controller can easily make bound controls in the views commit or discard changes by the user.

In macOS 10.10 and later, a view controller offers a full set of life cycle methods, allowing you to manage the content of a window in a way that is on a par with iOS view controller management. These methods, presented in order here to reflect a typical cycle, are:

1. [`viewDidLoad()`](nsviewcontroller/viewdidload().md)
2. [`viewWillAppear()`](nsviewcontroller/viewwillappear().md)
3. [`viewDidAppear()`](nsviewcontroller/viewdidappear().md)

1. [`updateViewConstraints()`](nsviewcontroller/updateviewconstraints().md)
2. [`viewWillLayout()`](nsviewcontroller/viewwilllayout().md)
3. [`viewDidLayout()`](nsviewcontroller/viewdidlayout().md)
4. [`viewWillDisappear()`](nsviewcontroller/viewwilldisappear().md)
5. [`viewDidDisappear()`](nsviewcontroller/viewdiddisappear().md)

In addition, in macOS 10.10 and later, a view controller participates in the responder chain. You can implement action methods directly in the view controller. Corresponding actions that originate in the view controller’s view proceed up the responder chain and are handled by those methods.

Prior to OS X v10.10, a typical usage pattern for loading a nib file was to subclass [`NSViewController`](nsviewcontroller.md) and override its [`loadView()`](nsviewcontroller/loadview().md) method to call `[super loadView]`. But in macOS 10.10 and later, the [`loadView()`](nsviewcontroller/loadview().md) method automatically looks for a nib file with the same name as the view controller. To take advantage of this behavior, name a nib file after its corresponding view controller and pass `nil` to both parameters of the [`init(nibName:bundle:)`](nsviewcontroller/init(nibname:bundle:).md) method.

A view controller employs lazy loading of its view: Immediately after a view controller is loaded into memory, the value of its [`isViewLoaded`](nsviewcontroller/isviewloaded.md) property is [`false`](https://developer.apple.com/documentation/swift/false). The value changes to [`true`](https://developer.apple.com/documentation/swift/true) after the [`loadView()`](nsviewcontroller/loadview().md) method returns and just before the system calls the [`viewDidLoad()`](nsviewcontroller/viewdidload().md) method.

A view controller is meant to be highly reusable, such as for dynamically representing various objects. For example, the  [`addAccessoryController(_:)`](nspagelayout/addaccessorycontroller(_:).md) methods of the [`NSPageLayout`](nspagelayout.md) and [`NSPrintPanel`](nsprintpanel.md) classes take an [`NSViewController`](nsviewcontroller.md) instance as the argument, and set the [`representedObject`](nsviewcontroller/representedobject.md) property to the [`NSPrintInfo`](nsprintinfo.md) object that is to be shown to the user. This allows a developer to easily create new printing accessory views using bindings and the [`NSPrintInfo`](nsprintinfo.md) class’s key-value coding and key-value observing compliance. When the user dismisses a printing dialog, the  [`NSPageLayout`](nspagelayout.md) and [`NSPrintPanel`](nsprintpanel.md) classes each send NSEditor messages to each accessory view controller to ensure that the user’s changes have been committed or discarded properly. The titles of the accessories are retrieved from the view controllers and shown to the user in menus that the user can choose from.

## Topics

### Creating A View Controller
- [init(nibName: NSNib.Name?, bundle: Bundle?)](nsviewcontroller/init(nibname:bundle:).md)
  Returns a view controller object initialized to the nib file in the specified bundle.
- [func loadView()](nsviewcontroller/loadview.md)
  Instantiates a view from a nib file and sets the value of the [`view`](nsviewcontroller/view.md) property.
### Represented Object
- [var representedObject: Any?](nsviewcontroller/representedobject.md)
  The object whose value is presented in the receiver’s primary view.
### Nib Properties
- [var nibBundle: Bundle?](nsviewcontroller/nibbundle.md)
  The nib bundle to be loaded to instantiate the receiver’s primary view.
- [var nibName: NSNib.Name?](nsviewcontroller/nibname.md)
  The name of the nib file to be loaded to instantiate the receiver’s primary view.
### View Properties
- [var view: NSView](nsviewcontroller/view.md)
  The view controller’s primary view.
- [var title: String?](nsviewcontroller/title.md)
  The localized title of the receiver’s primary view.
### View Property Wrappers
- [NSViewController.ViewLoading](nsviewcontroller/viewloading.md)
  A property wrapper that loads the view controller’s view before accessing the property.
### NSEditor Conformance
- [func commitEditing(withDelegate: Any?, didCommit: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsviewcontroller/commitediting(withdelegate:didcommit:contextinfo:).md)
  Attempt to commit any currently edited results of the receiver.
- [func commitEditing() -> Bool](nsviewcontroller/commitediting.md)
  Returns whether the receiver was able to commit any pending edits.
- [func discardEditing()](nsviewcontroller/discardediting.md)
  Causes the receiver to discard any changes, restoring the previous values.
### Using a Storyboard
- [var storyboard: NSStoryboard?](nsviewcontroller/storyboard.md)
  The storyboard from which the view controller was loaded.
- [func dismiss(Any?)](nsviewcontroller/dismiss(_:)-3n76y.md)
### Responding to View Events
- [func viewDidLoad()](nsviewcontroller/viewdidload.md)
  Called after the view controller’s view has been loaded into memory.
- [func loadViewIfNeeded()](nsviewcontroller/loadviewifneeded.md)
- [var isViewLoaded: Bool](nsviewcontroller/isviewloaded.md)
  A Boolean value indicating whether the view controller’s view is loaded into memory.
- [var viewIfLoaded: NSView?](nsviewcontroller/viewifloaded.md)
- [func viewWillAppear()](nsviewcontroller/viewwillappear.md)
  Called after the view controller’s view has been loaded into memory is about to be added to the view hierarchy in the window.
- [func viewDidAppear()](nsviewcontroller/viewdidappear.md)
  Called when the view controller’s view is fully transitioned onto the screen.
- [func viewWillDisappear()](nsviewcontroller/viewwilldisappear.md)
  Called when the view controller’s view is about to be removed from the view hierarchy in the window.
- [func viewDidDisappear()](nsviewcontroller/viewdiddisappear.md)
  Called after the view controller’s view is removed from the view hierarchy in a window.
### Managing View Layout
- [var preferredContentSize: NSSize](nsviewcontroller/preferredcontentsize.md)
  The desired size of the view controller’s view, in screen units.
- [func updateViewConstraints()](nsviewcontroller/updateviewconstraints.md)
  Called during Auto Layout constraint updating to enable the view controller to mediate the process.
- [func viewWillLayout()](nsviewcontroller/viewwilllayout.md)
  Called just before the [`layout()`](nsview/layout().md) method of the view controller’s view is called.
- [func viewDidLayout()](nsviewcontroller/viewdidlayout.md)
  Called immediately after the [`layout()`](nsview/layout().md) method of the view controller’s view is called.
### Managing Child View Controllers in a Custom Container
- [func addChild(NSViewController)](nsviewcontroller/addchild(_:).md)
  A convenience method for adding a child view controller at the end of the [`children`](nsviewcontroller/children.md) array.
- [var children: [NSViewController]](nsviewcontroller/children.md)
  An array of view controllers that are hierarchical children of the view controller.
- [func transition(from: NSViewController, to: NSViewController, options: NSViewController.TransitionOptions, completionHandler: (() -> Void)?)](nsviewcontroller/transition(from:to:options:completionhandler:).md)
  Performs a transition between two sibling child view controllers of the view controller.
- [func insertChild(NSViewController, at: Int)](nsviewcontroller/insertchild(_:at:).md)
  Inserts a specified child view controller into the [`children`](nsviewcontroller/children.md) array at a specified position.
- [func removeChild(at: Int)](nsviewcontroller/removechild(at:).md)
  Removes a specified child controller from the view controller.
- [func removeFromParent()](nsviewcontroller/removefromparent.md)
  Removes the called view controller from its parent view controller.
- [func preferredContentSizeDidChange(for: NSViewController)](nsviewcontroller/preferredcontentsizedidchange(for:).md)
  Called when there is a change in value of the [`preferredContentSize`](nsviewcontroller/preferredcontentsize.md) property of a child view controller or a presented view controller.
### Presenting Another View Controller’s Content
- [func present(NSViewController, animator: any NSViewControllerPresentationAnimator)](nsviewcontroller/present(_:animator:).md)
  Presents another view controller using a specified, custom animator for presentation and dismissal.
- [func dismiss(NSViewController)](nsviewcontroller/dismiss(_:)-91my5.md)
  Dismisses a presented view controller, using the same animator that presented it.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior)](nsviewcontroller/present(_:aspopoverrelativeto:of:preferrededge:behavior:).md)
  Presents another view controller as a popover.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior, hasFullSizeContent: Bool)](nsviewcontroller/present(_:aspopoverrelativeto:of:preferrededge:behavior:hasfullsizecontent:).md)
- [func presentAsModalWindow(NSViewController)](nsviewcontroller/presentasmodalwindow(_:).md)
  Presents another view controller as a modal window, also known as an alert.
- [func presentAsSheet(NSViewController)](nsviewcontroller/presentassheet(_:).md)
  Presents another view controller as a sheet.
- [func present(inWidget: NSViewController)](nsviewcontroller/present(inwidget:).md)
### Getting Related View Controllers
- [var parent: NSViewController?](nsviewcontroller/parent.md)
  The immediate ancestor view controller of the view controller.
- [var presentedViewControllers: [NSViewController]?](nsviewcontroller/presentedviewcontrollers.md)
  The view controllers, if any, that are currently presented by the view controller.
- [var presentingViewController: NSViewController?](nsviewcontroller/presentingviewcontroller.md)
  The view controller that presented the view controller or that presented its farthest ancestor view controller.
### Configuring an App Extension View Controller
- [var extensionContext: NSExtensionContext?](nsviewcontroller/extensioncontext.md)
  For a view controller that is part of an app extension, the app extension context.
- [var preferredScreenOrigin: NSPoint](nsviewcontroller/preferredscreenorigin.md)
  For a view controller that is part of an app extension, the preferred screen origin.
- [var preferredMaximumSize: NSSize](nsviewcontroller/preferredmaximumsize.md)
  For a view controller that is part of an app extension, the largest allowable size for the app extension’s primary view, in screen units.
- [var preferredMinimumSize: NSSize](nsviewcontroller/preferredminimumsize.md)
  For a view controller that is part of an app extension, the smallest allowable size for the app extension’s primary view, in screen units.
- [func viewWillTransition(to: NSSize)](nsviewcontroller/viewwilltransition(to:).md)
  For a view controller that is part of an app extension, called when its view is about to be resized.
- [var sourceItemView: NSView?](nsviewcontroller/sourceitemview.md)
### Constants
- [NSViewController.TransitionOptions](nsviewcontroller/transitionoptions.md)
  Animation options for view transitions in a view controller.
### Initializers
- [init?(coder: NSCoder)](nsviewcontroller/init(coder:).md)
### Default Implementations
- [PlaygroundLiveViewable Implementations](nsviewcontroller/playgroundliveviewable-implementations.md)
- [XCPlaygroundLiveViewable Implementations](nsviewcontroller/xcplaygroundliveviewable-implementations.md)

## Relationships

### Inherits From
- [NSResponder](nsresponder.md)
### Inherited By
- [NSCollectionViewItem](nscollectionviewitem.md)
- [NSPageController](nspagecontroller.md)
- [NSSplitViewController](nssplitviewcontroller.md)
- [NSSplitViewItemAccessoryViewController](nssplitviewitemaccessoryviewcontroller.md)
- [NSTabViewController](nstabviewcontroller.md)
- [NSTitlebarAccessoryViewController](nstitlebaraccessoryviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](nseditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](nssegueperforming.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [PlaygroundLiveViewable](../playgroundsupport/playgroundliveviewable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSWindowController](nswindowcontroller.md)
  A controller that manages a window, usually a window stored in a nib file.
- [class NSTitlebarAccessoryViewController](nstitlebaraccessoryviewcontroller.md)
  An object that manages a custom view—known as an accessory view—in the title bar–toolbar area of a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller)*