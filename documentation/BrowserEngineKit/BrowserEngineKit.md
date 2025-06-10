# BrowserEngineKit

**Framework**: BrowserEngineKit  
**Kind**: module

Create a browser that renders content using an alternative browser engine.

**Availability**:
- iOS 17.4+
- iPadOS 18.0+

#### Overview

A web browser loads content and code from remote — and potentially untrusted — servers. Design your browser app to isolate access to operating system resources, the data of the person using the app, and untrusted data from the web. Code defensively to reduce the risk posed by vulnerabilities in your browser code.

If you use [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) to render web content in your browser app, WebKit automatically distributes its work to extensions that isolate their access to important resources and data.

Whether you use [`WebKit`](https://developer.apple.com/documentation/WebKit) or write your own alternative browser engine, you need to request the entitlement to act as a person’s default web browser. For more information, see [`Preparing your app to be the default web browser`](https://developer.apple.com/documentation/Xcode/preparing-your-app-to-be-the-default-browser).

##### Build a Multi Process Browser

If you use an alternative browser engine in your app, you must design your secure browser infrastructure to separate different components into extensions that your browser manages. Design a limited inter-process communication (IPC) protocol that coordinates work across the extensions. Separating your alternative browser engine into distinct extensions limits the impact of security vulnerabilities in any one process.

For more information on designing your browser extensions, see [`Designing your browser architecture`](designing-your-browser-architecture.md). For information on using the extensions in your browser, see [`Managing the browser extension life cycle`](managing-the-browser-extension-lifecycle.md).

##### Render Websites

Your browser app can get significant benefits by integrating closely with UIKit. You can customize the way your app handles many low-level user interface events, ensure that your browser app correctly renders CSS, and that it properly manipulates the Javascript DOM. You can use view classes in [`BrowserEngineKit`](BrowserEngineKit.md) to handle scrolling, drag interactions, and the context menu in your browser app.

For information on integrating a custom text view with the UIKit text system, see [`Integrating custom browser text views with UIKit`](integrating-custom-browser-text-views-with-uikit.md).

In your browser app, launch extensions as the person browses web content to make network requests, load the web content, and render media. For more information, see [`Managing the browser extension life cycle`](managing-the-browser-extension-lifecycle.md). Use [`XPC`](https://developer.apple.com/documentation/XPC) to communicate between your browser app and extension processes. For more information, see [`Using XPC to communicate with browser extensions`](using-xpc-to-communicate-with-browser-extensions.md).

For information on installing alternative app marketplaces from their company websites within your browser app, see [`Enabling alternative distribution app installation in a browser`](https://developer.apple.com/documentation/appdistribution/enabling-alternative-distribution-app-installation-in-a-browser).

> ❗ **Important**:  To distribute an app that uses an alternative browser engine, you need to request the relevant entitlements for your developer account. For more information and to request the entitlements, see [`Using alternative browser engines in the European Union`](https://developer.apple.comhttps://developer.apple.com/support/alternative-browser-engines).

## Topics

### Essentials
- [Developing a browser app that uses an alternative browser engine](developing-a-browser-app-that-uses-an-alternative-browser-engine.md)
  Create a web browser app and associated extensions.
- [Designing your browser architecture](designing-your-browser-architecture.md)
  Isolate privileged access to operating system resources and private data from untrusted code.
- [Preparing your app to be the default web browser](../Xcode/preparing-your-app-to-be-the-default-browser.md)
  Configure your browser app so users can set it as the default on their device instead of Safari.
### Browser extensions
- [Creating browser extensions in Xcode](creating-browser-extensions-in-xcode.md)
  Configure your Xcode project to support your alternative browser engine.
- [Extension lifecycle](extension-lifecycle.md)
  Launch, communicate with, and invalidate browser extensions.
- [Extension resources](extension-resources.md)
  Control access to files and memory in browser extensions.
### Web content
- [View coordination](view-coordination.md)
  Display content in the browser’s UI that an extension renders.
- [Text interaction](text-interaction.md)
  Integrate your web browser engine asynchronously with the text system.
- [class BEWebAppManifest](bewebappmanifest.md)
  An object that represents a web app manifest.
### Scroll view interaction
- [class BEScrollView](bescrollview.md)
  A scroll view that works with its delegate to handle nesting, and customize scroll interactions.
- [class BEScrollViewScrollUpdate](bescrollviewscrollupdate.md)
  An object that represents a change in a scroll view’s scroll state.
- [protocol BEScrollViewDelegate](bescrollviewdelegate.md)
  The protocol that browser scroll view delegates conform to.
### Drag interaction
- [class BEDragInteraction](bedraginteraction.md)
  A `UIDragInteraction` subclass with features specific to browsers to enable asynchronous preparations and behaviours.
- [protocol BEDragInteractionDelegate](bedraginteractiondelegate.md)
  A protocol to which the drag interaction delegates conform.
### Context menus
- [class BEContextMenuConfiguration](becontextmenuconfiguration.md)
  A specialized `UIContextMenuConfiguration` object to defer a context menu presentation when the when the context menu gestures are first recognized and a possible menu presentation is not immediately known.
### Accessibility
- [protocol BEAccessibilityTextMarkerSupport](beaccessibilitytextmarkersupport.md)
  A set of methods that provide information about text offsets to support assistive features.
- [static var valueChangedNotification: UIAccessibility.Notification](beaccessibility/valuechangednotification.md)
  The notification you post when the value of an element changes.
- [static var selectionChangedNotification: UIAccessibility.Notification](beaccessibility/selectionchangednotification.md)
  The notification you post when the selection inside an element changes.
- [struct BEAccessibilityContainerType](beaccessibilitycontainertype.md)
  An enumeration that indicates the type of container in which an element is located.
- [enum BEAccessibilityPressedState](beaccessibilitypressedstate.md)
  An enumeration that indicates whether an element is pressed.
- [static var menuItem: UIAccessibilityTraits](beaccessibility/menuitem.md)
  The accessibility element behaves like a menu item.
- [static var popUpButton: UIAccessibilityTraits](beaccessibility/popupbutton.md)
  The accessibility element behaves like a pop-up button.
- [static var radioButton: UIAccessibilityTraits](beaccessibility/radiobutton.md)
  The accessibility element behaves like a radio button.
- [static var readOnly: UIAccessibilityTraits](beaccessibility/readonly.md)
  The accessibility element is read-only.
- [static var visited: UIAccessibilityTraits](beaccessibility/visited.md)
  The accessibility element behaves like a link that someone previously visited.
### Just-in-time code compilation
- [Protecting code compiled just in time](protecting-code-compiled-just-in-time.md)
  Toggle memory between being writable and executable.
- [Improving control flow integrity with pointer authentication](../Apple-Silicon/improving-control-flow-integrity-with-pointer-authentication.md)
  Increase confidence that your code uses pointers correctly.
- [var BE_JIT_WRITE_PROTECT_TAG: Int { get }](../BrowserEngineCore/BE_JIT_WRITE_PROTECT_TAG.md)
  A discriminator value the system uses to generate pointer authentication codes for just-in-time compilation.
### Downloads
- [Downloading files in a web browser with an alternative browser engine](downloading-files-in-a-web-browser.md)
  Report download progress to the system to keep your networking extension active.
- [class BEDownloadMonitor](bedownloadmonitor-9bwls.md)
  An object that reports the status of web downloads to the system.
### Classes
- [class BEMediaEnvironment](bemediaenvironment-15xci.md)
- [class BEProcessCapability](beprocesscapability-76ijx.md)
### Protocols
- [protocol BEExtensionProcess](beextensionprocess.md)
### Structures
- [struct BEAccessibility](beaccessibility.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/BrowserEngineKit)*