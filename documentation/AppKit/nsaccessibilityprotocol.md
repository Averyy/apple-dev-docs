# NSAccessibilityProtocol

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

The complete list of properties and methods for accessible elements.

**Availability**:
- macOS

## Declaration

```swift
protocol NSAccessibilityProtocol : NSObjectProtocol
```

```objc
@protocol NSAccessibility <NSObject>
```

## Overview

To be accessible, an app must provide information to the assistive app about its user interface and capabilities. There are three ways that apps and assistive apps interact:

- Informational properties. [`NSAccessibilityProtocol`](./nsaccessibilityprotocol.md) defines a number of properties that provide information about your view or control. If you’re working with a subclass of a standard AppKit view or control, you can either set the desired property or override its getters and setters. By default, overriding only the getter tells the assistive app that it has read-only access to the property. Overriding the setter tells the assistive app that it also has write access to the property.
- Action methods. [`NSAccessibilityProtocol`](./nsaccessibilityprotocol.md) also defines a number of methods that simulate button presses, mouse clicks, and selections in your view or control. By implementing these methods, you give assistive apps the ability to drive your view or control.
- Notifications. Your view or control may need to let the assistive app know when changes occur. [`NSAccessibility.Notification`](./nsaccessibility-swift.struct/notification.md) defines a number of notifications that you can send using the [`post(element:notification:)`](./nsaccessibility-swift.struct/post%28element,notification%29.md) method. The role-specific protocols don’t include these notifications; however, standard AppKit controls already send appropriate messages for their standard usage patterns. You typically need to send your own notifications only when you’re creating a custom control or when you’re using a standard control in a nonstandard way.

If you’re using standard AppKit user interface elements, much of the work has been done for you. AppKit views and controls adopt the [`NSAccessibilityProtocol`](./nsaccessibilityprotocol.md) protocol by default. In particular, [`NSView`](./nsview.md), [`NSWindow`](./nswindow.md), [`NSCell`](./nscell.md), and [`NSDrawer`](./nsdrawer.md) provide a default implementation for all the properties and methods in this protocol. In some cases, you may need to modify these default values to better represent your app, to provide additional context, or to modify the user’s flow through the app.

If you’re using custom view or control subclasses, you need to add the appropriate informational properties, action methods, and notifications. You do this by adopting a role-specific protocol instead of [`NSAccessibilityProtocol`](./nsaccessibilityprotocol.md). See [Custom Controls](./custom-controls.md).

If you’re using custom user interface elements that don’t inherit from [`NSView`](./nsview.md) or one of the other accessibility-enabled AppKit classes, subclass the [`NSAccessibilityElement`](./nsaccessibilityelement-swift.class.md) class instead of adopting instead of [`NSAccessibilityProtocol`](./nsaccessibilityprotocol.md).

### Customizing User Interface Elements

Often, you can adjust how an assistive app interacts with your user interface element without creating a custom subclass. If a user interface element inherits from [`NSView`](./nsview.md) or one of the other accessibility-enabled AppKit classes, you can customize it by:

- Setting its accessibility values using any of the setter methods in the [`NSAccessibilityProtocol`](./nsaccessibilityprotocol.md) protocol.
- Overriding any of the properties or methods in the [`NSAccessibilityProtocol`](./nsaccessibilityprotocol.md) protocol with a custom implementation.

If you override a getter method, the system lets assistive apps call your getter. This can be particularly useful when managing dynamic properties because you can calculate their current value on demand instead of trying to update the property in response to a change.

If you override a setter method, the system lets assistive apps both read and modify that property.

You can control which accessor methods the assistive app can use by overriding [`isAccessibilitySelectorAllowed(_:)`](./nsaccessibilityprotocol/isaccessibilityselectorallowed%28_%29.md). Return [`true`](../Swift/true.md) if the assistive app can call the selector; otherwise, return [`false`](../Swift/false.md).

## Topics

### Configuring accessibility
- [func isAccessibilityElement() -> Bool](./nsaccessibilityprotocol/isaccessibilityelement%28%29.md)
  Returns a Boolean value that determines whether the accessibility element participates in the accessibility hierarchy.
- [func setAccessibilityElement(Bool)](./nsaccessibilityprotocol/setaccessibilityelement%28_%29.md)
  Sets a Boolean value that determines whether the accessibility element participates in the accessibility hierarchy.
- [func isAccessibilityEnabled() -> Bool](./nsaccessibilityprotocol/isaccessibilityenabled%28%29.md)
  Returns a Boolean value that determines whether the accessibility element responds to user events.
- [func setAccessibilityEnabled(Bool)](./nsaccessibilityprotocol/setaccessibilityenabled%28_%29.md)
  Sets a Boolean value that determines whether the accessibility element responds to user events.
- [func accessibilityFrame() -> NSRect](./nsaccessibilityprotocol/accessibilityframe%28%29.md)
  Returns the accessibility element’s frame in screen coordinates.
- [func setAccessibilityFrame(NSRect)](./nsaccessibilityprotocol/setaccessibilityframe%28_%29.md)
  Sets the accessibility element’s frame in screen coordinates.
- [func accessibilityHelp() -> String?](./nsaccessibilityprotocol/accessibilityhelp%28%29.md)
  Returns the help text for the accessibility element.
- [func setAccessibilityHelp(String?)](./nsaccessibilityprotocol/setaccessibilityhelp%28_%29.md)
  Sets the help text for the accessibility element.
- [func accessibilityLabel() -> String?](./nsaccessibilityprotocol/accessibilitylabel%28%29.md)
  Returns a short description of the accessibility element.
- [func setAccessibilityLabel(String?)](./nsaccessibilityprotocol/setaccessibilitylabel%28_%29.md)
  Sets a short description of the accessibility element.
- [func accessibilityTitle() -> String?](./nsaccessibilityprotocol/accessibilitytitle%28%29.md)
  Returns the title of the accessibility element—for example, a button’s visible text.
- [func setAccessibilityTitle(String?)](./nsaccessibilityprotocol/setaccessibilitytitle%28_%29.md)
  Sets the title of the accessibility element.
- [func accessibilityValue() -> Any?](./nsaccessibilityprotocol/accessibilityvalue%28%29.md)
  Returns the accessibility element’s value.
- [func setAccessibilityValue(Any?)](./nsaccessibilityprotocol/setaccessibilityvalue%28_%29.md)
  Sets the accessibility element’s value.
- [func isAccessibilitySelectorAllowed(Selector) -> Bool](./nsaccessibilityprotocol/isaccessibilityselectorallowed%28_%29.md)
  Returns a Boolean value that indicates whether assistive apps can invoke the specified selector on the accessibility element.
- [accessibilityElement](./nsaccessibility-c.protocol/accessibilityelement.md)
  A Boolean value that determines whether the accessibility element participates in the accessibility hierarchy.
- [accessibilityEnabled](./nsaccessibility-c.protocol/accessibilityenabled.md)
  A Boolean value that determines whether the accessibility element responds to user events.
- [accessibilityFrame](./nsaccessibility-c.protocol/accessibilityframe.md)
  The accessibility element’s frame in screen coordinates.
- [accessibilityHelp](./nsaccessibility-c.protocol/accessibilityhelp.md)
  The help text for the accessibility element.
- [accessibilityLabel](./nsaccessibility-c.protocol/accessibilitylabel.md)
  A short description of the accessibility element.
- [accessibilityTitle](./nsaccessibility-c.protocol/accessibilitytitle.md)
  The title of the accessibility element—for example, a button’s visible text.
- [accessibilityValue](./nsaccessibility-c.protocol/accessibilityvalue.md)
  The accessibility element’s value.
### Setting content and values
- [func accessibilityContents() -> [Any]?](./nsaccessibilityprotocol/accessibilitycontents%28%29.md)
  Returns the contents of the current accessibility element.
- [func setAccessibilityContents([Any]?)](./nsaccessibilityprotocol/setaccessibilitycontents%28_%29.md)
  Sets the contents of the current accessibility element.
- [func accessibilityCriticalValue() -> Any?](./nsaccessibilityprotocol/accessibilitycriticalvalue%28%29.md)
  Returns the critical value for the level indicator.
- [func setAccessibilityCriticalValue(Any?)](./nsaccessibilityprotocol/setaccessibilitycriticalvalue%28_%29.md)
  Sets the critical value for the level indicator.
- [func accessibilityIdentifier() -> String?](./nsaccessibilityprotocol/accessibilityidentifier%28%29.md)
  Returns the accessibility element’s identity.
- [func setAccessibilityIdentifier(String?)](./nsaccessibilityprotocol/setaccessibilityidentifier%28_%29.md)
  Sets the accessibility element’s identity.
- [func accessibilityMaxValue() -> Any?](./nsaccessibilityprotocol/accessibilitymaxvalue%28%29.md)
  Returns the maximum value for the accessibility element.
- [func setAccessibilityMaxValue(Any?)](./nsaccessibilityprotocol/setaccessibilitymaxvalue%28_%29.md)
  Sets the maximum value for the accessibility element.
- [func accessibilityMinValue() -> Any?](./nsaccessibilityprotocol/accessibilityminvalue%28%29.md)
  Returns the minimum value for the accessibility element.
- [func setAccessibilityMinValue(Any?)](./nsaccessibilityprotocol/setaccessibilityminvalue%28_%29.md)
  Sets the minimum value for the accessibility element.
- [func accessibilityOrientation() -> NSAccessibilityOrientation](./nsaccessibilityprotocol/accessibilityorientation%28%29.md)
  Returns the orientation of the accessibility element.
- [func setAccessibilityOrientation(NSAccessibilityOrientation)](./nsaccessibilityprotocol/setaccessibilityorientation%28_%29.md)
  Sets the orientation of the accessibility element.
- [func isAccessibilityProtectedContent() -> Bool](./nsaccessibilityprotocol/isaccessibilityprotectedcontent%28%29.md)
  Returns a Boolean value that determines whether the accessibility element contains protected content.
- [func setAccessibilityProtectedContent(Bool)](./nsaccessibilityprotocol/setaccessibilityprotectedcontent%28_%29.md)
  Sets a Boolean value that determines whether the accessibility element contains protected content.
- [func isAccessibilitySelected() -> Bool](./nsaccessibilityprotocol/isaccessibilityselected%28%29.md)
  Returns a Boolean value that determines whether the accessibility element is currently in a selected state.
- [func setAccessibilitySelected(Bool)](./nsaccessibilityprotocol/setaccessibilityselected%28_%29.md)
  Sets a Boolean value that determines whether the accessibility element is currently in a selected state.
