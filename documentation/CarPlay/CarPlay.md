# CarPlay

**Framework**: CarPlay  
**Kind**: module  
**Role**: Framework

Deliver your iOS app’s audio, video, messaging, VoIP calling, navigation, or other features in CarPlay environments.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

## Overview

Use the CarPlay framework to add an in-vehicle or HomeView experience to your existing iOS app. The framework defines UIKit scenes and interface elements you use to present your app’s content in a CarPlay environment. In your CarPlay app, you assemble your interface from *templates*, which specify the data to display and a presentation style. When you present a template, CarPlay renders it for a vehicle and displays it, taking into account the vehicle’s screen size and environmental settings. This approach allows you to focus on your content and let CarPlay handle differences between display sizes and settings.

The CarPlay experience starts when someone connects their iOS device to HomeView or a CarPlay-enabled vehicle. When connected, people can launch apps or view your app’s widgets and Live Activities. The system forwards interactions with your app’s content back to your custom code, which you specify when you construct your interface. Interactions with widgets and Live Activities happen through the existing code paths for those items.

Add CarPlay support to your iOS app if it plays audio or video, provides turn-by-turn directions, sends or receives messages, manages VoIP calls, orders food, manages vehicle-related tasks, or offers other relevant services. You declare the type of app you’re creating by requesting specific entitlements, which govern the policies your app needs to follow and the templates it can use to display content.

> **Note**: For additional information about how to develop CarPlay apps, see [CarPlay Developer Guide](https://developer.apple.com/download/files/CarPlay-Developer-Guide.pdf) and [Accelerate Your App with CarPlay](https://developer.apple.com/videos/play/wwdc2020/10635/).

## Topics

### Essentials
- [Preparing your iOS app for CarPlay development](./preparing-your-ios-app-for-carplay-development.md)
  Configure the entitlements and provisioning profile you need to run your iOS app in CarPlay environments.
### App management
- [Building your app’s initial CarPlay interface](./building-your-apps-initial-carplay-interface.md)
  Build the interface for your CarPlay app using scenes and templates from the CarPlay framework.
- [class CPTemplateApplicationScene](./cptemplateapplicationscene.md)
  A CarPlay scene that manages your app’s interface on the vehicle’s center display.
- [protocol CPTemplateApplicationSceneDelegate](./cptemplateapplicationscenedelegate.md)
  Methods for responding to  life-cycle events in your app’s scene.
- [class CPInterfaceController](./cpinterfacecontroller.md)
  The type you use to present your app’s CarPlay interface and change what appears on the vehicle’s display.
- [class CPSessionConfiguration](./cpsessionconfiguration.md)
  An object that keeps you informed of changes to the CarPlay environment.
- [class CPWindow](./cpwindow.md)
  A type that navigation apps use to present their map content.
### Interface templates
- [class CPTabBarTemplate](./cptabbartemplate.md)
  A container template that displays and manages other templates, presenting them as tabs.
- [class CPListTemplate](./cplisttemplate.md)
  A template that displays a single-column list of items in one of several visual styles.
- [class CPGridTemplate](./cpgridtemplate.md)
  A template that displays and manages a grid of items.
- [class CPMapTemplate](./cpmaptemplate.md)
  A template that displays a navigation overlay that your app draws on the map.
- [class CPNowPlayingTemplate](./cpnowplayingtemplate.md)
  A shared system template that shows the currently selected audio content and offers controls to manage playback.
- [class CPPointOfInterestTemplate](./cppointofinteresttemplate.md)
  A template that displays a map with selectable points of interest.
- [class CPInformationTemplate](./cpinformationtemplate.md)
  A template that provides information for a point of interest, food order, parking location, or charging location.
- [class CPContactTemplate](./cpcontacttemplate.md)
  A template that displays information about a person or a business.
- [class CPSearchTemplate](./cpsearchtemplate.md)
  A template that provides the ability to search for a destination and see a list of search results.
- [class CPVoiceControlTemplate](./cpvoicecontroltemplate.md)
  A template that displays a voice control indicator during audio input.
- [class CPActionSheetTemplate](./cpactionsheettemplate.md)
  A template that displays a modal action sheet.
- [class CPAlertTemplate](./cpalerttemplate.md)
  A template that displays a modal alert.
- [All templates and supporting types](./all-templates-and-supporting-types.md)
  Explore the templates you use to build the interface of your CarPlay app.
### CarPlay app types
- [Audio](./audio.md)
  Build an app that plays audio or video content.
- [Communication](./communication-apps.md)
  Build an app that offers SiriKit messaging or VoIP calling services.
- [Driving task](./driving-task.md)
  Build an app that helps people perform driving-related tasks.
- [EV charging](./ev-charging.md)
  Build an app that provides helpful information about nearby charging facilities.
- [Fueling](./fueling.md)
  Build an app that provides helpful information about nearby fueling stations.
- [Navigation](./navigation-apps.md)
  Build an app that provides turn-by-turn directions to someone while driving.
- [Parking](./parking.md)
  Build an app that provides helpful information about nearby parking facilities.
- [Public safety](./public-safety.md)
  Build an app that offers public safety information to someone who’s driving.
- [Quick food ordering](./quick-food-ordering.md)
  Build an app that helps someone order food for pickup.
- [Video](./video.md)
  Build an app that plays video content exclusively.
- [Voice-based conversation](./voice-based-conversation.md)
  Build an app that responds to questions or requests and performs actions.
### Testing
- [Testing your app in CarPlay Simulator](./testing-your-app-in-carplay-simulator.md)
  Run your app in CarPlay Simulator to identify and debug potential issues.
### Errors
- [let CarPlayErrorDomain: String](./carplayerrordomain.md)
  The domain that CarPlay uses for any errors it provides.
### Deprecated
- [Deprecated Symbols](./deprecated-symbols.md)
  Symbols that the CarPlay framework no longer supports.
### Variables
- [CPTemplateApplicationDashboardSceneSessionRoleApplication](./cptemplateapplicationdashboardscenesessionroleapplication.md)
- [CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication](./cptemplateapplicationinstrumentclusterscenesessionroleapplication.md)
- [CPTemplateApplicationSceneSessionRoleApplication](./cptemplateapplicationscenesessionroleapplication.md)
### Macros
- [CARPLAY_TEMPLATE_UI_ACTOR](./carplay_template_ui_actor.md)
### Enumerations
- [CPPlaybackAction](./cpplaybackconfiguration/action.md)
  The action to perform when someone selects the item.
- [CPPlaybackPresentation](./cpplaybackconfiguration/presentation.md)
  Constants that specify the presentation style for the media of a selected item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CarPlay)*