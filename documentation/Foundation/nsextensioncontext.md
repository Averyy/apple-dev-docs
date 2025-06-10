# NSExtensionContext

**Framework**: Foundation  
**Kind**: class

The host app context from which an app extension is invoked.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSExtensionContext
```

#### Overview

When a host app sends a request to an app extension, it provides an extension context. For many app extensions, the most important part of the context is the data the user wants to work with, which is contained in the [`inputItems`](nsextensioncontext/inputitems.md) property.

## Topics

### Handling requests
- [func completeRequest(returningItems: [Any]?, completionHandler: ((Bool) -> Void)?)](nsextensioncontext/completerequest(returningitems:completionhandler:).md)
  Tells the host app to complete the app extension request with an array of result items.
- [func cancelRequest(withError: any Error)](nsextensioncontext/cancelrequest(witherror:).md)
  Tells the host app to cancel the app extension request, with a supplied error.
- [let NSExtensionItemsAndErrorsKey: String](nsextensionitemsanderrorskey.md)
  The extension items and errors key.
### Opening URLs
- [func open(URL, completionHandler: ((Bool) -> Void)?)](nsextensioncontext/open(_:completionhandler:).md)
  Asks the system to open a URL on behalf of the currently running app extension.
### Storing extension items
- [var inputItems: [Any]](nsextensioncontext/inputitems.md)
  The list of input [`NSExtensionItem`](nsextensionitem.md) objects associated with the context.
### Controlling media playback in notification content extensions
- [func mediaPlayingStarted()](nsextensioncontext/mediaplayingstarted.md)
  Tells the system that the Notification Content app extension began playing a media file.
- [func mediaPlayingPaused()](nsextensioncontext/mediaplayingpaused.md)
  Tells the system that the Notification Content app extension stopped playing a media file.
### Populating your share extension with metadata
- [var intent: INIntent?](nsextensioncontext/intent.md)
  Metadata for populating your share extensions interface.
### Getting Siri-related information
- [var hostedViewMinimumAllowedSize: CGSize](nsextensioncontext/hostedviewminimumallowedsize.md)
  The minimum size for a Siri hosted view.
- [var hostedViewMaximumAllowedSize: CGSize](nsextensioncontext/hostedviewmaximumallowedsize.md)
  The maximum size for a Siri hosted view.
- [func interfaceParametersDescription() -> String](nsextensioncontext/interfaceparametersdescription.md)
  Returns a human-readable string describing the data that SiriKit displays to the user when you handle an intent.
### Supporting broadcasting
- [func loadBroadcastingApplicationInfo(completion: (String, String, UIImage?) -> Void)](nsextensioncontext/loadbroadcastingapplicationinfo(completion:).md)
- [func completeRequest(withBroadcast: URL, setupInfo: [String : any NSCoding & NSObjectProtocol]?)](nsextensioncontext/completerequest(withbroadcast:setupinfo:).md)
### Handling notification actions
- [var notificationActions: [UNNotificationAction]](nsextensioncontext/notificationactions.md)
- [func performNotificationDefaultAction()](nsextensioncontext/performnotificationdefaultaction.md)
- [func dismissNotificationContentExtension()](nsextensioncontext/dismissnotificationcontentextension.md)
### Notifications
- [static let NSExtensionHostDidBecomeActive: NSNotification.Name](nsnotification/name-swift.struct/nsextensionhostdidbecomeactive.md)
  Posted when the extension’s host app moves from the inactive to the active state.
- [static let NSExtensionHostWillResignActive: NSNotification.Name](nsnotification/name-swift.struct/nsextensionhostwillresignactive.md)
  Posted when the extension’s host app moves from the active to the inactive state.
- [static let NSExtensionHostDidEnterBackground: NSNotification.Name](nsnotification/name-swift.struct/nsextensionhostdidenterbackground.md)
  Posted when the extension’s host app begins running in the background.
- [static let NSExtensionHostWillEnterForeground: NSNotification.Name](nsnotification/name-swift.struct/nsextensionhostwillenterforeground.md)
  Posted when the extension’s host app begins running in the foreground.
### Deprecated
- [func completeRequest(withBroadcast: URL, broadcastConfiguration: RPBroadcastConfiguration, setupInfo: [String : any NSCoding & NSObjectProtocol]?)](nsextensioncontext/completerequest(withbroadcast:broadcastconfiguration:setupinfo:).md)
  Tells the host app to complete the app extension request with the specified broadcast information.
- [var widgetActiveDisplayMode: NCWidgetDisplayMode](nsextensioncontext/widgetactivedisplaymode.md)
  The active display mode of the widget.
- [var widgetLargestAvailableDisplayMode: NCWidgetDisplayMode](nsextensioncontext/widgetlargestavailabledisplaymode.md)
  The largest display mode the widget supports.
- [func widgetMaximumSize(for: NCWidgetDisplayMode) -> CGSize](nsextensioncontext/widgetmaximumsize(for:).md)
  Returns the maximum size for the specified widget display mode.
### Structures
- [NSExtensionContext.DidBecomeActiveMessage](nsextensioncontext/didbecomeactivemessage.md)
- [NSExtensionContext.DidEnterBackgroundMessage](nsextensioncontext/didenterbackgroundmessage.md)
- [NSExtensionContext.WillEnterForegroundMessage](nsextensioncontext/willenterforegroundmessage.md)
- [NSExtensionContext.WillResignActiveMessage](nsextensioncontext/willresignactivemessage.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSExtensionRequestHandling](nsextensionrequesthandling.md)
  The interface an app extension uses to respond to a request from a host app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext)*