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

### Creating a Voice Control Template
- [init(voiceControlStates: [CPVoiceControlState])](./cpvoicecontroltemplate/init%28voicecontrolstates%29.md)
  Creates a voice control template with a list of voice control states.
- [class CPVoiceControlState](./cpvoicecontrolstate.md)
  A voice control state containing title variants and images for use by a voice control template.
### Activating a State
- [func activateVoiceControlState(withIdentifier: String)](./cpvoicecontroltemplate/activatevoicecontrolstate%28withidentifier%29.md)
  Changes the template’s state to the one matching the specified identifier.
- [var activeStateIdentifier: String?](./cpvoicecontroltemplate/activestateidentifier.md)
  The identifier of the template’s current voice control state.
### Getting Available States
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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Navigation
- [Integrating CarPlay with Your Navigation App](./integrating-carplay-with-your-navigation-app.md)
  Configure your navigation app to work with CarPlay by displaying your custom map and directions.
- [class CPTemplateApplicationDashboardScene](./cptemplateapplicationdashboardscene.md)
  A CarPlay scene that controls your app’s dashboard navigation window.
- [protocol CPTemplateApplicationDashboardSceneDelegate](./cptemplateapplicationdashboardscenedelegate.md)
  The methods for responding to the life-cycle events of your navigation app’s dashboard scene.
- [class CPMapTemplate](./cpmaptemplate.md)
  A template that displays a navigation overlay that your app draws on the map.
- [class CPSearchTemplate](./cpsearchtemplate.md)
  A template that provides the ability to search for a destination and see a list of search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpvoicecontroltemplate)*