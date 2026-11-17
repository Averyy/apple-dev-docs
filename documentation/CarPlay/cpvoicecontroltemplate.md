# CPVoiceControlTemplate

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A template that displays a voice control indicator during audio input.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class CPVoiceControlTemplate
```

```objc
@interface CPVoiceControlTemplate : CPTemplate
```

## Overview

CarPlay navigation apps must show a voice control indicator during audio input by presenting a voice control template. When creating the template, provide one or more [`CPVoiceControlState`](./cpvoicecontrolstate.md) objects. To switch between states, call the [`activateVoiceControlState(withIdentifier:)`](./cpvoicecontroltemplate/activatevoicecontrolstate%28withidentifier%29.md) method.

## Topics

### Creating a voice control template
- [init(voiceControlStates: [CPVoiceControlState])](./cpvoicecontroltemplate/init%28voicecontrolstates%29.md)
  Creates a voice control template with a list of voice control states.
- [class CPVoiceControlState](./cpvoicecontrolstate.md)
  A voice control state containing title variants and images for use by a voice control template.
### Activating a state
- [func activateVoiceControlState(withIdentifier: String)](./cpvoicecontroltemplate/activatevoicecontrolstate%28withidentifier%29.md)
  Changes the template’s state to the one matching the specified identifier.
- [var activeStateIdentifier: String?](./cpvoicecontroltemplate/activestateidentifier.md)
  The identifier of the template’s current voice control state.
### Getting the available states
- [var voiceControlStates: [CPVoiceControlState]](./cpvoicecontroltemplate/voicecontrolstates.md)
  The array of voice control states available to the template.
### Instance Properties
- [var backButton: CPBarButton?](./cpvoicecontroltemplate/backbutton.md)
- [var leadingNavigationBarButtons: [CPBarButton]](./cpvoicecontroltemplate/leadingnavigationbarbuttons.md)
  An array of bar buttons to be displayed on the leading side of the navigation bar.
- [var trailingNavigationBarButtons: [CPBarButton]](./cpvoicecontroltemplate/trailingnavigationbarbuttons.md)
  An array of bar buttons to be displayed on the trailing side of the navigation bar.

## Relationships

### Inherits From
- [CPTemplate](./cptemplate.md)
### Conforms To
- [CPBarButtonProviding](./cpbarbuttonproviding.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

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
- [class CPActionSheetTemplate](./cpactionsheettemplate.md)
  A template that displays a modal action sheet.
- [class CPAlertTemplate](./cpalerttemplate.md)
  A template that displays a modal alert.
- [All templates and supporting types](./all-templates-and-supporting-types.md)
  Explore the templates you use to build the interface of your CarPlay app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpvoicecontroltemplate)*