- [func accessibilityURL() -> URL?](./nsaccessibilityprotocol/accessibilityurl%28%29.md)
  Returns the URL for the accessibility element.
- [func setAccessibilityURL(URL?)](./nsaccessibilityprotocol/setaccessibilityurl%28_%29.md)
  Sets the URL for the accessibility element.
- [func accessibilityValueDescription() -> String?](./nsaccessibilityprotocol/accessibilityvaluedescription%28%29.md)
  Returns the human-readable description of the accessibility element’s value.
- [func setAccessibilityValueDescription(String?)](./nsaccessibilityprotocol/setaccessibilityvaluedescription%28_%29.md)
  Sets the human-readable description of the accessibility element’s value.
- [func accessibilityWarningValue() -> Any?](./nsaccessibilityprotocol/accessibilitywarningvalue%28%29.md)
  Returns the warning value for the level indicator.
- [func setAccessibilityWarningValue(Any?)](./nsaccessibilityprotocol/setaccessibilitywarningvalue%28_%29.md)
  Sets the warning value for the level indicator.
- [enum NSAccessibilityOrientation](./nsaccessibilityorientation.md)
  Values that indicate the orientation of accessibility elements, such as scroll bars and split views.
- [accessibilityContents](./nsaccessibility-c.protocol/accessibilitycontents.md)
  The contents of the current accessibility element.
- [accessibilityCriticalValue](./nsaccessibility-c.protocol/accessibilitycriticalvalue.md)
  The critical value for the level indicator.
- [accessibilityIdentifier](./nsaccessibility-c.protocol/accessibilityidentifier.md)
  The accessibility element’s identity.
- [accessibilityMaxValue](./nsaccessibility-c.protocol/accessibilitymaxvalue.md)
  The maximum value for the accessibility element.
- [accessibilityMinValue](./nsaccessibility-c.protocol/accessibilityminvalue.md)
  The minimum value for the accessibility element.
- [accessibilityOrientation](./nsaccessibility-c.protocol/accessibilityorientation.md)
  The orientation of the accessibility element.
- [accessibilityProtectedContent](./nsaccessibility-c.protocol/accessibilityprotectedcontent.md)
  A Boolean value that determines whether the accessibility element contains protected content.
- [accessibilitySelected](./nsaccessibility-c.protocol/accessibilityselected.md)
  A Boolean value that determines whether the accessibility element is currently in a selected state.
- [accessibilityURL](./nsaccessibility-c.protocol/accessibilityurl.md)
  The URL for the accessibility element.
- [accessibilityValueDescription](./nsaccessibility-c.protocol/accessibilityvaluedescription.md)
  A human-readable description of the accessibility element’s value.
- [accessibilityWarningValue](./nsaccessibility-c.protocol/accessibilitywarningvalue.md)
  The warning value for the level indicator.
### Determining relationships
- [func accessibilityChildren() -> [Any]?](./nsaccessibilityprotocol/accessibilitychildren%28%29.md)
  Returns the child accessibility elements in the accessibility hierarchy.
- [func setAccessibilityChildren([Any]?)](./nsaccessibilityprotocol/setaccessibilitychildren%28_%29.md)
  Sets the child accessibility elements in the accessibility hierarchy.
- [func accessibilityChildrenInNavigationOrder() -> [any NSAccessibilityElementProtocol]?](./nsaccessibilityprotocol/accessibilitychildreninnavigationorder%28%29.md)
  Returns the array of child accessibility elements in order for linear navigation.
- [func setAccessibilityChildrenInNavigationOrder([any NSAccessibilityElementProtocol]?)](./nsaccessibilityprotocol/setaccessibilitychildreninnavigationorder%28_%29.md)
  Sets the array of child accessibility elements in order for linear navigation.
- [func accessibilityParent() -> Any?](./nsaccessibilityprotocol/accessibilityparent%28%29.md)
  Returns the accessibility element’s parent in the accessibility hierarchy.
- [func setAccessibilityParent(Any?)](./nsaccessibilityprotocol/setaccessibilityparent%28_%29.md)
  Sets the accessibility element’s parent in the accessibility hierarchy.
- [func accessibilitySelectedChildren() -> [Any]?](./nsaccessibilityprotocol/accessibilityselectedchildren%28%29.md)
  Returns the accessibility element’s currently selected children.
- [func setAccessibilitySelectedChildren([Any]?)](./nsaccessibilityprotocol/setaccessibilityselectedchildren%28_%29.md)
  Sets the accessibility element’s currently selected children.
- [func accessibilityTopLevelUIElement() -> Any?](./nsaccessibilityprotocol/accessibilitytopleveluielement%28%29.md)
  Returns the top-level element that contains the accessibility element.
- [func setAccessibilityTopLevelUIElement(Any?)](./nsaccessibilityprotocol/setaccessibilitytopleveluielement%28_%29.md)
  Sets the top-level element that contains the accessibility element.
- [func accessibilityVisibleChildren() -> [Any]?](./nsaccessibilityprotocol/accessibilityvisiblechildren%28%29.md)
  Returns the accessibility element’s visible child accessibility elements.
- [func setAccessibilityVisibleChildren([Any]?)](./nsaccessibilityprotocol/setaccessibilityvisiblechildren%28_%29.md)
  Sets the accessibility element’s visible child accessibility elements.
- [accessibilityChildren](./nsaccessibility-c.protocol/accessibilitychildren.md)
  The child accessibility elements in the accessibility hierarchy.
- [accessibilityChildrenInNavigationOrder](./nsaccessibility-c.protocol/accessibilitychildreninnavigationorder.md)
  An array of child accessibility elements in order for linear navigation.
- [accessibilityParent](./nsaccessibility-c.protocol/accessibilityparent.md)
  The accessibility element’s parent in the accessibility hierarchy.
- [accessibilitySelectedChildren](./nsaccessibility-c.protocol/accessibilityselectedchildren.md)
  The accessibility element’s currently selected children.
- [accessibilityTopLevelUIElement](./nsaccessibility-c.protocol/accessibilitytopleveluielement.md)
  The top-level element that contains the accessibility element.
- [accessibilityVisibleChildren](./nsaccessibility-c.protocol/accessibilityvisiblechildren.md)
  The accessibility element’s visible child accessibility elements.
### Setting the focus
- [func accessibilityApplicationFocusedUIElement() -> Any?](./nsaccessibilityprotocol/accessibilityapplicationfocuseduielement%28%29.md)
  Returns the child accessibility element with the current focus.
- [func setAccessibilityApplicationFocusedUIElement(Any?)](./nsaccessibilityprotocol/setaccessibilityapplicationfocuseduielement%28_%29.md)
  Sets the child accessibility element with the current focus.
- [func isAccessibilityFocused() -> Bool](./nsaccessibilityprotocol/isaccessibilityfocused%28%29.md)
  Returns a Boolean value that determines whether the accessibility element has the keyboard focus.
- [func setAccessibilityFocused(Bool)](./nsaccessibilityprotocol/setaccessibilityfocused%28_%29.md)
  Sets a Boolean value that determines whether the accessibility element has the keyboard focus.
- [func accessibilityFocusedWindow() -> Any?](./nsaccessibilityprotocol/accessibilityfocusedwindow%28%29.md)
  Returns the child window with the current focus.
- [func setAccessibilityFocusedWindow(Any?)](./nsaccessibilityprotocol/setaccessibilityfocusedwindow%28_%29.md)
  Sets the child window with the current focus.
- [func accessibilitySharedFocusElements() -> [Any]?](./nsaccessibilityprotocol/accessibilitysharedfocuselements%28%29.md)
  Returns the array of elements that shares the keyboard focus with the accessibility element.
- [func setAccessibilitySharedFocusElements([Any]?)](./nsaccessibilityprotocol/setaccessibilitysharedfocuselements%28_%29.md)
  Sets the array of elements that shares the keyboard focus with the accessibility element.
- [accessibilityApplicationFocusedUIElement](./nsaccessibility-c.protocol/accessibilityapplicationfocuseduielement.md)
  The child accessibility element with the current focus.
- [accessibilityFocused](./nsaccessibility-c.protocol/accessibilityfocused.md)
  A Boolean value that determines whether the accessibility element has the keyboard focus.
- [accessibilityFocusedWindow](./nsaccessibility-c.protocol/accessibilityfocusedwindow.md)
  The child window with the current focus.
- [accessibilitySharedFocusElements](./nsaccessibility-c.protocol/accessibilitysharedfocuselements.md)
  An array of elements that shares the keyboard focus with the accessibility element.
### Assigning roles
- [func isAccessibilityRequired() -> Bool](./nsaccessibilityprotocol/isaccessibilityrequired%28%29.md)
  Returns a Boolean value that determines whether the accessibility element must have content for successful submission of a form.
- [func setAccessibilityRequired(Bool)](./nsaccessibilityprotocol/setaccessibilityrequired%28_%29.md)
  Sets a Boolean value that determines whether the accessibility element must have content for successful submission of a form.
- [func accessibilityRole() -> NSAccessibility.Role?](./nsaccessibilityprotocol/accessibilityrole%28%29.md)
  Returns the type of interface element that the accessibility element represents.
- [func setAccessibilityRole(NSAccessibility.Role?)](./nsaccessibilityprotocol/setaccessibilityrole%28_%29.md)
  Sets the type of interface element that the accessibility element represents.
- [func accessibilityRoleDescription() -> String?](./nsaccessibilityprotocol/accessibilityroledescription%28%29.md)
  Returns a localized, human-intelligible description of the accessibility element’s role, such as *radio button*.
- [func setAccessibilityRoleDescription(String?)](./nsaccessibilityprotocol/setaccessibilityroledescription%28_%29.md)
  Sets the localized, human-intelligible description of the accessibility element’s role, such as *radio button*.
- [func accessibilitySubrole() -> NSAccessibility.Subrole?](./nsaccessibilityprotocol/accessibilitysubrole%28%29.md)
  Returns the specialized interface element type that the accessibility element represents.
- [func setAccessibilitySubrole(NSAccessibility.Subrole?)](./nsaccessibilityprotocol/setaccessibilitysubrole%28_%29.md)
  Sets the specialized interface element type that the accessibility element represents.
- [NSAccessibility.Role](./nsaccessibility-swift.struct/role.md)
  Values that describe types of objects that accessibility elements represent.
