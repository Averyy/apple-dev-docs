# NSResponder

**Framework**: AppKit  
**Kind**: class

An abstract class that forms the basis of event and command processing in AppKit.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSResponder
```

#### Overview

The core classes—[`NSApplication`](nsapplication.md), [`NSWindow`](nswindow.md), and [`NSView`](nsview.md)—inherit from [`NSResponder`](nsresponder.md), as must any class that handles events. The responder model uses three components: event messages, action messages, and the responder chain.

[`NSResponder`](nsresponder.md) also plays an important role in the presentation of error information. The default implementations of the [`presentError(_:)`](nsresponder/presenterror(_:).md) and [`presentError(_:modalFor:delegate:didPresent:contextInfo:)`](nsresponder/presenterror(_:modalfor:delegate:didpresent:contextinfo:).md) methods send [`willPresentError(_:)`](nsresponder/willpresenterror(_:).md) to `self`, thereby giving subclasses the opportunity to customize the localized information presented in error alerts. `NSResponder` then forwards the message to the next responder, passing it the customized [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object. The exact path up the modified responder chain depends on the type of application window:

- Window that the document owns: view > superviews > window > window controller > document object > document controller > the application object
- Window with window controller but no documents: view > superviews > window > window controller > the application object
- Window with no window controllers: view > superviews > window > the application object

[`NSApplication`](nsapplication.md) displays a document-modal error alert and, if the error object has a recovery attempter, gives it a chance to recover from the error. A recovery attempter is an object that conforms to the [`NSErrorRecoveryAttempting`](https://developer.apple.com/documentation/Foundation/nserrorrecoveryattempting) informal protocol.

> **Note**:  In macOS 10.15 and later, [`NSResponder`](nsresponder.md) and its descendants call the [`dealloc`](https://developer.apple.com/documentation/objectivec/nsobject/1571947-dealloc) method on the main thread. This method helps to avoid situations where an asynchronous block unexpectedly deallocates an object on a background queue.

## Topics

### Changing the First Responder
- [var acceptsFirstResponder: Bool](nsresponder/acceptsfirstresponder.md)
  A Boolean value that indicates whether the responder accepts first responder status.
- [func becomeFirstResponder() -> Bool](nsresponder/becomefirstresponder.md)
  Notifies the receiver that it’s about to become first responder in its [`NSWindow`](nswindow.md).
- [func resignFirstResponder() -> Bool](nsresponder/resignfirstresponder.md)
  Notifies the receiver that it’s been asked to relinquish its status as first responder in its window.
- [func validateProposedFirstResponder(NSResponder, for: NSEvent?) -> Bool](nsresponder/validateproposedfirstresponder(_:for:).md)
  Allows controls to determine when they should become first responder.
### Managing the Next Responder
- [var nextResponder: NSResponder?](nsresponder/nextresponder.md)
  The next responder after this one, or `nil` if it has none.
### Responding to Mouse Events
- [func mouseDown(with: NSEvent)](nsresponder/mousedown(with:).md)
  Informs the receiver that the user has pressed the left mouse button.
- [func mouseDragged(with: NSEvent)](nsresponder/mousedragged(with:).md)
  Informs the receiver that the user has moved the mouse with the left button pressed.
- [func mouseUp(with: NSEvent)](nsresponder/mouseup(with:).md)
  Informs the receiver that the user has released the left mouse button.
- [func mouseMoved(with: NSEvent)](nsresponder/mousemoved(with:).md)
  Informs the receiver that the mouse has moved.
- [func mouseEntered(with: NSEvent)](nsresponder/mouseentered(with:).md)
  Informs the receiver that the cursor has entered a tracking rectangle.
- [func mouseExited(with: NSEvent)](nsresponder/mouseexited(with:).md)
  Informs the receiver that the cursor has exited a tracking rectangle.
- [func rightMouseDown(with: NSEvent)](nsresponder/rightmousedown(with:).md)
  Informs the receiver that the user has pressed the right mouse button.
- [func rightMouseDragged(with: NSEvent)](nsresponder/rightmousedragged(with:).md)
  Informs the receiver that the user has moved the mouse with the right button pressed.
- [func rightMouseUp(with: NSEvent)](nsresponder/rightmouseup(with:).md)
  Informs the receiver that the user has released the right mouse button.
- [func otherMouseDown(with: NSEvent)](nsresponder/othermousedown(with:).md)
  Informs the receiver that the user has pressed a mouse button other than the left or right one.
- [func otherMouseDragged(with: NSEvent)](nsresponder/othermousedragged(with:).md)
  Informs the receiver that the user has moved the mouse with a button other than the left or right button pressed.
- [func otherMouseUp(with: NSEvent)](nsresponder/othermouseup(with:).md)
  Informs the receiver that the user has released a mouse button other than the left or right button.
### Responding to Key Events
- [func keyDown(with: NSEvent)](nsresponder/keydown(with:).md)
  Informs the receiver that the user has pressed a key.
- [func keyUp(with: NSEvent)](nsresponder/keyup(with:).md)
  Informs the receiver that the user has released a key.
- [func interpretKeyEvents([NSEvent])](nsresponder/interpretkeyevents(_:).md)
  Handles a series of key events.
- [func performKeyEquivalent(with: NSEvent) -> Bool](nsresponder/performkeyequivalent(with:).md)
  Handle a key equivalent.
- [func flushBufferedKeyEvents()](nsresponder/flushbufferedkeyevents.md)
  Clears any unprocessed key events when overridden by subclasses.
### Responding to Pressure Changes
- [func pressureChange(with: NSEvent)](nsresponder/pressurechange(with:).md)
  Indicates a pressure change as the result of a user input event on a system that supports pressure sensitivity.
### Responding to Other Kinds of Events
- [func cursorUpdate(with: NSEvent)](nsresponder/cursorupdate(with:).md)
  Informs the receiver that the mouse cursor has moved into a cursor rectangle.
- [func flagsChanged(with: NSEvent)](nsresponder/flagschanged(with:).md)
  Informs the receiver that the user has pressed or released a modifier key (Shift, Control, and so on).
- [func tabletPoint(with: NSEvent)](nsresponder/tabletpoint(with:).md)
  Informs the receiver that a tablet-point event has occurred.
- [func tabletProximity(with: NSEvent)](nsresponder/tabletproximity(with:).md)
  Informs the receiver that a tablet-proximity event has occurred.
- [func helpRequested(NSEvent)](nsresponder/helprequested(_:).md)
  Displays context-sensitive help for the receiver if help has been registered.
- [func scrollWheel(with: NSEvent)](nsresponder/scrollwheel(with:).md)
  Informs the receiver that the mouse’s scroll wheel has moved.
- [func quickLook(with: NSEvent)](nsresponder/quicklook(with:).md)
  Performs a Quick Look on the content at the location specified by the supplied event.
- [func changeMode(with: NSEvent)](nsresponder/changemode(with:).md)
  Informs the responder that performed a double-tap on the side of an Apple Pencil.
### Responding to Action Messages
- [func supplementalTarget(forAction: Selector, sender: Any?) -> Any?](nsresponder/supplementaltarget(foraction:sender:).md)
  Finds a target for an action method.
- [protocol NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
  Methods that responder subclasses implement to support key binding commands, such as inserting tabs and newlines, or moving the insertion point.
- [Action Messages](action-messages.md)
  Implement action messages in your first responders to handle common tasks.
### Handling Window Restoration
- [class func allowedClasses(forRestorableStateKeyPath: String) -> [AnyClass]](nsresponder/allowedclasses(forrestorablestatekeypath:).md)
  Returns the classes that support secure coding.
- [func encodeRestorableState(with: NSCoder)](nsresponder/encoderestorablestate(with:).md)
  Saves the interface-related state of the responder.
- [func encodeRestorableState(with: NSCoder, backgroundQueue: OperationQueue)](nsresponder/encoderestorablestate(with:backgroundqueue:).md)
  Saves the interface-related state of the responder to a keyed archiver either synchronously or asynchronously on the given operation queue.
- [func restoreState(with: NSCoder)](nsresponder/restorestate(with:).md)
  Restores the interface-related state of the responder.
- [class var restorableStateKeyPaths: [String]](nsresponder/restorablestatekeypaths.md)
  Returns an array of key paths representing the restorable attributes of the responder.
- [func invalidateRestorableState()](nsresponder/invalidaterestorablestate.md)
  Marks the responder’s interface-related state as dirty.
### Supporting User Activities
- [var userActivity: NSUserActivity?](nsresponder/useractivity.md)
  An object encapsulating a user activity supported by this responder.
- [func updateUserActivityState(NSUserActivity)](nsresponder/updateuseractivitystate(_:).md)
  Updates the state of the given user activity.
### Presenting and Customizing Error Information
- [func presentError(any Error) -> Bool](nsresponder/presenterror(_:).md)
  Presents an error alert to the user as an application-modal dialog.
- [func presentError(any Error, modalFor: NSWindow, delegate: Any?, didPresent: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsresponder/presenterror(_:modalfor:delegate:didpresent:contextinfo:).md)
  Presents an error alert to the user as a document-modal sheet attached to document window.
- [func willPresentError(any Error) -> any Error](nsresponder/willpresenterror(_:).md)
  Returns a custom version of the supplied error object that’s more suitable for presentation in alert sheets and dialogs.
### Dispatching Messages
- [func tryToPerform(Selector, with: Any?) -> Bool](nsresponder/trytoperform(_:with:).md)
  Attempts to perform the method indicated by an action with a specified argument.
### Managing a Responder’s Menu
- [var menu: NSMenu?](nsresponder/menu.md)
  Returns the responder’s menu.
### Updating the Services Menu
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](nsresponder/validrequestor(forsendtype:returntype:).md)
  Overridden by subclasses to determine what services are available.
### Getting the Undo Manager
- [var undoManager: UndoManager?](nsresponder/undomanager.md)
  The undo manager for this responder.
### Testing Events
- [func shouldBeTreatedAsInkEvent(NSEvent) -> Bool](nsresponder/shouldbetreatedasinkevent(_:).md)
  Indicates whether a pen-down event should be treated as an ink event.
### Terminating the Responder Chain
- [func noResponder(for: Selector)](nsresponder/noresponder(for:).md)
  Handles the case where an event or action message falls off the end of the responder chain.
### Touch and Gesture Events
- [func beginGesture(with: NSEvent)](nsresponder/begingesture(with:).md)
  Informs the receiver that the user has begun a touch gesture.
- [func endGesture(with: NSEvent)](nsresponder/endgesture(with:).md)
  Informs the receiver that the user has ended a touch gesture.
- [func magnify(with: NSEvent)](nsresponder/magnify(with:).md)
  Informs the receiver that the user has begun a pinch gesture.
- [func rotate(with: NSEvent)](nsresponder/rotate(with:).md)
  Informs the receiver that the user has begun a rotation gesture.
- [func swipe(with: NSEvent)](nsresponder/swipe(with:).md)
  Informs the receiver that the user has begun a swipe gesture.
- [func touchesBegan(with: NSEvent)](nsresponder/touchesbegan(with:).md)
  Informs the receiver that new set of touches has been recognized.
- [func touchesMoved(with: NSEvent)](nsresponder/touchesmoved(with:).md)
  Informs the receiver that one or more touches has moved.
- [func touchesCancelled(with: NSEvent)](nsresponder/touchescancelled(with:).md)
  Informs the receiver that tracking of touches has been cancelled for any reason.
- [func touchesEnded(with: NSEvent)](nsresponder/touchesended(with:).md)
  Returns that a set of touches have been removed.
- [func wantsForwardedScrollEvents(for: NSEvent.GestureAxis) -> Bool](nsresponder/wantsforwardedscrollevents(for:).md)
  Returns whether to forward elastic scrolling gesture events up the responder.
- [func smartMagnify(with: NSEvent)](nsresponder/smartmagnify(with:).md)
  Informs the receiver that the user performed a smart zoom gesture.
- [func wantsScrollEventsForSwipeTracking(on: NSEvent.GestureAxis) -> Bool](nsresponder/wantsscrolleventsforswipetracking(on:).md)
  Implement this method to track gesture scroll events such as a swipe.
- [NSEvent.GestureAxis](nsevent/gestureaxis.md)
  Constants that specify the direction of travel for a gesture.
### Supporting the Touch Bar
- [var touchBar: NSTouchBar?](nsresponder/touchbar.md)
  The [`NSTouchBar`](nstouchbar.md) object associated with the responder.
- [func makeTouchBar() -> NSTouchBar?](nsresponder/maketouchbar.md)
  Your custom subclass of the `NSResponder` class should override this method to create and configure your subclass’s default [`NSTouchBar`](nstouchbar.md) object.
### Performing Text Find Actions
- [func performTextFinderAction(Any?)](nsresponder/performtextfinderaction(_:).md)
  Performs all find oriented actions.
### Supporting Tabbed Windows
- [func newWindowForTab(Any?)](nsresponder/newwindowfortab(_:).md)
  Creates a new window to show as a tab in a tabbed window.
### Creating Responders
- [init()](nsresponder/init.md)
  Creates a new responder object.
- [init?(coder: NSCoder)](nsresponder/init(coder:).md)
  Creates a new responder object with data in an unarchiver.
### Instance Methods
- [func contextMenuKeyDown(NSEvent)](nsresponder/contextmenukeydown(_:).md)
- [func mouseCancelled(with: NSEvent)](nsresponder/mousecancelled(with:).md)
- [func showWritingTools(Any?)](nsresponder/showwritingtools(_:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSApplication](nsapplication.md)
- [NSDrawer](nsdrawer.md)
- [NSPopover](nspopover.md)
- [NSView](nsview.md)
- [NSViewController](nsviewcontroller.md)
- [NSWindow](nswindow.md)
- [NSWindowController](nswindowcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder)*