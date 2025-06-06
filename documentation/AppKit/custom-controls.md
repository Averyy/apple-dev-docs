# Custom Controls

**Framework**: AppKit

Support accessibility for custom user interface elements by adopting a role-specific protocol and implementing its methods.

#### Overview

Role-specific accessibility protocols represent the most common control types found in apps. Adopt a role-specific accessibility protocol if:

- You’re creating a custom control that’s a subclass of [`NSView`](nsview.md), and you want to modify the control’s behavior beyond what AppKit provides by default.
- You’re working with a specialized control that doesn’t subclass [`NSView`](nsview.md). See [`NSAccessibilityElement`](nsaccessibilityelement-swift.class.md) first.

First, identify the role-specific protocol that best matches your control’s intended behavior. For example, if your control is something that triggers actions when the user clicks it, adopt the [`NSAccessibilityButton`](nsaccessibilitybutton.md) protocol.

After you select an appropriate protocol, adopt that protocol. The compiler may ask you to reimplement some of the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol’s accessor or action methods. Simply implement these methods, and your control is ready to use.

## Topics

### Buttons
- [protocol NSAccessibilityButton](nsaccessibilitybutton.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a button.
- [protocol NSAccessibilityRadioButton](nsaccessibilityradiobutton.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a radio button.
- [protocol NSAccessibilitySwitch](nsaccessibilityswitch.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a switch.
- [protocol NSAccessibilityCheckBox](nsaccessibilitycheckbox.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a checkbox.
### Value Controls
- [protocol NSAccessibilityStepper](nsaccessibilitystepper.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a stepper.
- [protocol NSAccessibilitySlider](nsaccessibilityslider.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a slider.
### Groups
- [protocol NSAccessibilityGroup](nsaccessibilitygroup.md)
  A role-based protocol that declares the minimum interface necessary to act as a container for other user interface elements.
### Lists
- [protocol NSAccessibilityTable](nsaccessibilitytable.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a table view.
- [protocol NSAccessibilityList](nsaccessibilitylist.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a list view.
- [protocol NSAccessibilityOutline](nsaccessibilityoutline.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as an outline view.
- [protocol NSAccessibilityRow](nsaccessibilityrow.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a row for a table, list, or outline view.
### Text
- [protocol NSAccessibilityStaticText](nsaccessibilitystatictext.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as static text.
- [protocol NSAccessibilityNavigableStaticText](nsaccessibilitynavigablestatictext.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as navigable static text.
### Images and Color
- [protocol NSAccessibilityImage](nsaccessibilityimage.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as an image.
- [protocol NSAccessibilityColor](nsaccessibilitycolor.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a color.
### Loading
- [protocol NSAccessibilityProgressIndicator](nsaccessibilityprogressindicator.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a progress indicator.
- [protocol NSAccessibilityElementLoading](nsaccessibilityelementloading.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to support loading.
### Dynamic Elements
- [protocol NSAccessibilityContainsTransientUI](nsaccessibilitycontainstransientui.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to support dynamic UI changes.
### Layout Elements
- [protocol NSAccessibilityLayoutArea](nsaccessibilitylayoutarea.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a layout area.
- [protocol NSAccessibilityLayoutItem](nsaccessibilitylayoutitem.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to act as a layout item.
### Supporting Types
- [protocol NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
  A role-based protocol that declares the minimum interface necessary to interact with an assistive app.

## See Also

- [Accessibility Functions](accessibility-functions.md)
  Global accessibility functions for custom views and controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/custom-controls)*