- [NSAccessibility.Subrole](./nsaccessibility-swift.struct/subrole.md)
  Values that describe specialized object subtypes that accessibility elements represent.
- [accessibilityRequired](./nsaccessibility-c.protocol/accessibilityrequired.md)
  A Boolean value that determines whether the accessibility element must have content for successful submission of a form.
- [accessibilityRole](./nsaccessibility-c.protocol/accessibilityrole.md)
  The type of interface element that the accessibility element represents.
- [accessibilityRoleDescription](./nsaccessibility-c.protocol/accessibilityroledescription.md)
  A localized, human-intelligible description of the accessibility element’s role, such as *radio button*.
- [accessibilitySubrole](./nsaccessibility-c.protocol/accessibilitysubrole.md)
  The specialized interface element type that the accessibility element represents.
### Assigning actions
- [func accessibilityCustomActions() -> [NSAccessibilityCustomAction]?](./nsaccessibilityprotocol/accessibilitycustomactions%28%29.md)
  Returns the custom actions of the current accessibility element.
- [func setAccessibilityCustomActions([NSAccessibilityCustomAction]?)](./nsaccessibilityprotocol/setaccessibilitycustomactions%28_%29.md)
  Sets the custom actions of the current accessibility element.
- [class NSAccessibilityCustomAction](./nsaccessibilitycustomaction.md)
  A custom action to perform on an accessible object.
- [accessibilityCustomActions](./nsaccessibility-c.protocol/accessibilitycustomactions.md)
  The custom actions of the current accessibility element.
### Assigning rotors
- [func accessibilityCustomRotors() -> [NSAccessibilityCustomRotor]](./nsaccessibilityprotocol/accessibilitycustomrotors%28%29.md)
  Returns the custom rotors of the current accessibility element.
- [func setAccessibilityCustomRotors([NSAccessibilityCustomRotor])](./nsaccessibilityprotocol/setaccessibilitycustomrotors%28_%29.md)
  Sets the custom rotors of the current accessibility element.
- [class NSAccessibilityCustomRotor](./nsaccessibilitycustomrotor.md)
  A context-sensitive function that helps VoiceOver users find the next instance of a related accessibility element.
- [accessibilityCustomRotors](./nsaccessibility-c.protocol/accessibilitycustomrotors.md)
  The custom rotors of the current accessibility element.
### Configuring text elements
- [func accessibilityInsertionPointLineNumber() -> Int](./nsaccessibilityprotocol/accessibilityinsertionpointlinenumber%28%29.md)
  Returns the line number that contains the insertion point.
- [func setAccessibilityInsertionPointLineNumber(Int)](./nsaccessibilityprotocol/setaccessibilityinsertionpointlinenumber%28_%29.md)
  Sets the line number that contains the insertion point.
- [func accessibilityNumberOfCharacters() -> Int](./nsaccessibilityprotocol/accessibilitynumberofcharacters%28%29.md)
  Returns the number of characters in the text.
- [func setAccessibilityNumberOfCharacters(Int)](./nsaccessibilityprotocol/setaccessibilitynumberofcharacters%28_%29.md)
  Sets the number of characters in the text.
- [func accessibilityPlaceholderValue() -> String?](./nsaccessibilityprotocol/accessibilityplaceholdervalue%28%29.md)
  Returns the placeholder value for the accessibility element.
- [func setAccessibilityPlaceholderValue(String?)](./nsaccessibilityprotocol/setaccessibilityplaceholdervalue%28_%29.md)
  Sets the placeholder value for the accessibility element.
- [func accessibilitySelectedText() -> String?](./nsaccessibilityprotocol/accessibilityselectedtext%28%29.md)
  Returns the currently selected text.
- [func setAccessibilitySelectedText(String?)](./nsaccessibilityprotocol/setaccessibilityselectedtext%28_%29.md)
  Sets the currently selected text.
- [func accessibilitySelectedTextRange() -> NSRange](./nsaccessibilityprotocol/accessibilityselectedtextrange%28%29.md)
  Returns the range of the currently selected text.
- [func setAccessibilitySelectedTextRange(NSRange)](./nsaccessibilityprotocol/setaccessibilityselectedtextrange%28_%29.md)
  Sets the range of the currently selected text.
- [func accessibilitySelectedTextRanges() -> [NSValue]?](./nsaccessibilityprotocol/accessibilityselectedtextranges%28%29.md)
  Returns an array of ranges for the currently selected text.
- [func setAccessibilitySelectedTextRanges([NSValue]?)](./nsaccessibilityprotocol/setaccessibilityselectedtextranges%28_%29.md)
  Sets an array of ranges for the currently selected text.
- [func accessibilitySharedCharacterRange() -> NSRange](./nsaccessibilityprotocol/accessibilitysharedcharacterrange%28%29.md)
  Returns the range of characters that the accessibility element displays.
- [func setAccessibilitySharedCharacterRange(NSRange)](./nsaccessibilityprotocol/setaccessibilitysharedcharacterrange%28_%29.md)
  Sets the range of characters that the accessibility element displays.
- [func accessibilitySharedTextUIElements() -> [Any]?](./nsaccessibilityprotocol/accessibilitysharedtextuielements%28%29.md)
  Returns the other elements that share text with the accessibility element.
- [func setAccessibilitySharedTextUIElements([Any]?)](./nsaccessibilityprotocol/setaccessibilitysharedtextuielements%28_%29.md)
  Sets the other elements that share text with the accessibility element.
- [func accessibilityVisibleCharacterRange() -> NSRange](./nsaccessibilityprotocol/accessibilityvisiblecharacterrange%28%29.md)
  Returns the range of visible characters in the document.
- [func setAccessibilityVisibleCharacterRange(NSRange)](./nsaccessibilityprotocol/setaccessibilityvisiblecharacterrange%28_%29.md)
  Sets the range of visible characters in the document.
- [func accessibilityString(for: NSRange) -> String?](./nsaccessibilityprotocol/accessibilitystring%28for%29.md)
  Returns the substring for the specified range.
- [func accessibilityAttributedString(for: NSRange) -> NSAttributedString?](./nsaccessibilityprotocol/accessibilityattributedstring%28for%29.md)
  Returns the attributed substring for the specified range of characters.
- [func accessibilityRTF(for: NSRange) -> Data?](./nsaccessibilityprotocol/accessibilityrtf%28for%29.md)
  Returns the rich text format (RTF) data that describes the specified range of characters.
- [func accessibilityFrame(for: NSRange) -> NSRect](./nsaccessibilityprotocol/accessibilityframe%28for%29.md)
  Returns the rectangle that encloses the specified range of characters.
- [func accessibilityLine(for: Int) -> Int](./nsaccessibilityprotocol/accessibilityline%28for%29.md)
  Returns the line number for the line that contains the specified character index.
- [func accessibilityRange(for: Int) -> NSRange](./nsaccessibilityprotocol/accessibilityrange%28for%29-6kv3.md)
  Returns the range of characters for the glyph that includes the specified character.
- [func accessibilityStyleRange(for: Int) -> NSRange](./nsaccessibilityprotocol/accessibilitystylerange%28for%29.md)
  Returns a range of characters that all have the same style as the specified character.
- [func accessibilityRange(forLine: Int) -> NSRange](./nsaccessibilityprotocol/accessibilityrange%28forline%29.md)
  Returns the range of characters in the specified line.
- [func accessibilityRange(for: NSPoint) -> NSRange](./nsaccessibilityprotocol/accessibilityrange%28for%29-1iudm.md)
  Returns the range of characters for the glyph at the specified point.
### Configuring windows
- [func accessibilityActivationPoint() -> NSPoint](./nsaccessibilityprotocol/accessibilityactivationpoint%28%29.md)
  Returns the activation point for the user interface element.
- [func setAccessibilityActivationPoint(NSPoint)](./nsaccessibilityprotocol/setaccessibilityactivationpoint%28_%29.md)
  Sets the activation point for the user interface element.
- [func isAccessibilityAlternateUIVisible() -> Bool](./nsaccessibilityprotocol/isaccessibilityalternateuivisible%28%29.md)
  Returns the Boolean value that determines whether the accessibility element’s alternative UI is currently visible.
- [func setAccessibilityAlternateUIVisible(Bool)](./nsaccessibilityprotocol/setaccessibilityalternateuivisible%28_%29.md)
  Sets the Boolean value that determines whether the accessibility element’s alternative UI is currently visible.
- [func accessibilityCancelButton() -> Any?](./nsaccessibilityprotocol/accessibilitycancelbutton%28%29.md)
  Returns the child accessibility element that represents the window’s cancel button.
- [func setAccessibilityCancelButton(Any?)](./nsaccessibilityprotocol/setaccessibilitycancelbutton%28_%29.md)
  Sets the child accessibility element that represents the window’s cancel button.
- [func accessibilityCloseButton() -> Any?](./nsaccessibilityprotocol/accessibilityclosebutton%28%29.md)
  Returns the child accessibility element that represents the window’s close button.
- [func setAccessibilityCloseButton(Any?)](./nsaccessibilityprotocol/setaccessibilityclosebutton%28_%29.md)
  Sets the child accessibility element that represents the window’s close button.
- [func accessibilityDefaultButton() -> Any?](./nsaccessibilityprotocol/accessibilitydefaultbutton%28%29.md)
  Returns the child accessibility element that represents the window’s default button.
- [func setAccessibilityDefaultButton(Any?)](./nsaccessibilityprotocol/setaccessibilitydefaultbutton%28_%29.md)
  Sets the child accessibility element that represents the window’s default button.
- [func accessibilityFullScreenButton() -> Any?](./nsaccessibilityprotocol/accessibilityfullscreenbutton%28%29.md)
  Returns the child accessibility element that represents the window’s full-screen button.
- [func setAccessibilityFullScreenButton(Any?)](./nsaccessibilityprotocol/setaccessibilityfullscreenbutton%28_%29.md)
  Sets the child accessibility element that represents the window’s full-screen button.
- [func accessibilityGrowArea() -> Any?](./nsaccessibilityprotocol/accessibilitygrowarea%28%29.md)
  Returns the child accessibility element that represents the window’s grow area.
- [func setAccessibilityGrowArea(Any?)](./nsaccessibilityprotocol/setaccessibilitygrowarea%28_%29.md)
  Sets the child accessibility element that represents the window’s grow area.
- [func isAccessibilityMain() -> Bool](./nsaccessibilityprotocol/isaccessibilitymain%28%29.md)
  Returns a Boolean value that determines whether the window is the app’s main window.
