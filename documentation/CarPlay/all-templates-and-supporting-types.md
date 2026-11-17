# All templates and supporting types

**Framework**: CarPlay  
**Role**: API Collection

Explore the templates you use to build the interface of your CarPlay app.

## Overview

Templates are objects you use to specify the content of your app’s CarPlay interface. A template manages the data you want to present, and offers some control over the presentation of that content. When you ask CarPlay to display a template, iOS generates the views needed to display that content and delivers them to CarPlay, which handles the presentation of that content in the vehicle. This process lets you focus on your app’s content while the system handles differences in display technologies, sizes, resolutions, interface configurations, and more.

Some CarPlay templates offer equivalent features to iOS views and view controllers, and you use them in similar situations. For example, the [`CPTabBarTemplate`](./cptabbartemplate.md) creates a tab bar interface similar to an iOS tab bar controller. Templates like [`CPListTemplate`](./cplisttemplate.md) and [`CPGridTemplate`](./cpgridtemplate.md) are building blocks of most interfaces and available in all app types. Other templates support s pecialized experiences and are available only in apps that offer relevant features.

> **Note**: For guidance on how to build your app’s interface, see [CarPlay](https://developer.apple.com/design/human-interface-guidelines/carplay) in Human Interface Guidelines.

## Topics

### Tab bar
- [class CPTabBarTemplate](./cptabbartemplate.md)
  A container template that displays and manages other templates, presenting them as tabs.
### Navigation bar
- [protocol CPBarButtonProviding](./cpbarbuttonproviding.md)
  The interface templates you use to manage buttons in the navigation bar.
- [class CPBarButton](./cpbarbutton.md)
  A button that appears in a navigation bar.
- [class CPMessageComposeBarButton](./cpmessagecomposebarbutton.md)
  A button that activates Siri and initiates the process for composing a message.
### Lists
- [class CPListTemplate](./cplisttemplate.md)
  A template that displays a single-column list of items in one of several visual styles.
- [class CPListSection](./cplistsection.md)
  A container that groups related items in a list interface.
- [class CPListItem](./cplistitem.md)
  A selectable row in a list interface.
- [class CPListImageRowItem](./cplistimagerowitem.md)
  A row type that displays multiple sub-elements horizontally in a variety of styles.
- [Supporting types for lists](./list-content.md)
  Create sections, single-line items, multi-element rows, headers, and other content for your list.
### Grids
- [class CPGridTemplate](./cpgridtemplate.md)
  A template that displays and manages a grid of items.
- [class CPGridButton](./cpgridbutton.md)
  A menu item button displayed on a grid template.
- [class CPMessageGridItemConfiguration](./cpmessagegriditemconfiguration.md)
  A type that associates message-related information with a grid button.
- [let CPGridTemplateMaximumItems: Int](./cpgridtemplatemaximumitems.md)
  The maximum number of buttons that a grid template displays.
### Maps
- [class CPMapTemplate](./cpmaptemplate.md)
  A template that displays a navigation overlay that your app draws on the map.
- [class CPMapButton](./cpmapbutton.md)
  A button that represents an action that a map template displays on the CarPlay screen.
- [class CPMapPanel](./cpmappanel.md)
  An overlay for a custom map interface that shows navigation-related instructions or information over a portion of the map.
- [class CPMapPanelSection](./cpmappanelsection.md)
  A single section of a map panel that you fill with a title and one or more items.
- [class CPMapPanelItem](./cpmappanelitem.md)
  A type that manages the waypoint, route, trip, and other information you display in a map panel.
- [class CPMapPanelButtonConfiguration](./cpmappanelbuttonconfiguration.md)
  A type that manages the action buttons and travel estimates in a map panel.
- [class CPChargingStationConnection](./cpchargingstationconnection.md)
  Details about the equipment at an electric vehicle charging station.
### Now playing
- [class CPNowPlayingTemplate](./cpnowplayingtemplate.md)
  A shared system template that shows the currently selected audio content and offers controls to manage playback.
- [protocol CPNowPlayingTemplateObserver](./cpnowplayingtemplateobserver.md)
  Methods for responding to interactions with buttons in the Now Playing template.
- [Now Playing supporting types](./now-playing-support.md)
  Add Now Playing buttons to your interface and configure overlays with sports information.
### Point of interest
- [class CPPointOfInterestTemplate](./cppointofinteresttemplate.md)
  A template that displays a map with selectable points of interest.
- [protocol CPPointOfInterestTemplateDelegate](./cppointofinteresttemplatedelegate.md)
  The methods to handle a point of interest template’s events.
- [class CPPointOfInterest](./cppointofinterest.md)
  An object that describes a point of interest on the template’s map and in its scrollable picker.
### Information
- [class CPInformationTemplate](./cpinformationtemplate.md)
  A template that provides information for a point of interest, food order, parking location, or charging location.
- [class CPInformationItem](./cpinformationitem.md)
  A data object that provides content for an information template.
- [class CPInformationRatingItem](./cpinformationratingitem.md)
  A data object that provides rated content for an information template.
### Contacts
- [class CPContactTemplate](./cpcontacttemplate.md)
  A template that displays information about a person or a business.
- [class CPContact](./cpcontact.md)
  A data object that contains information about a contact.
- [class CPContactCallButton](./cpcontactcallbutton.md)
  A button for calling the contact.
- [class CPContactDirectionsButton](./cpcontactdirectionsbutton.md)
  A button for getting directions to the contact’s location.
- [class CPContactMessageButton](./cpcontactmessagebutton.md)
  A button that activates Siri and initiates the compose message flow.
### Search
- [class CPSearchTemplate](./cpsearchtemplate.md)
  A template that provides the ability to search for a destination and see a list of search results.
### Voice control
- [class CPVoiceControlTemplate](./cpvoicecontroltemplate.md)
  A template that displays a voice control indicator during audio input.
- [class CPVoiceControlState](./cpvoicecontrolstate.md)
  A voice control state containing title variants and images for use by a voice control template.
### Action sheets
- [class CPActionSheetTemplate](./cpactionsheettemplate.md)
  A template that displays a modal action sheet.
### Alerts
- [class CPAlertTemplate](./cpalerttemplate.md)
  A template that displays a modal alert.
- [class CPAlertAction](./cpalertaction.md)
  An object that encapsulates an action the user can perform on an action sheet or alert.
### Common types
- [class CPTemplate](./cptemplate.md)
  An abstract base class for interface templates.
- [class CPTextButton](./cptextbutton.md)
  A button that displays a stylized title.
- [class CPButton](./cpbutton.md)
  A button that displays an image and invokes a handler when the user taps it.
- [class CPImageSet](./cpimageset.md)
  Light and dark representations of an image.
- [class CPPanel](./cppanel.md)
  A type that provides the common behaviors for panels you display on top of your app’s content.
- [class CPPanelItem](./cppanelitem.md)
  A type that provides the common behaviors for items you display in a section of a panel.
- [class CPPanelButtonConfiguration](./cppanelbuttonconfiguration.md)
  A type that provides the common behaviors for a button layout in a panel.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/all-templates-and-supporting-types)*