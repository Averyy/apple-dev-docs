# CPInterfaceController

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

The type you use to present your app’s CarPlay interface and change what appears on the vehicle’s display.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class CPInterfaceController
```

```objc
@interface CPInterfaceController : NSObject
```

## Mentions

- [Building your app’s initial CarPlay interface](./building-your-apps-initial-carplay-interface.md)

## Overview

When someone launches your app, CarPlay instantiates your app’s main scene so you can display your interface. Instead of creating your interface from views, you create it from system-provided templates, which specify how to lay out and present your content on the vehicle’s display. To display the templates you create, call the methods of the `CPInterfaceController` object your scene provides. The interface controller handles the presentation of your templates on the vehicle display, adjusting your content as needed to fit on different display sizes.

You don’t create a `CPInterfaceController` object directly. After creating your app’s main scene, the system delivers the interface controller to the scene’s delegate object. You can also retrieve the interface controller from the scene’s [`interfaceController`](./cptemplateapplicationscene/interfacecontroller.md) property at other times. Use only the provided interface controller to display the content for your app’s main scene.

CarPlay apps use a navigation-style interface, which uses a stack-based approach to manage your content. At startup, call the [`setRootTemplate(_:animated:completion:)`](./cpinterfacecontroller/setroottemplate%28_,animated,completion%29.md) method to install the template with your app’s main content. This template sits at the bottom of the stack and is the starting point for navigating your content. To navigate one level deeper into your content, call the interface controller’s [`pushTemplate(_:animated:completion:)`](./cpinterfacecontroller/pushtemplate%28_,animated,completion%29.md) method to push a new template onto the stack and display its content. To return to the previous template, call the [`popTemplate(animated:completion:)`](./cpinterfacecontroller/poptemplate%28animated,completion%29.md) method to remove the top-most template from the stack. You can pop any template off the stack except the root template.

In addition to displaying content in your app’s navigation interface, you can present specific templates modally or as an overlay. You can present action sheet, alert, and voice-control templates modally. You can also present the voice-control template using an overlay.

> **Note**: In navigation apps, dashboard and instrument cluster scenes present their content using [`CPDashboardController`](./cpdashboardcontroller.md) or [`CPInstrumentClusterController`](./cpinstrumentclustercontroller.md) types instead of `CPInterfaceControllerDelegate`.

## Topics

### Installing and removing templates
- [func setRootTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./cpinterfacecontroller/setroottemplate%28_,animated,completion%29.md)
  Installs the root template of your app’s navigation hierarchy.
- [func pushTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./cpinterfacecontroller/pushtemplate%28_,animated,completion%29.md)
  Adds the specified template to the navigation hierarchy and displays it.
- [func popTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./cpinterfacecontroller/poptemplate%28animated,completion%29.md)
  Removes the top-most template from your app’s navigation hierarchy.
- [func popToRootTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./cpinterfacecontroller/poptoroottemplate%28animated,completion%29.md)
  Removes all of the templates from your app’s navigation hierarchy except the root template.
- [func pop(to: CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./cpinterfacecontroller/pop%28to,animated,completion%29.md)
  Removes templates from your app’s navigation hierarchy until the specified template becomes visible.
### Responding to interface changes
- [var delegate: (any CPInterfaceControllerDelegate)?](./cpinterfacecontroller/delegate.md)
  A custom object you use to respond when templates appear and disappear.
- [protocol CPInterfaceControllerDelegate](./cpinterfacecontrollerdelegate.md)
  The methods you implement to observe the addition and removal of templates in your app’s interface.
### Configuring interface-related details
- [var prefersDarkUserInterfaceStyle: Bool](./cpinterfacecontroller/prefersdarkuserinterfacestyle.md)
  A Boolean value that indicates whether you prefer Dark Mode for your interface.
- [var carTraitCollection: UITraitCollection](./cpinterfacecontroller/cartraitcollection.md)
  The trait collection of the vehicle’s primary screen.
### Getting the current templates
- [var rootTemplate: CPTemplate](./cpinterfacecontroller/roottemplate.md)
  The root template in the navigation hierarchy.
- [var topTemplate: CPTemplate?](./cpinterfacecontroller/toptemplate.md)
  The top-most template in your app’s navigation hierarchy.
- [var templates: [CPTemplate]](./cpinterfacecontroller/templates.md)
  The templates currently in your app’s navigation hierarchy.
### Presenting a template modally
- [func presentTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./cpinterfacecontroller/presenttemplate%28_,animated,completion%29.md)
  Presents the template modally over your app’s navigation interface.
- [func dismissTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./cpinterfacecontroller/dismisstemplate%28animated,completion%29.md)
  Dismisses the template you previously presented modally.
- [var presentedTemplate: CPTemplate?](./cpinterfacecontroller/presentedtemplate.md)
  The current modally-presented template.
### Showing a template as an overlay
- [func showOverlayTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./cpinterfacecontroller/showoverlaytemplate%28_,animated,completion%29.md)
  Displays a voice-control template as an overlay on top of your app’s current content.
- [func hideOverlayTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./cpinterfacecontroller/hideoverlaytemplate%28animated,completion%29.md)
  Dismisses the template previously displayed as an overlay.
### Deprecated
- [func dismissTemplate(animated: Bool)](./cpinterfacecontroller/dismisstemplate%28animated%29.md)
  Dismiss the current modally-presented template, optionally animating the dismissal.
- [func pop(to: CPTemplate, animated: Bool)](./cpinterfacecontroller/pop%28to,animated%29.md)
  Pop back to a specified template.
- [func popTemplate(animated: Bool)](./cpinterfacecontroller/poptemplate%28animated%29.md)
  Pop back a single level in the template navigation hierarchy.
- [func popToRootTemplate(animated: Bool)](./cpinterfacecontroller/poptoroottemplate%28animated%29.md)
  Pop back to the first template in the template navigation hierarchy.
- [func presentTemplate(CPTemplate, animated: Bool)](./cpinterfacecontroller/presenttemplate%28_,animated%29.md)
  Present a template modally over the navigation hierarchy. Only one template may be presented at a time.
- [func pushTemplate(CPTemplate, animated: Bool)](./cpinterfacecontroller/pushtemplate%28_,animated%29.md)
  Push a new template onto the template navigation hierarchy, showing it immediately.
- [func setRootTemplate(CPTemplate, animated: Bool)](./cpinterfacecontroller/setroottemplate%28_,animated%29.md)
  Set the root template. If no existing templates exist in the template navigation hierarchy, the animated flag will be ignored. If there is an existing template navigation hierarchy, the existing stack will be replaced by the new root template.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### App management
- [Building your app’s initial CarPlay interface](./building-your-apps-initial-carplay-interface.md)
  Build the interface for your CarPlay app using scenes and templates from the CarPlay framework.
- [class CPTemplateApplicationScene](./cptemplateapplicationscene.md)
  A CarPlay scene that manages your app’s interface on the vehicle’s center display.
- [protocol CPTemplateApplicationSceneDelegate](./cptemplateapplicationscenedelegate.md)
  Methods for responding to  life-cycle events in your app’s scene.
- [class CPSessionConfiguration](./cpsessionconfiguration.md)
  An object that keeps you informed of changes to the CarPlay environment.
- [class CPWindow](./cpwindow.md)
  A type that navigation apps use to present their map content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller)*