- [func setAccessibilityMain(Bool)](./nsaccessibilityprotocol/setaccessibilitymain%28_%29.md)
  Sets a Boolean value that determines whether the window is the app’s main window.
- [func accessibilityMinimizeButton() -> Any?](./nsaccessibilityprotocol/accessibilityminimizebutton%28%29.md)
  Returns the child accessibility element that represents the window’s minimize button.
- [func setAccessibilityMinimizeButton(Any?)](./nsaccessibilityprotocol/setaccessibilityminimizebutton%28_%29.md)
  Sets the child accessibility element that represents the window’s minimize button.
- [func isAccessibilityMinimized() -> Bool](./nsaccessibilityprotocol/isaccessibilityminimized%28%29.md)
  Returns the Boolean value that determines whether the window is in a minimized state.
- [func setAccessibilityMinimized(Bool)](./nsaccessibilityprotocol/setaccessibilityminimized%28_%29.md)
  Sets the Boolean value that determines whether the window is in a minimized state.
- [func isAccessibilityModal() -> Bool](./nsaccessibilityprotocol/isaccessibilitymodal%28%29.md)
  Returns a Boolean value that determines whether the window is modal.
- [func setAccessibilityModal(Bool)](./nsaccessibilityprotocol/setaccessibilitymodal%28_%29.md)
  Sets a Boolean value that determines whether the window is modal.
- [func accessibilityProxy() -> Any?](./nsaccessibilityprotocol/accessibilityproxy%28%29.md)
  Returns the child accessibility element that represents the window’s proxy icon.
- [func setAccessibilityProxy(Any?)](./nsaccessibilityprotocol/setaccessibilityproxy%28_%29.md)
  Sets the child accessibility element that represents the window’s proxy icon.
- [func accessibilityShownMenu() -> Any?](./nsaccessibilityprotocol/accessibilityshownmenu%28%29.md)
  Returns the menu currently displaying for the accessibility element.
- [func setAccessibilityShownMenu(Any?)](./nsaccessibilityprotocol/setaccessibilityshownmenu%28_%29.md)
  Sets the menu currently displaying for the accessibility element.
- [func accessibilityToolbarButton() -> Any?](./nsaccessibilityprotocol/accessibilitytoolbarbutton%28%29.md)
  Returns the child accessibility element that represents the window’s toolbar button.
- [func setAccessibilityToolbarButton(Any?)](./nsaccessibilityprotocol/setaccessibilitytoolbarbutton%28_%29.md)
  Sets the child accessibility element that represents the window’s toolbar button.
- [func accessibilityWindow() -> Any?](./nsaccessibilityprotocol/accessibilitywindow%28%29.md)
  Returns the window that contains the accessibility element.
- [func setAccessibilityWindow(Any?)](./nsaccessibilityprotocol/setaccessibilitywindow%28_%29.md)
  Sets the window that contains the accessibility element.
- [func accessibilityZoomButton() -> Any?](./nsaccessibilityprotocol/accessibilityzoombutton%28%29.md)
  Returns the child accessibility element that represents the window’s zoom button.
- [func setAccessibilityZoomButton(Any?)](./nsaccessibilityprotocol/setaccessibilityzoombutton%28_%29.md)
  Sets the child accessibility element that represents the window’s zoom button.
- [accessibilityActivationPoint](./nsaccessibility-c.protocol/accessibilityactivationpoint.md)
  The activation point for the user interface element.
- [accessibilityAlternateUIVisible](./nsaccessibility-c.protocol/accessibilityalternateuivisible.md)
  A Boolean value that determines whether the accessibility element’s alternative UI is currently visible.
- [accessibilityCancelButton](./nsaccessibility-c.protocol/accessibilitycancelbutton.md)
  The child accessibility element that represents the window’s cancel button.
- [accessibilityCloseButton](./nsaccessibility-c.protocol/accessibilityclosebutton.md)
  The child accessibility element that represents the window’s close button.
- [accessibilityDefaultButton](./nsaccessibility-c.protocol/accessibilitydefaultbutton.md)
  The child accessibility element that represents the window’s default button.
- [accessibilityFullScreenButton](./nsaccessibility-c.protocol/accessibilityfullscreenbutton.md)
  The child accessibility element that represents the window’s full-screen button.
- [accessibilityGrowArea](./nsaccessibility-c.protocol/accessibilitygrowarea.md)
  The child accessibility element that represents the window’s grow area.
- [accessibilityMain](./nsaccessibility-c.protocol/accessibilitymain.md)
  A Boolean value that determines whether the window is the app’s main window.
- [accessibilityMinimizeButton](./nsaccessibility-c.protocol/accessibilityminimizebutton.md)
  The child accessibility element that represents the window’s minimize button.
- [accessibilityMinimized](./nsaccessibility-c.protocol/accessibilityminimized.md)
  A Boolean value that determines whether this window is in a minimized state.
- [accessibilityModal](./nsaccessibility-c.protocol/accessibilitymodal.md)
  A Boolean value that determines whether the window is modal.
- [accessibilityProxy](./nsaccessibility-c.protocol/accessibilityproxy.md)
  The child accessibility element that represents the window’s proxy icon.
- [accessibilityShownMenu](./nsaccessibility-c.protocol/accessibilityshownmenu.md)
  The menu currently displaying for the accessibility element.
- [accessibilityToolbarButton](./nsaccessibility-c.protocol/accessibilitytoolbarbutton.md)
  The child accessibility element that represents the window’s toolbar button.
- [accessibilityWindow](./nsaccessibility-c.protocol/accessibilitywindow.md)
  The window that contains the accessibility element.
- [accessibilityZoomButton](./nsaccessibility-c.protocol/accessibilityzoombutton.md)
  The child accessibility element that represents the window’s zoom button.
### Managing apps
- [func accessibilityExtrasMenuBar() -> Any?](./nsaccessibilityprotocol/accessibilityextrasmenubar%28%29.md)
  Returns the icon for the app’s menu bar extra.
- [func setAccessibilityExtrasMenuBar(Any?)](./nsaccessibilityprotocol/setaccessibilityextrasmenubar%28_%29.md)
  Sets the icon for the app’s menu bar extra.
- [func isAccessibilityFrontmost() -> Bool](./nsaccessibilityprotocol/isaccessibilityfrontmost%28%29.md)
  Returns a Boolean value that determines whether the app is the frontmost app.
- [func setAccessibilityFrontmost(Bool)](./nsaccessibilityprotocol/setaccessibilityfrontmost%28_%29.md)
  Sets a Boolean value that determines whether the app is the frontmost app.
- [func isAccessibilityHidden() -> Bool](./nsaccessibilityprotocol/isaccessibilityhidden%28%29.md)
  Returns a Boolean value that determines whether the app is in a hidden state.
- [func setAccessibilityHidden(Bool)](./nsaccessibilityprotocol/setaccessibilityhidden%28_%29.md)
  Sets a Boolean value that determines whether the app is in a hidden state.
- [func accessibilityMainWindow() -> Any?](./nsaccessibilityprotocol/accessibilitymainwindow%28%29.md)
  Returns the app’s main window.
- [func setAccessibilityMainWindow(Any?)](./nsaccessibilityprotocol/setaccessibilitymainwindow%28_%29.md)
  Sets the app’s main window.
- [func accessibilityMenuBar() -> Any?](./nsaccessibilityprotocol/accessibilitymenubar%28%29.md)
  Returns the app’s menu bar.
- [func setAccessibilityMenuBar(Any?)](./nsaccessibilityprotocol/setaccessibilitymenubar%28_%29.md)
  Sets the app’s menu bar.
- [func accessibilityWindows() -> [Any]?](./nsaccessibilityprotocol/accessibilitywindows%28%29.md)
  Returns an array that contains all the app’s windows.
- [func setAccessibilityWindows([Any]?)](./nsaccessibilityprotocol/setaccessibilitywindows%28_%29.md)
  Sets the array that contains all the app’s windows.
- [accessibilityExtrasMenuBar](./nsaccessibility-c.protocol/accessibilityextrasmenubar.md)
  The icon for the app’s menu bar extra.
- [accessibilityFrontmost](./nsaccessibility-c.protocol/accessibilityfrontmost.md)
  A Boolean value that determines whether the app is the frontmost app.
- [accessibilityHidden](./nsaccessibility-c.protocol/accessibilityhidden.md)
  A Boolean value that determines whether the app is in a hidden state.
- [accessibilityMainWindow](./nsaccessibility-c.protocol/accessibilitymainwindow.md)
  The app’s main window.
- [accessibilityMenuBar](./nsaccessibility-c.protocol/accessibilitymenubar.md)
  The app’s menu bar.
- [accessibilityWindows](./nsaccessibility-c.protocol/accessibilitywindows.md)
  An array that contains all the app’s windows.
### Configuring grid views
- [func accessibilityColumnCount() -> Int](./nsaccessibilityprotocol/accessibilitycolumncount%28%29.md)
  Returns the number of columns in the accessibility element’s grid.
- [func setAccessibilityColumnCount(Int)](./nsaccessibilityprotocol/setaccessibilitycolumncount%28_%29.md)
  Sets the number of columns in the accessibility element’s grid.
- [func isAccessibilityOrderedByRow() -> Bool](./nsaccessibilityprotocol/isaccessibilityorderedbyrow%28%29.md)
  Returns a Boolean value that determines whether the accessibility element’s grid is in row major order or in column major order.
- [func setAccessibilityOrderedByRow(Bool)](./nsaccessibilityprotocol/setaccessibilityorderedbyrow%28_%29.md)
  Sets a Boolean value that determines whether the element’s grid is in row major order or in column major order.
- [func accessibilityRowCount() -> Int](./nsaccessibilityprotocol/accessibilityrowcount%28%29.md)
  Returns the number of rows in the accessibility element’s grid.
- [func setAccessibilityRowCount(Int)](./nsaccessibilityprotocol/setaccessibilityrowcount%28_%29.md)
  Sets the number of rows in the accessibility element’s grid.
- [accessibilityColumnCount](./nsaccessibility-c.protocol/accessibilitycolumncount.md)
  The number of columns in the accessibility element’s grid.
- [accessibilityOrderedByRow](./nsaccessibility-c.protocol/accessibilityorderedbyrow.md)
  A Boolean value that determines whether the accessibility element’s grid is in row major order or in column major order.
- [accessibilityRowCount](./nsaccessibility-c.protocol/accessibilityrowcount.md)
  The number of rows in the accessibility element’s grid.
