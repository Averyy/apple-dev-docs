# CPBarButtonProviding

**Framework**: CarPlay  
**Kind**: protocol

The methods that templates use to provide buttons for the navigation bar.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol CPBarButtonProviding : NSObjectProtocol
```

#### Overview

`CPBarButtonProviding` is a protocol that templates use to provide a Back button and leading and trailing buttons for the navigation bar.

You don’t adopt this protocol in your own types. If you want to add buttons to the navigation bar, you must use one of the prebuilt templates that already conforms to the protocol, such as [`CPMapTemplate`](cpmaptemplate.md) or [`CPContactTemplate`](cpcontacttemplate.md).

> **Note**:  The root templates of a tab bar don’t show leading or trailing bar buttons, and the system throws an exception if you attempt to assign bar buttons to the Now Playing template.

 The root templates of a tab bar don’t show leading or trailing bar buttons, and the system throws an exception if you attempt to assign bar buttons to the Now Playing template.

## Topics

### Providing Navigation Bar Buttons
- [var backButton: CPBarButton?](cpbarbuttonproviding/backbutton.md)
  A button to display as the Back button on the navigation bar.
- [var leadingNavigationBarButtons: [CPBarButton]](cpbarbuttonproviding/leadingnavigationbarbuttons.md)
  An array of bar buttons to display on the leading side of the navigation bar.
- [var trailingNavigationBarButtons: [CPBarButton]](cpbarbuttonproviding/trailingnavigationbarbuttons.md)
  An array of bar buttons to display on the trailing side of the navigation bar.
- [class CPBarButton](cpbarbutton.md)
  A button for placement in a navigation bar.
- [class CPMessageComposeBarButton](cpmessagecomposebarbutton.md)
  A button that activates Siri and initiates the compose message flow.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [CPContactTemplate](cpcontacttemplate.md)
- [CPGridTemplate](cpgridtemplate.md)
- [CPInformationTemplate](cpinformationtemplate.md)
- [CPListTemplate](cplisttemplate.md)
- [CPMapTemplate](cpmaptemplate.md)
- [CPPointOfInterestTemplate](cppointofinteresttemplate.md)

## See Also

- [class CPListTemplate](cplisttemplate.md)
  A template that displays and manages a list of items.
- [class CPGridTemplate](cpgridtemplate.md)
  A template that displays and manages a grid of items.
- [class CPTabBarTemplate](cptabbartemplate.md)
  A container template that displays and manages other templates, presenting them as tabs.
- [class CPTemplate](cptemplate.md)
  An abstract base class for interface templates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbuttonproviding)*