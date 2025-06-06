# NSWindow

**Framework**: AppKit  
**Kind**: class

A window that an app displays on the screen.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSWindow
```

#### Overview

A single [`NSWindow`](nswindow.md) object corresponds to, at most, one on-screen window. Windows perform two principal functions:

- To place views in a provided area
- To accept and distribute mouse and keyboard events the user generates to the appropriate views

> **Note**:  Although the [`NSWindow`](nswindow.md) class inherits the [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding) protocol from [`NSResponder`](nsresponder.md), the class doesn’t support coding. Legacy support for archivers exists, but its use is deprecated and may not work. Any attempt to archive or unarchive a window object using a keyed coding object raises an [`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception) exception. For details about window restoration, see [`restorationClass`](nswindow/restorationclass.md).

 Although the [`NSWindow`](nswindow.md) class inherits the [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding) protocol from [`NSResponder`](nsresponder.md), the class doesn’t support coding. Legacy support for archivers exists, but its use is deprecated and may not work. Any attempt to archive or unarchive a window object using a keyed coding object raises an [`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception) exception. For details about window restoration, see [`restorationClass`](nswindow/restorationclass.md).

## Topics

### Creating a Window
- [convenience init(contentViewController: NSViewController)](nswindow/init(contentviewcontroller:).md)
  Creates a titled window that contains the specified content view controller.
- [init(contentRect: NSRect, styleMask: NSWindow.StyleMask, backing: NSWindow.BackingStoreType, defer: Bool)](nswindow/init(contentrect:stylemask:backing:defer:).md)
  Initializes the window with the specified values.
- [convenience init(contentRect: NSRect, styleMask: NSWindow.StyleMask, backing: NSWindow.BackingStoreType, defer: Bool, screen: NSScreen?)](nswindow/init(contentrect:stylemask:backing:defer:screen:).md)
  Initializes an allocated window with the specified values.
### Managing the Window’s Behavior
- [var delegate: (any NSWindowDelegate)?](nswindow/delegate.md)
  The window’s delegate.
- [protocol NSWindowDelegate](nswindowdelegate.md)
  A set of optional methods that a window’s delegate can implement to respond to events, such as window resizing, moving, exposing, and minimizing.
### Configuring the Window’s Content
- [var contentViewController: NSViewController?](nswindow/contentviewcontroller.md)
  The main content view controller for the window.
- [var contentView: NSView?](nswindow/contentview.md)
  The window’s content view, the highest accessible view object in the window’s view hierarchy.
### Configuring the Window’s Appearance
- [var styleMask: NSWindow.StyleMask](nswindow/stylemask-swift.property.md)
  Flags that describe the window’s current style, such as if it’s resizable or in full-screen mode.
- [NSWindow.StyleMask](nswindow/stylemask-swift.struct.md)
  Constants that specify the style of a window, and that you can combine with the C bitwise OR operator.
- [func toggleFullScreen(Any?)](nswindow/togglefullscreen(_:).md)
  Takes the window into or out of fullscreen mode,
- [var worksWhenModal: Bool](nswindow/workswhenmodal.md)
  A Boolean value that indicates whether the window is able to receive keyboard and mouse events even when some other window is being run modally.
- [var alphaValue: CGFloat](nswindow/alphavalue.md)
  The window’s alpha value.
- [var backgroundColor: NSColor!](nswindow/backgroundcolor.md)
  The color of the window’s background.
- [var colorSpace: NSColorSpace?](nswindow/colorspace.md)
  The window’s color space.
- [func setDynamicDepthLimit(Bool)](nswindow/setdynamicdepthlimit(_:).md)
  Sets a Boolean value that indicates whether the window’s depth limit can change to match the depth of the screen it’s on.
- [var canHide: Bool](nswindow/canhide.md)
  A Boolean value that indicates whether the window can hide when its application becomes hidden.
- [var isOnActiveSpace: Bool](nswindow/isonactivespace.md)
  A Boolean value that indicates whether the window is on the currently active space.
- [var hidesOnDeactivate: Bool](nswindow/hidesondeactivate.md)
  A Boolean value that indicates whether the window is removed from the screen when its application becomes inactive.
- [var collectionBehavior: NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.property.md)
  A value that identifies the window’s behavior in window collections.
- [var isOpaque: Bool](nswindow/isopaque.md)
  A Boolean value that indicates whether the window is opaque.
- [var hasShadow: Bool](nswindow/hasshadow.md)
  A Boolean value that indicates whether the window has a shadow.
- [func invalidateShadow()](nswindow/invalidateshadow.md)
  Invalidates the window shadow so that it is recomputed based on the current window shape.
- [func autorecalculatesContentBorderThickness(for: NSRectEdge) -> Bool](nswindow/autorecalculatescontentborderthickness(for:).md)
  Indicates whether the window calculates the thickness of a given border automatically.
- [func setAutorecalculatesContentBorderThickness(Bool, for: NSRectEdge)](nswindow/setautorecalculatescontentborderthickness(_:for:).md)
  Specifies whether the window calculates the thickness of a given border automatically.
- [func contentBorderThickness(for: NSRectEdge) -> CGFloat](nswindow/contentborderthickness(for:).md)
  Indicates the thickness of a given border of the window.
- [func setContentBorderThickness(CGFloat, for: NSRectEdge)](nswindow/setcontentborderthickness(_:for:).md)
  Specifies the thickness of a given border of the window.
- [var preventsApplicationTerminationWhenModal: Bool](nswindow/preventsapplicationterminationwhenmodal.md)
  A Boolean value that indicates whether the window prevents application termination when modal.
- [var appearanceSource: (any NSAppearanceCustomization)!](nswindow/appearancesource.md)
  An object that the window inherits its appearance from.
### Accessing Window Information
- [var depthLimit: NSWindow.Depth](nswindow/depthlimit.md)
  The depth limit of the window.
- [var hasDynamicDepthLimit: Bool](nswindow/hasdynamicdepthlimit.md)
  A Boolean value that indicates whether the window’s depth limit can change to match the depth of the screen it’s on.
- [class var defaultDepthLimit: NSWindow.Depth](nswindow/defaultdepthlimit.md)
  Returns the default depth limit for instances of `NSWindow`.
- [var windowNumber: Int](nswindow/windownumber.md)
  The window number of the window’s window device.
- [class func windowNumbers(options: NSWindow.NumberListOptions) -> [NSNumber]?](nswindow/windownumbers(options:).md)
  Returns the window numbers for all visible windows satisfying the specified options.
- [var deviceDescription: [NSDeviceDescriptionKey : Any]](nswindow/devicedescription.md)
  A dictionary containing information about the window’s resolution, such as color, depth, and so on.
- [struct NSDeviceDescriptionKey](nsdevicedescriptionkey.md)
  These constants are the keys for device description dictionaries.
- [var canBecomeVisibleWithoutLogin: Bool](nswindow/canbecomevisiblewithoutlogin.md)
  A Boolean value that indicates whether the window can be displayed at the login window.
- [var sharingType: NSWindow.SharingType](nswindow/sharingtype-swift.property.md)
  A Boolean value that indicates the level of access other processes have to the window’s content.
- [var backingType: NSWindow.BackingStoreType](nswindow/backingtype.md)
  The window’s backing store type.
- [func displayLink(target: Any, selector: Selector) -> CADisplayLink](nswindow/displaylink(target:selector:).md)
### Getting Layout Information
- [class func contentRect(forFrameRect: NSRect, styleMask: NSWindow.StyleMask) -> NSRect](nswindow/contentrect(forframerect:stylemask:).md)
  Returns the content rectangle used by a window with a given frame rectangle and window style.
- [class func frameRect(forContentRect: NSRect, styleMask: NSWindow.StyleMask) -> NSRect](nswindow/framerect(forcontentrect:stylemask:).md)
  Returns the frame rectangle used by a window with a given content rectangle and window style.
- [class func minFrameWidth(withTitle: String, styleMask: NSWindow.StyleMask) -> CGFloat](nswindow/minframewidth(withtitle:stylemask:).md)
  Returns the minimum width a window’s frame rectangle must have for it to display a title, with a given window style.
- [func contentRect(forFrameRect: NSRect) -> NSRect](nswindow/contentrect(forframerect:).md)
  Returns the window’s content rectangle with a given frame rectangle.
- [func frameRect(forContentRect: NSRect) -> NSRect](nswindow/framerect(forcontentrect:).md)
  Returns the window’s frame rectangle with a given content rectangle.
### Managing Windows
- [var windowController: NSWindowController?](nswindow/windowcontroller.md)
  The window’s window controller.
### Managing Sheets
- [var attachedSheet: NSWindow?](nswindow/attachedsheet.md)
  The sheet attached to the window.
- [var isSheet: Bool](nswindow/issheet.md)
  A Boolean value that indicates whether the window has ever run as a modal sheet.
- [func beginSheet(NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](nswindow/beginsheet(_:completionhandler:).md)
  Starts a document-modal session and presents—or queues for presentation—a sheet.
- [func beginCriticalSheet(NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](nswindow/begincriticalsheet(_:completionhandler:).md)
  Starts a document-modal session and presents the specified critical sheet.
- [func endSheet(NSWindow)](nswindow/endsheet(_:).md)
  Ends a document-modal session and dismisses the specified sheet.
- [func endSheet(NSWindow, returnCode: NSApplication.ModalResponse)](nswindow/endsheet(_:returncode:).md)
  Ends a document-modal session and dismisses the specified sheet.
- [var sheetParent: NSWindow?](nswindow/sheetparent.md)
  The window to which the sheet is attached.
- [var sheets: [NSWindow]](nswindow/sheets.md)
  An array of the sheets currently attached to the window.
### Sizing Windows
- [var frame: NSRect](nswindow/frame.md)
  The window’s frame rectangle in screen coordinates, including the title bar.
- [func setFrameOrigin(NSPoint)](nswindow/setframeorigin(_:).md)
  Positions the bottom-left corner of the window’s frame rectangle at a given point in screen coordinates.
- [func setFrameTopLeftPoint(NSPoint)](nswindow/setframetopleftpoint(_:).md)
  Positions the top-left corner of the window’s frame rectangle at a given point in screen coordinates.
- [func constrainFrameRect(NSRect, to: NSScreen?) -> NSRect](nswindow/constrainframerect(_:to:).md)
  Modifies and returns a frame rectangle so that its top edge lies on a specific screen.
- [func cascadeTopLeft(from: NSPoint) -> NSPoint](nswindow/cascadetopleft(from:).md)
  Positions the window’s top-left to a given point.
- [func setFrame(NSRect, display: Bool)](nswindow/setframe(_:display:).md)
  Sets the origin and size of the window’s frame rectangle according to a given frame rectangle, thereby setting its position and size onscreen.
- [func setFrame(NSRect, display: Bool, animate: Bool)](nswindow/setframe(_:display:animate:).md)
  Sets the origin and size of the window’s frame rectangle, with optional animation, according to a given frame rectangle, thereby setting its position and size onscreen.
- [func animationResizeTime(NSRect) -> TimeInterval](nswindow/animationresizetime(_:).md)
  Specifies the duration of a smooth frame-size change.
- [var aspectRatio: NSSize](nswindow/aspectratio.md)
  The window’s aspect ratio, which constrains the size of its frame rectangle to integral multiples of this ratio when the user resizes it.
- [var minSize: NSSize](nswindow/minsize.md)
  The minimum size to which the window’s frame (including its title bar) can be sized.
- [var maxSize: NSSize](nswindow/maxsize.md)
  The maximum size to which the window’s frame (including its title bar) can be sized.
- [var isZoomed: Bool](nswindow/iszoomed.md)
  A Boolean value that indicates whether the window is in a zoomed state.
- [func performZoom(Any?)](nswindow/performzoom(_:).md)
  This action method simulates the user clicking the zoom box by momentarily highlighting the button and then zooming the window.
- [func zoom(Any?)](nswindow/zoom(_:).md)
  Toggles the size and location of the window between its standard state (which the application provides as the best size to display the window’s data) and its user state (a new size and location the user may have set by moving or resizing the window).
- [var resizeFlags: NSEvent.ModifierFlags](nswindow/resizeflags.md)
  The flags field of the event record for the mouse-down event that initiated the resizing session.
- [var resizeIncrements: NSSize](nswindow/resizeincrements.md)
  The window’s resizing increments.
- [var preservesContentDuringLiveResize: Bool](nswindow/preservescontentduringliveresize.md)
  A Boolean value that indicates whether the window tries to optimize user-initiated resize operations by preserving the content of views that have not changed.
- [var inLiveResize: Bool](nswindow/inliveresize.md)
  A Boolean value that indicates whether the window is being resized by the user.
### Sizing Content
- [var contentAspectRatio: NSSize](nswindow/contentaspectratio.md)
  The window’s content aspect ratio.
- [var contentMinSize: NSSize](nswindow/contentminsize.md)
  The minimum size of the window’s content view in the window’s base coordinate system.
- [func setContentSize(NSSize)](nswindow/setcontentsize(_:).md)
  Sets the size of the window’s content view to a given size, which is expressed in the window’s base coordinate system.
- [var contentMaxSize: NSSize](nswindow/contentmaxsize.md)
  The maximum size of the window’s content view in the window’s base coordinate system.
- [var contentResizeIncrements: NSSize](nswindow/contentresizeincrements.md)
  The window’s content-view resizing increments.
- [var contentLayoutGuide: Any?](nswindow/contentlayoutguide.md)
  A value used by Auto Layout constraints to automatically bind to the value of [`contentLayoutRect`](nswindow/contentlayoutrect.md).
- [var contentLayoutRect: NSRect](nswindow/contentlayoutrect.md)
  The area inside the window that is for non-obscured content, in window coordinates.
- [var maxFullScreenContentSize: NSSize](nswindow/maxfullscreencontentsize.md)
  A maximum size that is used to determine if a window can fit when it is in full screen in a tile.
- [var minFullScreenContentSize: NSSize](nswindow/minfullscreencontentsize.md)
  A minimum size that is used to determine if a window can fit when it is in full screen in a tile.
### Managing Window Layers
- [func orderOut(Any?)](nswindow/orderout(_:).md)
  Removes the window from the screen list, which hides the window.
- [func orderBack(Any?)](nswindow/orderback(_:).md)
  Moves the window to the back of its level in the screen list, without changing either the key window or the main window.
- [func orderFront(Any?)](nswindow/orderfront(_:).md)
  Moves the window to the front of its level in the screen list, without changing either the key window or the main window.
- [func orderFrontRegardless()](nswindow/orderfrontregardless.md)
  Moves the window to the front of its level, even if its application isn’t active, without changing either the key window or the main window.
- [func order(NSWindow.OrderingMode, relativeTo: Int)](nswindow/order(_:relativeto:).md)
  Repositions the window’s window device in the window server’s screen list.
- [var level: NSWindow.Level](nswindow/level-swift.property.md)
  The window level of the window.
- [NSWindow.Level](nswindow/level-swift.struct.md)
  The standard window levels in macOS.
### Managing Window Visibility and Occlusion State
- [var isVisible: Bool](nswindow/isvisible.md)
  A Boolean value that indicates whether the window is visible onscreen (even when it’s obscured by other windows).
- [var occlusionState: NSWindow.OcclusionState](nswindow/occlusionstate-swift.property.md)
  The occlusion state of the window.
### Managing Window Frames in User Defaults
- [class func removeFrame(usingName: NSWindow.FrameAutosaveName)](nswindow/removeframe(usingname:).md)
  Removes the frame data stored under a given name from the application’s user defaults.
- [func setFrameUsingName(NSWindow.FrameAutosaveName) -> Bool](nswindow/setframeusingname(_:).md)
  Sets the window’s frame rectangle by reading the rectangle data stored under a given name from the defaults system.
- [func setFrameUsingName(NSWindow.FrameAutosaveName, force: Bool) -> Bool](nswindow/setframeusingname(_:force:).md)
  Sets the window’s frame rectangle by reading the rectangle data stored under a given name from the defaults system. Can operate on non-resizable windows.
- [func saveFrame(usingName: NSWindow.FrameAutosaveName)](nswindow/saveframe(usingname:).md)
  Saves the window’s frame rectangle in the user defaults system under a given name.
- [func setFrameAutosaveName(NSWindow.FrameAutosaveName) -> Bool](nswindow/setframeautosavename(_:).md)
  Sets the name AppKit uses to automatically save the window’s frame rectangle data in the defaults system.
- [var frameAutosaveName: NSWindow.FrameAutosaveName](nswindow/frameautosavename-swift.property.md)
  The name used to automatically save the window’s frame rectangle data in the defaults system.
- [typealias FrameAutosaveName](nswindow/frameautosavename-swift.typealias.md)
  The type of a window’s frame autosave name.
- [var frameDescriptor: NSWindow.PersistableFrameDescriptor](nswindow/framedescriptor.md)
  A string representation of the window’s frame rectangle.
- [func setFrame(from: NSWindow.PersistableFrameDescriptor)](nswindow/setframe(from:).md)
  Sets the window’s frame rectangle from a given string representation.
- [typealias PersistableFrameDescriptor](nswindow/persistableframedescriptor.md)
  The type of a window’s frame descriptor.
### Managing Key Status
- [var isKeyWindow: Bool](nswindow/iskeywindow.md)
  A Boolean value that indicates whether the window is the key window for the application.
- [var canBecomeKey: Bool](nswindow/canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKey()](nswindow/makekey.md)
  Makes the window the key window.
- [func makeKeyAndOrderFront(Any?)](nswindow/makekeyandorderfront(_:).md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
- [func becomeKey()](nswindow/becomekey.md)
  Informs the window that it has become the key window.
- [func resignKey()](nswindow/resignkey.md)
  Resigns the window’s key window status.
### Managing Main Status
- [var isMainWindow: Bool](nswindow/ismainwindow.md)
  A Boolean value that indicates whether the window is the application’s main window.
- [var canBecomeMain: Bool](nswindow/canbecomemain.md)
  A Boolean value that indicates whether the window can become the application’s main window.
- [func makeMain()](nswindow/makemain.md)
  Makes the window the main window.
- [func becomeMain()](nswindow/becomemain.md)
  Informs the window that it has become the main window.
- [func resignMain()](nswindow/resignmain.md)
  Resigns the window’s main window status.
### Managing Toolbars
- [var toolbar: NSToolbar?](nswindow/toolbar.md)
  The window’s toolbar.
- [func toggleToolbarShown(Any?)](nswindow/toggletoolbarshown(_:).md)
  Toggles the visibility of the window’s toolbar.
- [func runToolbarCustomizationPalette(Any?)](nswindow/runtoolbarcustomizationpalette(_:).md)
  Presents the toolbar customization user interface.
### Managing Attached Windows
- [var childWindows: [NSWindow]?](nswindow/childwindows.md)
  An array of the window’s attached child windows.
- [func addChildWindow(NSWindow, ordered: NSWindow.OrderingMode)](nswindow/addchildwindow(_:ordered:).md)
  Adds a given window as a child window of the window.
- [func removeChildWindow(NSWindow)](nswindow/removechildwindow(_:).md)
  Detaches a given child window from the window.
- [var parent: NSWindow?](nswindow/parent.md)
  The parent window to which the window is attached as a child.
### Managing Default Buttons
- [var defaultButtonCell: NSButtonCell?](nswindow/defaultbuttoncell.md)
  The button cell that performs as if clicked when the window receives a Return (or Enter) key event.
- [func enableKeyEquivalentForDefaultButtonCell()](nswindow/enablekeyequivalentfordefaultbuttoncell.md)
  Reenables the default button cell’s key equivalent, so it performs a click when the user presses Return (or Enter).
- [func disableKeyEquivalentForDefaultButtonCell()](nswindow/disablekeyequivalentfordefaultbuttoncell.md)
  Disables the default button cell’s key equivalent, so it doesn’t perform a click when the user presses Return (or Enter).
### Managing Field Editors
- [func fieldEditor(Bool, for: Any?) -> NSText?](nswindow/fieldeditor(_:for:).md)
  Returns the window’s field editor, creating it if requested.
- [func endEditing(for: Any?)](nswindow/endediting(for:).md)
  Forces the field editor to give up its first responder status and prepares it for its next assignment.
### Managing the Window Menu
- [var isExcludedFromWindowsMenu: Bool](nswindow/isexcludedfromwindowsmenu.md)
  A Boolean value that indicates whether the window is excluded from the application’s Windows menu.
### Managing Cursor Rectangles
- [var areCursorRectsEnabled: Bool](nswindow/arecursorrectsenabled.md)
  A Boolean value that indicates whether the window’s cursor rectangles are enabled.
- [func enableCursorRects()](nswindow/enablecursorrects.md)
  Reenables cursor rectangle management within the window after a [`disableCursorRects()`](nswindow/disablecursorrects().md) message.
- [func disableCursorRects()](nswindow/disablecursorrects.md)
  Disables all cursor rectangle management within the window.
- [func discardCursorRects()](nswindow/discardcursorrects.md)
  Invalidates all cursor rectangles in the window.
- [func invalidateCursorRects(for: NSView)](nswindow/invalidatecursorrects(for:).md)
  Marks as invalid the cursor rectangles of a given view object in the window, so they’ll be set up again when the window becomes key.
- [func resetCursorRects()](nswindow/resetcursorrects.md)
  Clears the window’s cursor rectangles and the cursor rectangles of the [`NSView`](nsview.md) objects in its view hierarchy.
### Managing Title Bars
- [class func standardWindowButton(NSWindow.ButtonType, for: NSWindow.StyleMask) -> NSButton?](nswindow/standardwindowbutton(_:for:).md)
  Returns a new instance of a given standard window button, sized appropriately for a given window style.
- [func standardWindowButton(NSWindow.ButtonType) -> NSButton?](nswindow/standardwindowbutton(_:).md)
  Returns the window button of a given window button kind in the window’s view hierarchy.
- [var showsToolbarButton: Bool](nswindow/showstoolbarbutton.md)
  A Boolean value that indicates whether the toolbar control button is currently displayed.
- [var titlebarAppearsTransparent: Bool](nswindow/titlebarappearstransparent.md)
  A Boolean value that indicates whether the title bar draws its background.
- [var toolbarStyle: NSWindow.ToolbarStyle](nswindow/toolbarstyle-swift.property.md)
  The style that determines the appearance and location of the toolbar in relation to the title bar.
- [NSWindow.ToolbarStyle](nswindow/toolbarstyle-swift.enum.md)
  Styles that determine the appearance and location of the toolbar in relation to the title bar.
- [var titlebarSeparatorStyle: NSTitlebarSeparatorStyle](nswindow/titlebarseparatorstyle.md)
  The type of separator that the app displays between the title bar and content of a window.
- [enum NSTitlebarSeparatorStyle](nstitlebarseparatorstyle.md)
  Styles that determine the type of separator displayed between the title bar and content of a window.
- [var windowTitlebarLayoutDirection: NSUserInterfaceLayoutDirection](nswindow/windowtitlebarlayoutdirection.md)
  The direction the window’s title bar lays text out, either left to right or right to left.
### Managing Title Bar Accessories
- [func addTitlebarAccessoryViewController(NSTitlebarAccessoryViewController)](nswindow/addtitlebaraccessoryviewcontroller(_:).md)
  Adds the specified title bar accessory view controller to the window.
- [func insertTitlebarAccessoryViewController(NSTitlebarAccessoryViewController, at: Int)](nswindow/inserttitlebaraccessoryviewcontroller(_:at:).md)
  Inserts the view controller into the window’s array of title bar accessory view controllers at the specified index.
- [func removeTitlebarAccessoryViewController(at: Int)](nswindow/removetitlebaraccessoryviewcontroller(at:).md)
  Removes the view controller at the specified index from the window’s array of title bar accessory view controllers.
- [var titlebarAccessoryViewControllers: [NSTitlebarAccessoryViewController]](nswindow/titlebaraccessoryviewcontrollers.md)
  An array of title bar accessory view controllers that are currently added to the window.
### Managing Window Tabs
- [class var allowsAutomaticWindowTabbing: Bool](nswindow/allowsautomaticwindowtabbing.md)
  A Boolean value that indicates whether the app can automatically organize windows into tabs.
- [class var userTabbingPreference: NSWindow.UserTabbingPreference](nswindow/usertabbingpreference-swift.type.property.md)
  A value that indicates the user’s preference for window tabbing.
- [var tab: NSWindowTab](nswindow/tab.md)
  An object that represents information about a window when it displays as a tab.
- [var tabbingIdentifier: NSWindow.TabbingIdentifier](nswindow/tabbingidentifier-swift.property.md)
  A value that allows a group of related windows.
- [typealias TabbingIdentifier](nswindow/tabbingidentifier-swift.typealias.md)
  A value that allows a group of related windows.
- [func addTabbedWindow(NSWindow, ordered: NSWindow.OrderingMode)](nswindow/addtabbedwindow(_:ordered:).md)
  Adds the provided window as a new tab in a tabbed window using the specified ordering instruction.
- [var tabbingMode: NSWindow.TabbingMode](nswindow/tabbingmode-swift.property.md)
  A value that indicates when a window displays tabs.
- [var tabbedWindows: [NSWindow]?](nswindow/tabbedwindows.md)
  An array of windows that display as tabs.
- [func mergeAllWindows(Any?)](nswindow/mergeallwindows(_:).md)
  Merges all open windows into a single tabbed window.
- [func selectNextTab(Any?)](nswindow/selectnexttab(_:).md)
  Selects the next tab in the tab group in the trailing direction.
- [func selectPreviousTab(Any?)](nswindow/selectprevioustab(_:).md)
  Selects the previous tab in the tab group in the leading direction.
- [func moveTabToNewWindow(Any?)](nswindow/movetabtonewwindow(_:).md)
  Moves the tab to a new containing window.
- [func toggleTabBar(Any?)](nswindow/toggletabbar(_:).md)
  Shows or hides the tab bar.
- [func toggleTabOverview(Any?)](nswindow/toggletaboverview(_:).md)
  Shows or hides the tab overview.
- [var tabGroup: NSWindowTabGroup?](nswindow/tabgroup.md)
  A group of windows that display together as a tab group.
### Managing Tooltips
- [var allowsToolTipsWhenApplicationIsInactive: Bool](nswindow/allowstooltipswhenapplicationisinactive.md)
  A Boolean value that indicates whether the window can display tooltips even when the application is in the background.
### Handling Events
- [var currentEvent: NSEvent?](nswindow/currentevent.md)
  The event currently being processed by the application.
- [func nextEvent(matching: NSEvent.EventTypeMask) -> NSEvent?](nswindow/nextevent(matching:).md)
  Returns the next event matching a given mask.
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](nswindow/nextevent(matching:until:inmode:dequeue:).md)
  Forwards the message to the global application object.
- [func discardEvents(matching: NSEvent.EventTypeMask, before: NSEvent?)](nswindow/discardevents(matching:before:).md)
  Forwards the message to the global application object.
- [func postEvent(NSEvent, atStart: Bool)](nswindow/postevent(_:atstart:).md)
  Forwards the message to the global application object.
- [func sendEvent(NSEvent)](nswindow/sendevent(_:).md)
  This action method dispatches mouse and keyboard events the global application object sends to the window.
- [func tryToPerform(Selector, with: Any?) -> Bool](nswindow/trytoperform(_:with:).md)
  Dispatches action messages with a given argument.
### Managing Responders
- [var initialFirstResponder: NSView?](nswindow/initialfirstresponder.md)
  The view that’s made first responder (also called the key view) the first time the window is placed onscreen.
- [var firstResponder: NSResponder?](nswindow/firstresponder.md)
  The window’s first responder.
- [func makeFirstResponder(NSResponder?) -> Bool](nswindow/makefirstresponder(_:).md)
  Attempts to make a given responder the first responder for the window.
### Managing the Key View Loop
- [func selectKeyView(preceding: NSView)](nswindow/selectkeyview(preceding:).md)
  Gives key view status to the view that precedes the given view.
- [func selectKeyView(following: NSView)](nswindow/selectkeyview(following:).md)
  Gives key view status to the view that follows the given view.
- [func selectPreviousKeyView(Any?)](nswindow/selectpreviouskeyview(_:).md)
  Searches for a candidate previous key view and, if it finds one, tries to make it the first responder.
- [func selectNextKeyView(Any?)](nswindow/selectnextkeyview(_:).md)
  Searches for a candidate next key view and, if it finds one, tries to make it the first responder.
- [var keyViewSelectionDirection: NSWindow.SelectionDirection](nswindow/keyviewselectiondirection.md)
  The direction the window is currently using to change the key view.
- [var autorecalculatesKeyViewLoop: Bool](nswindow/autorecalculateskeyviewloop.md)
  A Boolean value that indicates whether the window automatically recalculates the key view loop when views are added.
- [func recalculateKeyViewLoop()](nswindow/recalculatekeyviewloop.md)
  Marks the key view loop as “dirty” and in need of recalculation.
### Managing Window Sharing
- [func transferWindowSharing(to: NSWindow, completionHandler: ((any Error)?) -> Void)](nswindow/transferwindowsharing(to:completionhandler:).md)
- [var hasActiveWindowSharingSession: Bool](nswindow/hasactivewindowsharingsession.md)
### Handling Mouse Events
- [var acceptsMouseMovedEvents: Bool](nswindow/acceptsmousemovedevents.md)
  A Boolean value that indicates whether the window accepts mouse-moved events.
- [var ignoresMouseEvents: Bool](nswindow/ignoresmouseevents.md)
  A Boolean value that indicates whether the window is transparent to mouse events.
- [var mouseLocationOutsideOfEventStream: NSPoint](nswindow/mouselocationoutsideofeventstream.md)
  The current location of the pointer reckoned in the window’s base coordinate system, regardless of the current event being handled or of any events pending.
- [class func windowNumber(at: NSPoint, belowWindowWithWindowNumber: Int) -> Int](nswindow/windownumber(at:belowwindowwithwindownumber:).md)
  Returns the number of the frontmost window that would be hit by a mouse-down at the specified screen location.
- [func trackEvents(matching: NSEvent.EventTypeMask, timeout: TimeInterval, mode: RunLoop.Mode, handler: (NSEvent?, UnsafeMutablePointer<ObjCBool>) -> Void)](nswindow/trackevents(matching:timeout:mode:handler:).md)
  Tracks events that match the specified mask using the specified tracking handler until the tracking handler explicitly terminates tracking.
- [func performDrag(with: NSEvent)](nswindow/performdrag(with:).md)
  Starts a window drag based on the specified mouse-down event.
- [class let foreverDuration: TimeInterval](nsevent/foreverduration.md)
  The longest time duration possible.
### Handling Window Restoration
- [var isRestorable: Bool](nswindow/isrestorable.md)
  A Boolean value indicating whether the window configuration is preserved between application launches.
- [var restorationClass: (any NSWindowRestoration.Type)?](nswindow/restorationclass.md)
  The restoration class associated with the window.
- [func disableSnapshotRestoration()](nswindow/disablesnapshotrestoration.md)
  Disables snapshot restoration.
- [func enableSnapshotRestoration()](nswindow/enablesnapshotrestoration.md)
  Enables snapshot restoration.
### Drawing Windows
- [func display()](nswindow/display.md)
  Passes a display message down the window’s view hierarchy, thus redrawing all views within the window.
- [func displayIfNeeded()](nswindow/displayifneeded.md)
  Passes a display message down the window’s view hierarchy, thus redrawing all views that need displaying.
- [var viewsNeedDisplay: Bool](nswindow/viewsneeddisplay.md)
  A Boolean value that indicates whether any of the window’s views need to be displayed.
- [var allowsConcurrentViewDrawing: Bool](nswindow/allowsconcurrentviewdrawing.md)
  A Boolean value that indicates whether the window allows multithreaded view drawing.
### Window Animation
- [var animationBehavior: NSWindow.AnimationBehavior](nswindow/animationbehavior-swift.property.md)
  The window’s automatic animation behavior.
### Updating Windows
- [func disableScreenUpdatesUntilFlush()](nswindow/disablescreenupdatesuntilflush.md)
  Disables the window’s screen updates until the window is flushed.
- [func update()](nswindow/update.md)
  Updates the window.
### Dragging Items
- [func drag(NSImage, at: NSPoint, offset: NSSize, event: NSEvent, pasteboard: NSPasteboard, source: Any, slideBack: Bool)](nswindow/drag(_:at:offset:event:pasteboard:source:slideback:).md)
  Begins a dragging session.
- [func registerForDraggedTypes([NSPasteboard.PasteboardType])](nswindow/registerfordraggedtypes(_:).md)
  Registers a set of pasteboard types that the window accepts as the destination of an image-dragging session.
- [func unregisterDraggedTypes()](nswindow/unregisterdraggedtypes.md)
  Unregisters the window as a possible destination for dragging operations.
### Accessing Edited Status
- [var isDocumentEdited: Bool](nswindow/isdocumentedited.md)
  A Boolean value that indicates whether the window’s document has been edited.
### Converting Coordinates
- [var backingScaleFactor: CGFloat](nswindow/backingscalefactor.md)
  The backing scale factor.
- [func backingAlignedRect(NSRect, options: AlignmentOptions) -> NSRect](nswindow/backingalignedrect(_:options:).md)
  Returns a backing store pixel-aligned rectangle in window coordinates.
- [func convertFromBacking(NSRect) -> NSRect](nswindow/convertfrombacking(_:).md)
  Converts a rectangle from its pixel-aligned backing store coordinate system to the window’s coordinate system.
- [func convertFromScreen(NSRect) -> NSRect](nswindow/convertfromscreen(_:).md)
  Converts a rectangle from the screen coordinate system to the window’s coordinate system.
- [func convertPointFromBacking(NSPoint) -> NSPoint](nswindow/convertpointfrombacking(_:).md)
  Converts a point from its pixel-aligned backing store coordinate system to the window’s coordinate system.
- [func convertPoint(fromScreen: NSPoint) -> NSPoint](nswindow/convertpoint(fromscreen:).md)
  Converts a point from the screen coordinate system to the window’s coordinate system.
- [func convertToBacking(NSRect) -> NSRect](nswindow/converttobacking(_:).md)
  Converts a rectangle from the window’s coordinate system to its pixel-aligned backing store coordinate system.
- [func convertToScreen(NSRect) -> NSRect](nswindow/converttoscreen(_:).md)
  Converts a rectangle to the screen coordinate system from the window’s coordinate system.
- [func convertPointToBacking(NSPoint) -> NSPoint](nswindow/convertpointtobacking(_:).md)
  Converts a point from the window’s coordinate system to its pixel-aligned backing store coordinate system.
- [func convertPoint(toScreen: NSPoint) -> NSPoint](nswindow/convertpoint(toscreen:).md)
  Converts a point to the screen coordinate system from the window’s coordinate system.
### Managing Titles
- [var title: String](nswindow/title.md)
  The string that appears in the title bar of the window or the path to the represented file.
- [var subtitle: String](nswindow/subtitle.md)
  A secondary line of text that appears in the title bar of the window.
- [var titleVisibility: NSWindow.TitleVisibility](nswindow/titlevisibility-swift.property.md)
  A value that indicates the visibility of the window’s title and title bar buttons.
- [func setTitleWithRepresentedFilename(String)](nswindow/settitlewithrepresentedfilename(_:).md)
  Sets a given path as the window’s title, formatting it as a file-system path, and records this path as the window’s associated file.
- [var representedFilename: String](nswindow/representedfilename.md)
  The path to the file of the window’s represented file.
- [var representedURL: URL?](nswindow/representedurl.md)
  The URL of the file the window represents.
### Accessing Screen Information
- [var screen: NSScreen?](nswindow/screen.md)
  The screen the window is on.
- [var deepestScreen: NSScreen?](nswindow/deepestscreen.md)
  The deepest screen the window is on (it may be split over several screens).
- [var displaysWhenScreenProfileChanges: Bool](nswindow/displayswhenscreenprofilechanges.md)
  A Boolean value that indicates whether the window context should be updated when the screen profile changes or when the window moves to a different screen.
### Moving Windows
- [var isMovableByWindowBackground: Bool](nswindow/ismovablebywindowbackground.md)
  A Boolean value that indicates whether the window is movable by clicking and dragging anywhere in its background.
- [var isMovable: Bool](nswindow/ismovable.md)
  A Boolean value that indicates whether the window can be dragged by clicking in its title bar or background.
- [func center()](nswindow/center.md)
  Sets the window’s location to the center of the screen.
### Closing Windows
- [func performClose(Any?)](nswindow/performclose(_:).md)
  Simulates the user clicking the close button by momentarily highlighting the button and then closing the window.
- [func close()](nswindow/close.md)
  Removes the window from the screen.
- [var isReleasedWhenClosed: Bool](nswindow/isreleasedwhenclosed.md)
  A Boolean value that indicates whether the window is released when it receives the `close` message.
### Minimizing Windows
- [var isMiniaturized: Bool](nswindow/isminiaturized.md)
  A Boolean value that indicates whether the window is minimized.
- [func performMiniaturize(Any?)](nswindow/performminiaturize(_:).md)
  Simulates the user clicking the minimize button by momentarily highlighting the button, then minimizing the window.
- [func miniaturize(Any?)](nswindow/miniaturize(_:).md)
  Removes the window from the screen list and displays the minimized window in the Dock.
- [func deminiaturize(Any?)](nswindow/deminiaturize(_:).md)
  De-minimizes the window.
- [var miniwindowImage: NSImage?](nswindow/miniwindowimage.md)
  The custom miniaturized window image of the window.
- [var miniwindowTitle: String!](nswindow/miniwindowtitle.md)
  The title displayed in the window’s minimized window.
### Getting the Dock Tile
- [var dockTile: NSDockTile](nswindow/docktile.md)
  The application’s Dock tile.
### Printing Windows
- [func printWindow(Any?)](nswindow/printwindow(_:).md)
  Runs the Print panel, and if the user chooses an option other than canceling, prints the window (its frame view and all subviews).
- [func dataWithEPS(inside: NSRect) -> Data](nswindow/datawitheps(inside:).md)
  Returns EPS data that draws the region of the window within a given rectangle.
- [func dataWithPDF(inside: NSRect) -> Data](nswindow/datawithpdf(inside:).md)
  Returns PDF data that draws the region of the window within a given rectangle.
### Providing Services
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](nswindow/validrequestor(forsendtype:returntype:).md)
  Searches for an object that responds to a Services request.
### Triggering Constraint-Based Layout
- [func updateConstraintsIfNeeded()](nswindow/updateconstraintsifneeded.md)
  Updates the constraints based on changes to views in the window since the last layout.
- [func layoutIfNeeded()](nswindow/layoutifneeded.md)
  Updates the layout of views in the window based on the current views and constraints.
### Debugging Constraint-Based Layout
- [func visualizeConstraints([NSLayoutConstraint]?)](nswindow/visualizeconstraints(_:).md)
  Displays a visual representation of the supplied constraints in the window.
### Constraint-Based Layouts
- [func anchorAttribute(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Attribute](nswindow/anchorattribute(for:).md)
  Returns the part of the window that stays stationary during constraint-based layout.
- [func setAnchorAttribute(NSLayoutConstraint.Attribute, for: NSLayoutConstraint.Orientation)](nswindow/setanchorattribute(_:for:).md)
  Sets the part of the window that stays stationary during constraint-based layout.
### Working with Window Depths
- [var bitsPerPixel: Int](nswindow/depth/bitsperpixel.md)
  Returns the bits per pixel for the specified window depth.
- [var bitsPerSample: Int](nswindow/depth/bitspersample.md)
  Returns the bits per sample for the specified window depth.
- [var colorSpaceName: NSColorSpaceName?](nswindow/depth/colorspacename.md)
  Returns the name of the color space corresponding to the passed window depth.
- [var numberOfColorComponents: Int](nscolorspacename/numberofcolorcomponents.md)
  Returns the number of color components in the specified color space.
- [var isPlanar: Bool](nswindow/depth/isplanar.md)
  Returns whether the specified window depth is planar.
- [func canRepresent(NSDisplayGamut) -> Bool](nswindow/canrepresent(_:).md)
  A Boolean value that indicates if the window and its screen use a color space that can represent the specified display gamut.
### Getting Information About Scripting Attributes
- [var hasCloseBox: Bool](nswindow/hasclosebox.md)
  A Boolean value that indicates if the window has a close box.
- [var hasTitleBar: Bool](nswindow/hastitlebar.md)
  A Boolean value that indicates if the window has a title bar.
- [var isModalPanel: Bool](nswindow/ismodalpanel.md)
  A Boolean value that indicates whether the window is a modal panel.
- [var isFloatingPanel: Bool](nswindow/isfloatingpanel.md)
  A Boolean value that indicates whether the window is a floating panel.
- [var isZoomable: Bool](nswindow/iszoomable.md)
  A Boolean value that indicates whether the window allows zooming.
- [var isResizable: Bool](nswindow/isresizable.md)
  A Boolean value that indicates if the user can resize the window.
- [var isMiniaturizable: Bool](nswindow/isminiaturizable.md)
  A Boolean value that indicates whether the window can minimize.
- [var orderedIndex: Int](nswindow/orderedindex.md)
  The zero-based position of the window, based on its order from front to back among all visible application windows.
### Setting Scripting Attributes
- [func setIsMiniaturized(Bool)](nswindow/setisminiaturized(_:).md)
  Sets the window’s miniaturized state to the value you specify.
- [func setIsVisible(Bool)](nswindow/setisvisible(_:).md)
  Sets the window’s visible state to the value you specify.
- [func setIsZoomed(Bool)](nswindow/setiszoomed(_:).md)
  Sets the window’s zoomed state to the value you specify.
### Handling Script Commands
- [func handleClose(NSCloseCommand) -> Any?](nswindow/handleclose(_:).md)
  Handles the AppleScript command to close the window (and its associated document, if any).
- [func handlePrint(NSScriptCommand) -> Any?](nswindow/handleprint(_:).md)
  Handles the AppleScript command to print the contents of the window (or its associated document, if any).
- [func handleSave(NSScriptCommand) -> Any?](nswindow/handlesave(_:).md)
  Handles the AppleScript command to save the window (and its associated document, if any).
### Constants
- [NSWindow.SelectionDirection](nswindow/selectiondirection.md)
  Constants that specify the direction a window is currently using to change the key view.
- [NSWindow.ButtonType](nswindow/buttontype.md)
  Constants that provide a way to access standard title bar buttons.
- [NSRunLoop—Ordering Modes for NSWindow](nsrunloop-ordering-modes-for-nsw.md)
  Constants that specify the priority for runloop messages.
- [NSWindow.Depth](nswindow/depth.md)
  A type that represents the depth, or amount of memory, for a single pixel in a window or screen.
- [NSWindow.BackingStoreType](nswindow/backingstoretype.md)
  Constants that specify how the window device buffers the drawing done in a window.
- [NSWindow.OrderingMode](nswindow/orderingmode.md)
  Constants that let you specify how a window is ordered relative to another window.
- [NSWindow.SharingType](nswindow/sharingtype-swift.enum.md)
  Constants that represent the access levels other processes can have to a window’s content.
- [NSWindow.NumberListOptions](nswindow/numberlistoptions.md)
  Options to use when retrieving window numbers from the system.
- [NSWindow.AnimationBehavior](nswindow/animationbehavior-swift.enum.md)
  Constants that control the automatic window animation behavior windows use when ordering to the front or out of view.
- [NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.struct.md)
  Window collection behaviors related to Mission Control, Spaces, and Stage Manager.
- [NSWindow.OcclusionState](nswindow/occlusionstate-swift.struct.md)
  Specifies whether the window is occluded.
- [NSWindow.TitleVisibility](nswindow/titlevisibility-swift.enum.md)
  Specifies the appearance of the window’s title bar area.
- [NSWindow.UserTabbingPreference](nswindow/usertabbingpreference-swift.enum.md)
  A value that indicates the user’s preference for window tabbing.
- [NSWindow.TabbingMode](nswindow/tabbingmode-swift.enum.md)
  The preferred tabbing behavior of a window.
- [Application Kit Version for Deferred Window Display Support](application-kit-version-for-deferred-window-display-support.md)
  The version of the AppKit.framework containing a specific bug fix or capability.
- [Application Kit Version for Custom Sheet Position](application-kit-version-for-custom-sheet-position.md)
  The version of the AppKit.framework containing a specific bug fix or capability.
- [NSWindowDidChangeBackingPropertiesNotification User Info Properties](nswindowdidchangebackingpropertiesnotification-user-info-properties.md)
  These constants are values that are returned in the [`userInfo`](https://developer.apple.com/documentation/foundation/nsnotification/1409222-userinfo) dictionary of the [`didChangeBackingPropertiesNotification`](nswindow/didchangebackingpropertiesnotification.md).
### Notifications
- [class let didBecomeKeyNotification: NSNotification.Name](nswindow/didbecomekeynotification.md)
  A notification that the window object became the key window.
- [class let didBecomeMainNotification: NSNotification.Name](nswindow/didbecomemainnotification.md)
  A notification that the window object became the main window.
- [class let didChangeScreenNotification: NSNotification.Name](nswindow/didchangescreennotification.md)
  A notification that a portion of the window object’s frame moved onto or off of a screen.
- [class let didChangeScreenProfileNotification: NSNotification.Name](nswindow/didchangescreenprofilenotification.md)
  A notification that the screen containing the window changed.
- [class let didDeminiaturizeNotification: NSNotification.Name](nswindow/diddeminiaturizenotification.md)
  A notification that the window is no longer minimized.
- [class let didEndSheetNotification: NSNotification.Name](nswindow/didendsheetnotification.md)
  A notification that the window object closed an attached sheet.
- [class let didEndLiveResizeNotification: NSNotification.Name](nswindow/didendliveresizenotification.md)
  A notification that the user resized the window object.
- [class let didExposeNotification: NSNotification.Name](nswindow/didexposenotification.md)
  A notification that a window exposed a portion of its nonretained content.
- [class let didMiniaturizeNotification: NSNotification.Name](nswindow/didminiaturizenotification.md)
  A notification that the window object minimized.
- [class let didMoveNotification: NSNotification.Name](nswindow/didmovenotification.md)
  A notification that the window object moved.
- [class let didResignKeyNotification: NSNotification.Name](nswindow/didresignkeynotification.md)
  A notification that the window object resigned its status as key window.
- [class let didResignMainNotification: NSNotification.Name](nswindow/didresignmainnotification.md)
  A notification that the window object resigned its status as main window.
- [class let didResizeNotification: NSNotification.Name](nswindow/didresizenotification.md)
  A notification that the window object size changed.
- [class let didUpdateNotification: NSNotification.Name](nswindow/didupdatenotification.md)
  A notification that the window object received an update message.
- [class let willBeginSheetNotification: NSNotification.Name](nswindow/willbeginsheetnotification.md)
  A notification that the window object is about to open a sheet.
- [class let willCloseNotification: NSNotification.Name](nswindow/willclosenotification.md)
  A notification that the window object is about to close.
- [class let willMiniaturizeNotification: NSNotification.Name](nswindow/willminiaturizenotification.md)
  A notification that the window object is about to minimize.
- [class let willMoveNotification: NSNotification.Name](nswindow/willmovenotification.md)
  A notification that the window object is about to move.
- [class let willStartLiveResizeNotification: NSNotification.Name](nswindow/willstartliveresizenotification.md)
  A notification that the user is about to resize the window.
- [class let willEnterFullScreenNotification: NSNotification.Name](nswindow/willenterfullscreennotification.md)
  A notification that the window will enter full-screen mode.
- [class let didEnterFullScreenNotification: NSNotification.Name](nswindow/didenterfullscreennotification.md)
  A notification that the window entered full-screen mode.
- [class let willExitFullScreenNotification: NSNotification.Name](nswindow/willexitfullscreennotification.md)
  A notification that the window object will exit full-screen mode.
- [class let didExitFullScreenNotification: NSNotification.Name](nswindow/didexitfullscreennotification.md)
  A notification that the window object exited full-screen mode.
- [class let willEnterVersionBrowserNotification: NSNotification.Name](nswindow/willenterversionbrowsernotification.md)
  A notification that the window object will enter version browser mode.
- [class let didEnterVersionBrowserNotification: NSNotification.Name](nswindow/didenterversionbrowsernotification.md)
  A notification that the window object entered version browser mode.
- [class let willExitVersionBrowserNotification: NSNotification.Name](nswindow/willexitversionbrowsernotification.md)
  A notification that the window object will exit version browser mode.
- [class let didExitVersionBrowserNotification: NSNotification.Name](nswindow/didexitversionbrowsernotification.md)
  A notification that the window object exited version browser mode.
- [class let didChangeBackingPropertiesNotification: NSNotification.Name](nswindow/didchangebackingpropertiesnotification.md)
  A notification that the window object backing properties changed.
- [class let didChangeOcclusionStateNotification: NSNotification.Name](nswindow/didchangeocclusionstatenotification.md)
  A notification that the window object’s occlusion state changed.
### Deprecated
- [Deprecated Symbols](nswindow-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Instance Properties
- [var cascadingReferenceFrame: NSRect](nswindow/cascadingreferenceframe.md)
### Instance Methods
- [func beginDraggingSession(items: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession](nswindow/begindraggingsession(items:event:source:).md)
- [func javaAdd(toOrderingGroup: NSWindow!)](nswindow/javaadd(toorderinggroup:).md)
- [func javaRemove(fromOrderingGroup: NSWindow!)](nswindow/javaremove(fromorderinggroup:).md)
- [func requestSharingOfWindow(NSWindow, completionHandler: ((any Error)?) -> Void)](nswindow/requestsharingofwindow(_:completionhandler:).md)
- [func requestSharingOfWindow(usingPreview: NSImage, title: String, completionHandler: ((any Error)?) -> Void)](nswindow/requestsharingofwindow(usingpreview:title:completionhandler:).md)

## Relationships

### Inherits From
- [NSResponder](nsresponder.md)
### Inherited By
- [NSPanel](nspanel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSMenuItemValidation](nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](nsuserinterfacevalidations.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSPanel](nspanel.md)
  A special kind of window that typically performs a function that is auxiliary to the main window.
- [protocol NSWindowDelegate](nswindowdelegate.md)
  A set of optional methods that a window’s delegate can implement to respond to events, such as window resizing, moving, exposing, and minimizing.
- [class NSWindowTab](nswindowtab.md)
  A tab associated with a window that is part of a tabbing group.
- [class NSWindowTabGroup](nswindowtabgroup.md)
  A group of windows that display together as a single tabbed window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow)*