### Configuring scroll views
- [func accessibilityHorizontalScrollBar() -> Any?](./nsaccessibilityprotocol/accessibilityhorizontalscrollbar%28%29.md)
  Returns the horizontal scroll bar for the scroll view.
- [func setAccessibilityHorizontalScrollBar(Any?)](./nsaccessibilityprotocol/setaccessibilityhorizontalscrollbar%28_%29.md)
  Sets the horizontal scroll bar for the scroll view.
- [func accessibilityVerticalScrollBar() -> Any?](./nsaccessibilityprotocol/accessibilityverticalscrollbar%28%29.md)
  Returns the vertical scroll bar for the scroll view.
- [func setAccessibilityVerticalScrollBar(Any?)](./nsaccessibilityprotocol/setaccessibilityverticalscrollbar%28_%29.md)
  Sets the vertical scroll bar for the scroll view.
- [accessibilityHorizontalScrollBar](./nsaccessibility-c.protocol/accessibilityhorizontalscrollbar.md)
  The horizontal scroll bar for the scroll view.
- [accessibilityVerticalScrollBar](./nsaccessibility-c.protocol/accessibilityverticalscrollbar.md)
  The vertical scroll bar for the scroll view.
### Configuring table and outline views
- [func accessibilityColumnHeaderUIElements() -> [Any]?](./nsaccessibilityprotocol/accessibilitycolumnheaderuielements%28%29.md)
  Returns the column header accessibility elements for the table or outline.
- [func setAccessibilityColumnHeaderUIElements([Any]?)](./nsaccessibilityprotocol/setaccessibilitycolumnheaderuielements%28_%29.md)
  Sets the column header accessibility elements for the table or outline.
- [func accessibilityColumns() -> [Any]?](./nsaccessibilityprotocol/accessibilitycolumns%28%29.md)
  Returns the column accessibility elements for the table or outline.
- [func setAccessibilityColumns([Any]?)](./nsaccessibilityprotocol/setaccessibilitycolumns%28_%29.md)
  Sets the column accessibility elements for the table or outline.
- [func accessibilityColumnTitles() -> [Any]?](./nsaccessibilityprotocol/accessibilitycolumntitles%28%29.md)
  Returns the column titles for the accessibility element.
- [func setAccessibilityColumnTitles([Any]?)](./nsaccessibilityprotocol/setaccessibilitycolumntitles%28_%29.md)
  Sets the column titles for the accessibility element.
- [func isAccessibilityExpanded() -> Bool](./nsaccessibilityprotocol/isaccessibilityexpanded%28%29.md)
  Returns a Boolean value that determines whether the accessibility element is in an expanded state.
- [func setAccessibilityExpanded(Bool)](./nsaccessibilityprotocol/setaccessibilityexpanded%28_%29.md)
  Sets a Boolean value that determines whether accessibility element is in an expanded state.
- [func accessibilityHeader() -> Any?](./nsaccessibilityprotocol/accessibilityheader%28%29.md)
  Returns the header for the table view.
- [func setAccessibilityHeader(Any?)](./nsaccessibilityprotocol/setaccessibilityheader%28_%29.md)
  Sets the header for the table view.
- [func accessibilityIndex() -> Int](./nsaccessibilityprotocol/accessibilityindex%28%29.md)
  Returns the index of the row or column that the accessibility element represents.
- [func setAccessibilityIndex(Int)](./nsaccessibilityprotocol/setaccessibilityindex%28_%29.md)
  Sets the index of the row or column that the accessibility element represents.
- [func accessibilityRowHeaderUIElements() -> [Any]?](./nsaccessibilityprotocol/accessibilityrowheaderuielements%28%29.md)
  Returns the row header accessibility elements for the table or outline.
- [func setAccessibilityRowHeaderUIElements([Any]?)](./nsaccessibilityprotocol/setaccessibilityrowheaderuielements%28_%29.md)
  Sets the row header accessibility elements for the table or outline.
- [func accessibilityRows() -> [Any]?](./nsaccessibilityprotocol/accessibilityrows%28%29.md)
  Returns the row accessibility elements for the table or outline.
- [func setAccessibilityRows([Any]?)](./nsaccessibilityprotocol/setaccessibilityrows%28_%29.md)
  Sets the row accessibility elements for the table or outline.
- [func accessibilitySelectedColumns() -> [Any]?](./nsaccessibilityprotocol/accessibilityselectedcolumns%28%29.md)
  Returns the currently selected columns for the table or outline.
- [func setAccessibilitySelectedColumns([Any]?)](./nsaccessibilityprotocol/setaccessibilityselectedcolumns%28_%29.md)
  Sets the currently selected columns for the table or outline.
- [func accessibilitySelectedRows() -> [Any]?](./nsaccessibilityprotocol/accessibilityselectedrows%28%29.md)
  Returns the currently selected rows for the table or outline.
- [func setAccessibilitySelectedRows([Any]?)](./nsaccessibilityprotocol/setaccessibilityselectedrows%28_%29.md)
  Sets the currently selected rows for the table or outline.
- [func accessibilitySortDirection() -> NSAccessibilitySortDirection](./nsaccessibilityprotocol/accessibilitysortdirection%28%29.md)
  Returns the accessibility element’s sort direction.
- [func setAccessibilitySortDirection(NSAccessibilitySortDirection)](./nsaccessibilityprotocol/setaccessibilitysortdirection%28_%29.md)
  Sets the accessibility element’s sort direction.
- [func accessibilityVisibleColumns() -> [Any]?](./nsaccessibilityprotocol/accessibilityvisiblecolumns%28%29.md)
  Returns the visible columns for the table or outline.
- [func setAccessibilityVisibleColumns([Any]?)](./nsaccessibilityprotocol/setaccessibilityvisiblecolumns%28_%29.md)
  Sets the visible columns for the table or outline.
- [func accessibilityVisibleRows() -> [Any]?](./nsaccessibilityprotocol/accessibilityvisiblerows%28%29.md)
  Returns the visible rows for the table or outline.
- [func setAccessibilityVisibleRows([Any]?)](./nsaccessibilityprotocol/setaccessibilityvisiblerows%28_%29.md)
  Sets the visible rows for the table or outline.
- [enum NSAccessibilitySortDirection](./nsaccessibilitysortdirection.md)
  Values that indicate the sort direction of a column.
- [accessibilityColumnHeaderUIElements](./nsaccessibility-c.protocol/accessibilitycolumnheaderuielements.md)
  The column header accessibility elements for the table or outline.
- [accessibilityColumns](./nsaccessibility-c.protocol/accessibilitycolumns.md)
  The column accessibility elements for the table or outline.
- [accessibilityColumnTitles](./nsaccessibility-c.protocol/accessibilitycolumntitles.md)
  The column titles for the accessibility element.
- [accessibilityExpanded](./nsaccessibility-c.protocol/accessibilityexpanded.md)
  A Boolean value that determines whether the accessibility element is in an expanded state.
- [accessibilityHeader](./nsaccessibility-c.protocol/accessibilityheader.md)
  The header for the table view.
- [accessibilityIndex](./nsaccessibility-c.protocol/accessibilityindex.md)
  The index of the row or column that the accessibility element represents.
- [accessibilityRowHeaderUIElements](./nsaccessibility-c.protocol/accessibilityrowheaderuielements.md)
  The row header accessibility elements for the table or outline.
- [accessibilityRows](./nsaccessibility-c.protocol/accessibilityrows.md)
  The row accessibility elements for the table or outline.
- [accessibilitySelectedColumns](./nsaccessibility-c.protocol/accessibilityselectedcolumns.md)
  The currently selected columns for the table or outline.
- [accessibilitySelectedRows](./nsaccessibility-c.protocol/accessibilityselectedrows.md)
  The currently selected rows for the table or outline.
- [accessibilitySortDirection](./nsaccessibility-c.protocol/accessibilitysortdirection.md)
  The accessibility element’s sort direction.
- [accessibilityVisibleColumns](./nsaccessibility-c.protocol/accessibilityvisiblecolumns.md)
  The visible columns for the table or outline.
- [accessibilityVisibleRows](./nsaccessibility-c.protocol/accessibilityvisiblerows.md)
  The visible rows for the table or outline.
### Configuring outline rows
- [func isAccessibilityDisclosed() -> Bool](./nsaccessibilityprotocol/isaccessibilitydisclosed%28%29.md)
  Returns a Boolean value that determines whether the row is disclosing other rows.
- [func setAccessibilityDisclosed(Bool)](./nsaccessibilityprotocol/setaccessibilitydisclosed%28_%29.md)
  Sets a Boolean value that determines whether the row is disclosing other rows.
- [func accessibilityDisclosedByRow() -> Any?](./nsaccessibilityprotocol/accessibilitydisclosedbyrow%28%29.md)
  Returns the row disclosing the current row.
- [func setAccessibilityDisclosedByRow(Any?)](./nsaccessibilityprotocol/setaccessibilitydisclosedbyrow%28_%29.md)
  Sets the row disclosing the current row.
- [func accessibilityDisclosedRows() -> Any?](./nsaccessibilityprotocol/accessibilitydisclosedrows%28%29.md)
  Returns the rows that the current row discloses.
- [func setAccessibilityDisclosedRows(Any?)](./nsaccessibilityprotocol/setaccessibilitydisclosedrows%28_%29.md)
  Sets the rows that the current row discloses.
- [func accessibilityDisclosureLevel() -> Int](./nsaccessibilityprotocol/accessibilitydisclosurelevel%28%29.md)
  Returns the indention level for the row.
- [func setAccessibilityDisclosureLevel(Int)](./nsaccessibilityprotocol/setaccessibilitydisclosurelevel%28_%29.md)
  Sets the indention level for the row.
- [accessibilityDisclosed](./nsaccessibility-c.protocol/accessibilitydisclosed.md)
  A Boolean value that determines whether the row is disclosing other rows.
- [accessibilityDisclosedByRow](./nsaccessibility-c.protocol/accessibilitydisclosedbyrow.md)
  The row disclosing the current row.
- [accessibilityDisclosedRows](./nsaccessibility-c.protocol/accessibilitydisclosedrows.md)
  The rows that the current row discloses.
- [accessibilityDisclosureLevel](./nsaccessibility-c.protocol/accessibilitydisclosurelevel.md)
  The indention level for the row.
### Configuring cell-based tables
- [func accessibilityColumnIndexRange() -> NSRange](./nsaccessibilityprotocol/accessibilitycolumnindexrange%28%29.md)
  Returns the column index range of the cell.
