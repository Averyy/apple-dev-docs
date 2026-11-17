# CPBarButtonProviding

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

The interface templates you use to manage buttons in the navigation bar.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol CPBarButtonProviding : NSObjectProtocol
```

```objc
@protocol CPBarButtonProviding <NSObject>
```

## Overview

This protocol adds support for displaying custom buttons in the navigation bar that appears above your app’s template-based content. CarPlay implements a navigation-style interface for apps, which allows your app to make changes to the interface by pushing and popping templates off the system-managed navigation stack. The navigation bar at the top of each template offers a place to add custom actions relevant to the current content.

System-provided templates adopt this protocol to support the addition of buttons to the navigation bar when the template is visible. You don’t adopt this protocol in your app’s custom types. When you prepare a template for display, add buttons to the properties of this protocol if you have actions you want to make available.

> **Note**: The [`CPNowPlayingTemplate`](./cpnowplayingtemplate.md), [`CPSearchTemplate`](./cpsearchtemplate.md), [`CPTabBarTemplate`](./cptabbartemplate.md), and [`CPActionSheetTemplate`](./cpactionsheettemplate.md) types don’t support navigation bar buttons. The [`CPVoiceControlTemplate`](./cpvoicecontroltemplate.md) type supports navigation bar buttons only in iOS 26.4 and later.

## Topics

### Providing navigation bar buttons
- [var backButton: CPBarButton?](./cpbarbuttonproviding/backbutton.md)
  A button you use to implement custom transitions.
- [var leadingNavigationBarButtons: [CPBarButton]](./cpbarbuttonproviding/leadingnavigationbarbuttons.md)
  Additional buttons to display at the leading edge of the navigation bar.
- [var trailingNavigationBarButtons: [CPBarButton]](./cpbarbuttonproviding/trailingnavigationbarbuttons.md)
  Additional buttons to display at the trailing edge of the navigation bar.
- [class CPBarButton](./cpbarbutton.md)
  A button that appears in a navigation bar.
- [class CPMessageComposeBarButton](./cpmessagecomposebarbutton.md)
  A button that activates Siri and initiates the process for composing a message.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [CPContactTemplate](./cpcontacttemplate.md)
- [CPGridTemplate](./cpgridtemplate.md)
- [CPInformationTemplate](./cpinformationtemplate.md)
- [CPListTemplate](./cplisttemplate.md)
- [CPMapTemplate](./cpmaptemplate.md)
- [CPPointOfInterestTemplate](./cppointofinteresttemplate.md)
- [CPVoiceControlTemplate](./cpvoicecontroltemplate.md)

## See Also

### Navigation bar
- [class CPBarButton](./cpbarbutton.md)
  A button that appears in a navigation bar.
- [class CPMessageComposeBarButton](./cpmessagecomposebarbutton.md)
  A button that activates Siri and initiates the process for composing a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbuttonproviding)*