- [func setAccessibilityColumnIndexRange(NSRange)](./nsaccessibilityprotocol/setaccessibilitycolumnindexrange%28_%29.md)
  Sets the column index range of the cell.
- [func accessibilityRowIndexRange() -> NSRange](./nsaccessibilityprotocol/accessibilityrowindexrange%28%29.md)
  Returns the row index range of the cell.
- [func setAccessibilityRowIndexRange(NSRange)](./nsaccessibilityprotocol/setaccessibilityrowindexrange%28_%29.md)
  Sets the row index range of the cell.
- [func accessibilitySelectedCells() -> [Any]?](./nsaccessibilityprotocol/accessibilityselectedcells%28%29.md)
  Returns the currently selected cells for the table.
- [func setAccessibilitySelectedCells([Any]?)](./nsaccessibilityprotocol/setaccessibilityselectedcells%28_%29.md)
  Sets the currently selected cells for the table.
- [func accessibilityVisibleCells() -> [Any]?](./nsaccessibilityprotocol/accessibilityvisiblecells%28%29.md)
  Returns the visible cells for the table.
- [func setAccessibilityVisibleCells([Any]?)](./nsaccessibilityprotocol/setaccessibilityvisiblecells%28_%29.md)
  Sets the visible cells for the table.
- [func accessibilityCell(forColumn: Int, row: Int) -> Any?](./nsaccessibilityprotocol/accessibilitycell%28forcolumn,row%29.md)
  Returns the cell at the specified column and row.
- [accessibilityColumnIndexRange](./nsaccessibility-c.protocol/accessibilitycolumnindexrange.md)
  The column index range of the cell.
- [accessibilityRowIndexRange](./nsaccessibility-c.protocol/accessibilityrowindexrange.md)
  The row index range of the cell.
- [accessibilitySelectedCells](./nsaccessibility-c.protocol/accessibilityselectedcells.md)
  The currently selected cells for the table.
- [accessibilityVisibleCells](./nsaccessibility-c.protocol/accessibilityvisiblecells.md)
  The visible cells for the table.
### Configuring layout
- [func accessibilityHandles() -> [Any]?](./nsaccessibilityprotocol/accessibilityhandles%28%29.md)
  Returns the drag handle elements for the layout item element.
- [func setAccessibilityHandles([Any]?)](./nsaccessibilityprotocol/setaccessibilityhandles%28_%29.md)
  Sets the drag handle accessibility elements for the layout item element.
- [func accessibilityHorizontalUnits() -> NSAccessibilityUnits](./nsaccessibilityprotocol/accessibilityhorizontalunits%28%29.md)
  Returns the units that the layout area uses for horizontal values.
- [func setAccessibilityHorizontalUnits(NSAccessibilityUnits)](./nsaccessibilityprotocol/setaccessibilityhorizontalunits%28_%29.md)
  Sets the units that the layout area uses for horizontal values.
- [func accessibilityHorizontalUnitDescription() -> String?](./nsaccessibilityprotocol/accessibilityhorizontalunitdescription%28%29.md)
  Returns the description of the layout area’s horizontal units.
- [func setAccessibilityHorizontalUnitDescription(String?)](./nsaccessibilityprotocol/setaccessibilityhorizontalunitdescription%28_%29.md)
  Sets the description of the layout area’s horizontal units.
- [func accessibilityVerticalUnits() -> NSAccessibilityUnits](./nsaccessibilityprotocol/accessibilityverticalunits%28%29.md)
  Returns the units that the layout area uses for vertical values.
- [func setAccessibilityVerticalUnits(NSAccessibilityUnits)](./nsaccessibilityprotocol/setaccessibilityverticalunits%28_%29.md)
  Sets the units that the layout area uses for vertical values.
- [func accessibilityVerticalUnitDescription() -> String?](./nsaccessibilityprotocol/accessibilityverticalunitdescription%28%29.md)
  Returns the description of the layout area’s vertical units.
- [func setAccessibilityVerticalUnitDescription(String?)](./nsaccessibilityprotocol/setaccessibilityverticalunitdescription%28_%29.md)
  Sets the description of the layout area’s vertical units.
- [func accessibilityLayoutPoint(forScreenPoint: NSPoint) -> NSPoint](./nsaccessibilityprotocol/accessibilitylayoutpoint%28forscreenpoint%29.md)
  Converts the provided point in screen coordinates to a point in the layout area’s coordinate system.
- [func accessibilityLayoutSize(forScreenSize: NSSize) -> NSSize](./nsaccessibilityprotocol/accessibilitylayoutsize%28forscreensize%29.md)
  Converts the provided size in screen coordinates to a size in the layout area’s coordinate system.
- [func accessibilityScreenPoint(forLayoutPoint: NSPoint) -> NSPoint](./nsaccessibilityprotocol/accessibilityscreenpoint%28forlayoutpoint%29.md)
  Converts the provided point in the layout area’s coordinates to a point in the screen’s coordinate system.
- [func accessibilityScreenSize(forLayoutSize: NSSize) -> NSSize](./nsaccessibilityprotocol/accessibilityscreensize%28forlayoutsize%29.md)
  Converts the provided size in the layout area’s coordinates to a size in the screen’s coordinate system.
- [accessibilityHandles](./nsaccessibility-c.protocol/accessibilityhandles.md)
  The drag handle accessibility elements for the layout item element.
- [accessibilityHorizontalUnits](./nsaccessibility-c.protocol/accessibilityhorizontalunits.md)
  The units that the layout area uses for horizontal values.
- [accessibilityHorizontalUnitDescription](./nsaccessibility-c.protocol/accessibilityhorizontalunitdescription.md)
  A description of the layout area’s horizontal units.
- [accessibilityVerticalUnits](./nsaccessibility-c.protocol/accessibilityverticalunits.md)
  The units that the layout area uses for vertical values.
- [accessibilityVerticalUnitDescription](./nsaccessibility-c.protocol/accessibilityverticalunitdescription.md)
  A description of the layout area’s vertical units.
### Configuring sliders
- [func accessibilityAllowedValues() -> [NSNumber]?](./nsaccessibilityprotocol/accessibilityallowedvalues%28%29.md)
  Returns the allowed values for the slider accessibility element.
- [func setAccessibilityAllowedValues([NSNumber]?)](./nsaccessibilityprotocol/setaccessibilityallowedvalues%28_%29.md)
  Sets the allowed values for the slider accessibility element.
- [func accessibilityLabelUIElements() -> [Any]?](./nsaccessibilityprotocol/accessibilitylabeluielements%28%29.md)
  Returns the child label elements for the slider accessibility element.
- [func setAccessibilityLabelUIElements([Any]?)](./nsaccessibilityprotocol/setaccessibilitylabeluielements%28_%29.md)
  Sets the child label elements for the slider accessibility element.
- [func accessibilityLabelValue() -> Float](./nsaccessibilityprotocol/accessibilitylabelvalue%28%29.md)
  Returns the value of the label accessibility element.
- [func setAccessibilityLabelValue(Float)](./nsaccessibilityprotocol/setaccessibilitylabelvalue%28_%29.md)
  Sets the value of the label accessibility element.
- [accessibilityAllowedValues](./nsaccessibility-c.protocol/accessibilityallowedvalues.md)
  The allowed values for the slider accessibility element.
- [accessibilityLabelUIElements](./nsaccessibility-c.protocol/accessibilitylabeluielements.md)
  The child label elements for the slider accessibility element.
- [accessibilityLabelValue](./nsaccessibility-c.protocol/accessibilitylabelvalue.md)
  The value of the label accessibility element.
### Configuring split views
- [func accessibilityNextContents() -> [Any]?](./nsaccessibilityprotocol/accessibilitynextcontents%28%29.md)
  Returns the contents that follow the divider accessibility element.
- [func setAccessibilityNextContents([Any]?)](./nsaccessibilityprotocol/setaccessibilitynextcontents%28_%29.md)
  Sets the contents that follow the divider accessibility element.
- [func accessibilityPreviousContents() -> [Any]?](./nsaccessibilityprotocol/accessibilitypreviouscontents%28%29.md)
  Returns the contents that precede the divider accessibility element.
- [func setAccessibilityPreviousContents([Any]?)](./nsaccessibilityprotocol/setaccessibilitypreviouscontents%28_%29.md)
  Sets the contents that precede the divider accessibility element.
- [func accessibilitySplitters() -> [Any]?](./nsaccessibilityprotocol/accessibilitysplitters%28%29.md)
  Returns an array that contains the views and splitter bar from the split view.
- [func setAccessibilitySplitters([Any]?)](./nsaccessibilityprotocol/setaccessibilitysplitters%28_%29.md)
  Sets the array that contains the views and splitter bar from the split view.
- [accessibilityNextContents](./nsaccessibility-c.protocol/accessibilitynextcontents.md)
  The contents that follow the divider accessibility element.
- [accessibilityPreviousContents](./nsaccessibility-c.protocol/accessibilitypreviouscontents.md)
  The contents that precede the divider accessibility element.
- [accessibilitySplitters](./nsaccessibility-c.protocol/accessibilitysplitters.md)
  An array that contains the views and splitter bar from the split view.
### Configuring tabs and toolbars
- [func accessibilityOverflowButton() -> Any?](./nsaccessibilityprotocol/accessibilityoverflowbutton%28%29.md)
  Returns the overflow button for the toolbar.
- [func setAccessibilityOverflowButton(Any?)](./nsaccessibilityprotocol/setaccessibilityoverflowbutton%28_%29.md)
  Sets the overflow button for the toolbar.
- [func accessibilityTabs() -> [Any]?](./nsaccessibilityprotocol/accessibilitytabs%28%29.md)
  Returns the tab accessibility elements for the tab view.
- [func setAccessibilityTabs([Any]?)](./nsaccessibilityprotocol/setaccessibilitytabs%28_%29.md)
  Sets the tab accessibility elements for the tab view.
- [accessibilityOverflowButton](./nsaccessibility-c.protocol/accessibilityoverflowbutton.md)
  The overflow button for the toolbar.
- [accessibilityTabs](./nsaccessibility-c.protocol/accessibilitytabs.md)
  The tab accessibility elements for the tab view.
### Configuring ruler views
- [func accessibilityMarkerGroupUIElement() -> Any?](./nsaccessibilityprotocol/accessibilitymarkergroupuielement%28%29.md)
  Returns the user interface element that functions as a marker group for the ruler accessibility element.
- [func setAccessibilityMarkerGroupUIElement(Any?)](./nsaccessibilityprotocol/setaccessibilitymarkergroupuielement%28_%29.md)
  Sets the user interface element that functions as a marker group for the ruler accessibility element.
- [func accessibilityMarkerTypeDescription() -> String?](./nsaccessibilityprotocol/accessibilitymarkertypedescription%28%29.md)
  Returns the human-readable description of the marker type.
- [func setAccessibilityMarkerTypeDescription(String?)](./nsaccessibilityprotocol/setaccessibilitymarkertypedescription%28_%29.md)
  Sets the human-readable description of the marker type.
- [func accessibilityMarkerUIElements() -> [Any]?](./nsaccessibilityprotocol/accessibilitymarkeruielements%28%29.md)
  Returns the array of marker accessibility elements for the ruler.
- [func setAccessibilityMarkerUIElements([Any]?)](./nsaccessibilityprotocol/setaccessibilitymarkeruielements%28_%29.md)
  Sets the array of marker accessibility elements for the ruler.
- [func accessibilityMarkerValues() -> Any?](./nsaccessibilityprotocol/accessibilitymarkervalues%28%29.md)
  Returns the marker values for the ruler.
- [func setAccessibilityMarkerValues(Any?)](./nsaccessibilityprotocol/setaccessibilitymarkervalues%28_%29.md)
  Sets the marker values for the ruler.
- [func accessibilityRulerMarkerType() -> NSAccessibilityRulerMarkerType](./nsaccessibilityprotocol/accessibilityrulermarkertype%28%29.md)
  Returns the type of markers for the ruler.
- [func setAccessibilityRulerMarkerType(NSAccessibilityRulerMarkerType)](./nsaccessibilityprotocol/setaccessibilityrulermarkertype%28_%29.md)
  Sets the type of markers for the ruler.
- [func accessibilityUnits() -> NSAccessibilityUnits](./nsaccessibilityprotocol/accessibilityunits%28%29.md)
  Returns the units for the ruler.
- [func setAccessibilityUnits(NSAccessibilityUnits)](./nsaccessibilityprotocol/setaccessibilityunits%28_%29.md)
  Sets the units used for the ruler.
- [func accessibilityUnitDescription() -> String?](./nsaccessibilityprotocol/accessibilityunitdescription%28%29.md)
  Returns the human-readable description of the ruler’s units.
- [func setAccessibilityUnitDescription(String?)](./nsaccessibilityprotocol/setaccessibilityunitdescription%28_%29.md)
  Sets the human-readable description of the ruler’s units.
- [enum NSAccessibilityRulerMarkerType](./nsaccessibilityrulermarkertype.md)
  Values that indicate the marker type of an accessibility element.
- [enum NSAccessibilityUnits](./nsaccessibilityunits.md)
  Values that indicate the unit values of a ruler or layout area.
- [accessibilityMarkerGroupUIElement](./nsaccessibility-c.protocol/accessibilitymarkergroupuielement.md)
  The user interface element that functions as a marker group for the ruler accessibility element.
- [accessibilityMarkerTypeDescription](./nsaccessibility-c.protocol/accessibilitymarkertypedescription.md)
  A human-readable description of the marker type.
- [accessibilityMarkerUIElements](./nsaccessibility-c.protocol/accessibilitymarkeruielements.md)
  An array of marker accessibility elements for the ruler.
- [accessibilityMarkerValues](./nsaccessibility-c.protocol/accessibilitymarkervalues.md)
  The marker values for the ruler.
- [accessibilityRulerMarkerType](./nsaccessibility-c.protocol/accessibilityrulermarkertype.md)
  The type of markers for the ruler.
- [accessibilityUnits](./nsaccessibility-c.protocol/accessibilityunits.md)
  The units for the ruler.
- [accessibilityUnitDescription](./nsaccessibility-c.protocol/accessibilityunitdescription.md)
  A human-readable description of the ruler’s units.
### Managing documents and editing
- [func accessibilityDocument() -> String?](./nsaccessibilityprotocol/accessibilitydocument%28%29.md)
  Returns the URL for the file that the accessibility element represents.
- [func setAccessibilityDocument(String?)](./nsaccessibilityprotocol/setaccessibilitydocument%28_%29.md)
  Sets the URL for the file that the accessibility element represents.
- [func isAccessibilityEdited() -> Bool](./nsaccessibilityprotocol/isaccessibilityedited%28%29.md)
  Returns a Boolean value that indicates whether the accessibility element is in an edited state.
- [func setAccessibilityEdited(Bool)](./nsaccessibilityprotocol/setaccessibilityedited%28_%29.md)
  Sets a Boolean value that indicates whether the accessibility element is in an edited state.
- [func accessibilityFilename() -> String?](./nsaccessibilityprotocol/accessibilityfilename%28%29.md)
  Returns the filename for the file that the accessibility element represents.
- [func setAccessibilityFilename(String?)](./nsaccessibilityprotocol/setaccessibilityfilename%28_%29.md)
  Sets the filename for the file that the accessibility element represents.
- [accessibilityDocument](./nsaccessibility-c.protocol/accessibilitydocument.md)
  The URL for the file that the accessibility element represents.
- [accessibilityEdited](./nsaccessibility-c.protocol/accessibilityedited.md)
  A Boolean value that indicates whether the accessibility element is in an edited state.
- [accessibilityFilename](./nsaccessibility-c.protocol/accessibilityfilename.md)
  The filename for the file that the accessibility element represents.
### Configuring linkage elements
- [func accessibilityLinkedUIElements() -> [Any]?](./nsaccessibilityprotocol/accessibilitylinkeduielements%28%29.md)
  Returns the elements that have links with the accessibility element.
- [func setAccessibilityLinkedUIElements([Any]?)](./nsaccessibilityprotocol/setaccessibilitylinkeduielements%28_%29.md)
  Sets the elements that have links with the accessibility element.
- [func accessibilityServesAsTitleForUIElements() -> [Any]?](./nsaccessibilityprotocol/accessibilityservesastitleforuielements%28%29.md)
  Returns the list of elements that the accessibility element is a title for.
- [func setAccessibilityServesAsTitleForUIElements([Any]?)](./nsaccessibilityprotocol/setaccessibilityservesastitleforuielements%28_%29.md)
  Sets the list of elements that the accessibility element is a title for.
- [func accessibilityTitleUIElement() -> Any?](./nsaccessibilityprotocol/accessibilitytitleuielement%28%29.md)
  Returns the static text element that represents the accessibility element’s title.
- [func setAccessibilityTitleUIElement(Any?)](./nsaccessibilityprotocol/setaccessibilitytitleuielement%28_%29.md)
  Sets the static text element that represents the accessibility element’s title.
- [accessibilityLinkedUIElements](./nsaccessibility-c.protocol/accessibilitylinkeduielements.md)
  The elements that have links with the accessibility element.
- [accessibilityServesAsTitleForUIElements](./nsaccessibility-c.protocol/accessibilityservesastitleforuielements.md)
  The list of elements that the accessibility element is a title for.
- [accessibilityTitleUIElement](./nsaccessibility-c.protocol/accessibilitytitleuielement.md)
  A static text element that represents the accessibility element’s title.
### Configuring search fields
- [func accessibilityClearButton() -> Any?](./nsaccessibilityprotocol/accessibilityclearbutton%28%29.md)
  Returns the clear button for the search field.
- [func setAccessibilityClearButton(Any?)](./nsaccessibilityprotocol/setaccessibilityclearbutton%28_%29.md)
  Sets the clear button for the search field.
- [func accessibilitySearchButton() -> Any?](./nsaccessibilityprotocol/accessibilitysearchbutton%28%29.md)
  Returns the search button for the search field.
- [func setAccessibilitySearchButton(Any?)](./nsaccessibilityprotocol/setaccessibilitysearchbutton%28_%29.md)
  Sets the search button for the search field.
- [func accessibilitySearchMenu() -> Any?](./nsaccessibilityprotocol/accessibilitysearchmenu%28%29.md)
  Returns the search menu for the search field.
- [func setAccessibilitySearchMenu(Any?)](./nsaccessibilityprotocol/setaccessibilitysearchmenu%28_%29.md)
  Sets the search menu for the search field.
- [accessibilityClearButton](./nsaccessibility-c.protocol/accessibilityclearbutton.md)
  The clear button for the search field.
- [accessibilitySearchButton](./nsaccessibility-c.protocol/accessibilitysearchbutton.md)
  The search button for the search field.
- [accessibilitySearchMenu](./nsaccessibility-c.protocol/accessibilitysearchmenu.md)
  The search menu for the search field.
### Confirming and canceling operations
- [func accessibilityPerformCancel() -> Bool](./nsaccessibilityprotocol/accessibilityperformcancel%28%29.md)
  Cancels the current operation.
- [func accessibilityPerformConfirm() -> Bool](./nsaccessibilityprotocol/accessibilityperformconfirm%28%29.md)
  Simulates pressing Return in the accessibility element.
### Selecting elements
- [func accessibilityPerformPick() -> Bool](./nsaccessibilityprotocol/accessibilityperformpick%28%29.md)
  Selects the accessibility element.
- [func accessibilityPerformPress() -> Bool](./nsaccessibilityprotocol/accessibilityperformpress%28%29.md)
  Simulates clicking the accessibility element.
### Searching elements
- [let NSAccessibilitySearchCurrentElementKey: String](./nsaccessibilitysearchcurrentelementkey.md)
- [let NSAccessibilitySearchCurrentRangeKey: String](./nsaccessibilitysearchcurrentrangekey.md)
- [let NSAccessibilitySearchDirectionKey: String](./nsaccessibilitysearchdirectionkey.md)
- [let NSAccessibilitySearchDirectionNext: String](./nsaccessibilitysearchdirectionnext.md)
- [let NSAccessibilitySearchDirectionPrevious: String](./nsaccessibilitysearchdirectionprevious.md)
- [struct NSAccessibilitySearchKey](./nsaccessibilitysearchkey.md)
### Showing user interface elements
- [func accessibilityPerformShowAlternateUI() -> Bool](./nsaccessibilityprotocol/accessibilityperformshowalternateui%28%29.md)
  Displays the accessibility element’s alternative UI.
- [func accessibilityPerformShowDefaultUI() -> Bool](./nsaccessibilityprotocol/accessibilityperformshowdefaultui%28%29.md)
  Returns to the accessibility element’s original UI.
- [func accessibilityPerformShowMenu() -> Bool](./nsaccessibilityprotocol/accessibilityperformshowmenu%28%29.md)
  Displays the menu accessibility element.
- [func accessibilityPerformRaise() -> Bool](./nsaccessibilityprotocol/accessibilityperformraise%28%29.md)
  Brings the window to the front.
### Incrementing, decrementing, and deleting values
- [func accessibilityIncrementButton() -> Any?](./nsaccessibilityprotocol/accessibilityincrementbutton%28%29.md)
  Returns the increment button for the stepper accessibility element.
- [func setAccessibilityIncrementButton(Any?)](./nsaccessibilityprotocol/setaccessibilityincrementbutton%28_%29.md)
  Sets the increment button for the stepper accessibility element.
- [func accessibilityDecrementButton() -> Any?](./nsaccessibilityprotocol/accessibilitydecrementbutton%28%29.md)
  Returns the decrement button for the stepper accessibility element.
- [func setAccessibilityDecrementButton(Any?)](./nsaccessibilityprotocol/setaccessibilitydecrementbutton%28_%29.md)
  Sets the decrement button for the stepper accessibility element.
- [func accessibilityPerformIncrement() -> Bool](./nsaccessibilityprotocol/accessibilityperformincrement%28%29.md)
  Increments the accessibility element’s value.
- [func accessibilityPerformDecrement() -> Bool](./nsaccessibilityprotocol/accessibilityperformdecrement%28%29.md)
  Decrements the accessibility element’s value.
- [func accessibilityPerformDelete() -> Bool](./nsaccessibilityprotocol/accessibilityperformdelete%28%29.md)
  Deletes the accessibility element’s value.
### Managing notifications
- [static func post(element: Any, notification: NSAccessibility.Notification)](./nsaccessibility-swift.struct/post%28element,notification%29.md)
  Sends a notification to any observing assistive apps.
- [static func post(element: Any, notification: NSAccessibility.Notification, userInfo: [NSAccessibility.NotificationUserInfoKey : Any]?)](./nsaccessibility-swift.struct/post%28element,notification,userinfo%29.md)
  Sends a notification and an optional user info dictionary to any observing assistive apps.
- [NSAccessibility.Notification](./nsaccessibility-swift.struct/notification.md)
  The name of the notification.
- [NSAccessibility.NotificationUserInfoKey](./nsaccessibility-swift.struct/notificationuserinfokey.md)
  The key in the user info dictionary for a notification.
### Handling errors
- [static let ErrorCodeExceptionInfo: String](./nsaccessibility-swift.struct/errorcodeexceptioninfo.md)
  An integer error code for debugging.
### Supporting types
- [struct NSAccessibility](./nsaccessibility-swift.struct.md)
  A namespace for accessibility symbols for AppKit apps.
### Instance methods
- [func accessibilityAttributedUserInputLabels() -> [NSAttributedString]?](./nsaccessibilityprotocol/accessibilityattributeduserinputlabels%28%29.md)
- [func accessibilityUserInputLabels() -> [String]?](./nsaccessibilityprotocol/accessibilityuserinputlabels%28%29.md)
- [func setAccessibilityAttributedUserInputLabels([NSAttributedString]?)](./nsaccessibilityprotocol/setaccessibilityattributeduserinputlabels%28_%29.md)
- [func setAccessibilityUserInputLabels([String]?)](./nsaccessibilityprotocol/setaccessibilityuserinputlabels%28_%29.md)
- [accessibilityAttributedUserInputLabels](./nsaccessibility-c.protocol/accessibilityattributeduserinputlabels.md)
- [accessibilityUserInputLabels](./nsaccessibility-c.protocol/accessibilityuserinputlabels.md)
### Instance Properties
- [accessibilityDecrementButton](./nsaccessibility-c.protocol/accessibilitydecrementbutton.md)
  The decrement button for the stepper accessibility element.
- [accessibilityIncrementButton](./nsaccessibility-c.protocol/accessibilityincrementbutton.md)
  The increment button for the stepper accessibility element.
- [accessibilityInsertionPointLineNumber](./nsaccessibility-c.protocol/accessibilityinsertionpointlinenumber.md)
  The line number that contains the insertion point.
- [accessibilityNumberOfCharacters](./nsaccessibility-c.protocol/accessibilitynumberofcharacters.md)
  The number of characters in the text.
- [accessibilityPlaceholderValue](./nsaccessibility-c.protocol/accessibilityplaceholdervalue.md)
  The placeholder value for the accessibility element.
- [accessibilitySelectedText](./nsaccessibility-c.protocol/accessibilityselectedtext.md)
  The currently selected text.
- [accessibilitySelectedTextRange](./nsaccessibility-c.protocol/accessibilityselectedtextrange.md)
  The range of the currently selected text.
- [accessibilitySelectedTextRanges](./nsaccessibility-c.protocol/accessibilityselectedtextranges.md)
  An array of ranges for the currently selected text.
- [accessibilitySharedCharacterRange](./nsaccessibility-c.protocol/accessibilitysharedcharacterrange.md)
  The range of characters that the accessibility element displays.
- [accessibilitySharedTextUIElements](./nsaccessibility-c.protocol/accessibilitysharedtextuielements.md)
  Other elements that share text with the accessibility element.
- [accessibilityVisibleCharacterRange](./nsaccessibility-c.protocol/accessibilityvisiblecharacterrange.md)
  The range of visible characters in the document.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [NSAccessibilityElement](./nsaccessibilityelement-swift.class.md)
- [NSActionCell](./nsactioncell.md)
- [NSApplication](./nsapplication.md)
- [NSBackgroundExtensionView](./nsbackgroundextensionview.md)
- [NSBox](./nsbox.md)
- [NSBrowser](./nsbrowser.md)
- [NSBrowserCell](./nsbrowsercell.md)
- [NSButton](./nsbutton.md)
- [NSButtonCell](./nsbuttoncell.md)
- [NSCell](./nscell.md)
- [NSClipView](./nsclipview.md)
- [NSCollectionView](./nscollectionview.md)
- [NSColorPanel](./nscolorpanel.md)
- [NSColorWell](./nscolorwell.md)
- [NSComboBox](./nscombobox.md)
- [NSComboBoxCell](./nscomboboxcell.md)
- [NSComboButton](./nscombobutton.md)
- [NSControl](./nscontrol.md)
- [NSDatePicker](./nsdatepicker.md)
- [NSDatePickerCell](./nsdatepickercell.md)
- [NSDrawer](./nsdrawer.md)
- [NSFontPanel](./nsfontpanel.md)
- [NSForm](./nsform.md)
- [NSFormCell](./nsformcell.md)
- [NSGlassEffectContainerView](./nsglasseffectcontainerview.md)
- [NSGlassEffectView](./nsglasseffectview.md)
- [NSGridView](./nsgridview.md)
- [NSImageCell](./nsimagecell.md)
- [NSImageView](./nsimageview.md)
- [NSLevelIndicator](./nslevelindicator.md)
- [NSLevelIndicatorCell](./nslevelindicatorcell.md)
- [NSMatrix](./nsmatrix.md)
- [NSMenu](./nsmenu.md)
- [NSMenuItem](./nsmenuitem.md)
- [NSMenuItemCell](./nsmenuitemcell.md)
- [NSOpenGLView](./nsopenglview.md)
- [NSOpenPanel](./nsopenpanel.md)
- [NSOutlineView](./nsoutlineview.md)
- [NSPanel](./nspanel.md)
- [NSPathCell](./nspathcell.md)
- [NSPathComponentCell](./nspathcomponentcell.md)
- [NSPathControl](./nspathcontrol.md)
- [NSPopUpButton](./nspopupbutton.md)
- [NSPopUpButtonCell](./nspopupbuttoncell.md)
- [NSPopover](./nspopover.md)
- [NSPredicateEditor](./nspredicateeditor.md)
- [NSProgressIndicator](./nsprogressindicator.md)
- [NSRuleEditor](./nsruleeditor.md)
- [NSRulerView](./nsrulerview.md)
- [NSSavePanel](./nssavepanel.md)
- [NSScrollView](./nsscrollview.md)
- [NSScroller](./nsscroller.md)
- [NSScrubber](./nsscrubber.md)
- [NSScrubberArrangedView](./nsscrubberarrangedview.md)
- [NSScrubberImageItemView](./nsscrubberimageitemview.md)
- [NSScrubberItemView](./nsscrubberitemview.md)
- [NSScrubberSelectionView](./nsscrubberselectionview.md)
- [NSScrubberTextItemView](./nsscrubbertextitemview.md)
- [NSSearchField](./nssearchfield.md)
- [NSSearchFieldCell](./nssearchfieldcell.md)
- [NSSecureTextField](./nssecuretextfield.md)
- [NSSecureTextFieldCell](./nssecuretextfieldcell.md)
- [NSSegmentedCell](./nssegmentedcell.md)
- [NSSegmentedControl](./nssegmentedcontrol.md)
- [NSSlider](./nsslider.md)
- [NSSliderAccessory](./nsslideraccessory.md)
- [NSSliderCell](./nsslidercell.md)
- [NSSplitView](./nssplitview.md)
- [NSStackView](./nsstackview.md)
- [NSStatusBarButton](./nsstatusbarbutton.md)
- [NSStepper](./nsstepper.md)
- [NSStepperCell](./nssteppercell.md)
- [NSSwitch](./nsswitch.md)
- [NSTabView](./nstabview.md)
- [NSTableCellView](./nstablecellview.md)
- [NSTableHeaderCell](./nstableheadercell.md)
- [NSTableHeaderView](./nstableheaderview.md)
- [NSTableRowView](./nstablerowview.md)
- [NSTableView](./nstableview.md)
- [NSText](./nstext.md)
- [NSTextAttachmentCell](./nstextattachmentcell-swift.class.md)
- [NSTextField](./nstextfield.md)
- [NSTextFieldCell](./nstextfieldcell.md)
- [NSTextInsertionIndicator](./nstextinsertionindicator.md)
- [NSTextView](./nstextview.md)
- [NSTokenField](./nstokenfield.md)
- [NSTokenFieldCell](./nstokenfieldcell.md)
- [NSView](./nsview.md)
- [NSVisualEffectView](./nsvisualeffectview.md)
- [NSWindow](./nswindow.md)

## See Also

### AppKit Elements
- [struct NSAccessibility](./nsaccessibility-swift.struct.md)
  A namespace for accessibility symbols for AppKit apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol)*