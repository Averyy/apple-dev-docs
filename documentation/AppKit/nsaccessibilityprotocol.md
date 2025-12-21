# NSAccessibilityProtocol

**Framework**: AppKit  
**Kind**: protocol

The complete list of properties and methods for accessible elements.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSAccessibilityProtocol : NSObjectProtocol
```

#### Overview

To be accessible, an app must provide information to the assistive app about its user interface and capabilities. There are three ways that apps and assistive apps interact:

- Informational properties. [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) defines a number of properties that provide information about your view or control. If you’re working with a subclass of a standard AppKit view or control, you can either set the desired property or override its getters and setters. By default, overriding only the getter tells the assistive app that it has read-only access to the property. Overriding the setter tells the assistive app that it also has write access to the property.
- Action methods. [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) also defines a number of methods that simulate button presses, mouse clicks, and selections in your view or control. By implementing these methods, you give assistive apps the ability to drive your view or control.
- Notifications. Your view or control may need to let the assistive app know when changes occur. [`NSAccessibility.Notification`](nsaccessibility-swift.struct/notification.md) defines a number of notifications that you can send using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) method. The role-specific protocols don’t include these notifications; however, standard AppKit controls already send appropriate messages for their standard usage patterns. You typically need to send your own notifications only when you’re creating a custom control or when you’re using a standard control in a nonstandard way.

If you’re using standard AppKit user interface elements, much of the work has been done for you. AppKit views and controls adopt the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol by default. In particular, [`NSView`](nsview.md), [`NSWindow`](nswindow.md), [`NSCell`](nscell.md), and [`NSDrawer`](nsdrawer.md) provide a default implementation for all the properties and methods in this protocol. In some cases, you may need to modify these default values to better represent your app, to provide additional context, or to modify the user’s flow through the app.

If you’re using custom view or control subclasses, you need to add the appropriate informational properties, action methods, and notifications. You do this by adopting a role-specific protocol instead of [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md). See [`Custom Controls`](custom-controls.md).

If you’re using custom user interface elements that don’t inherit from [`NSView`](nsview.md) or one of the other accessibility-enabled AppKit classes, subclass the [`NSAccessibilityElement`](nsaccessibilityelement-swift.class.md) class instead of adopting instead of [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md).

##### Customizing User Interface Elements

Often, you can adjust how an assistive app interacts with your user interface element without creating a custom subclass. If a user interface element inherits from [`NSView`](nsview.md) or one of the other accessibility-enabled AppKit classes, you can customize it by:

- Setting its accessibility values using any of the setter methods in the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol.
- Overriding any of the properties or methods in the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol with a custom implementation.

If you override a getter method, the system lets assistive apps call your getter. This can be particularly useful when managing dynamic properties because you can calculate their current value on demand instead of trying to update the property in response to a change.

If you override a setter method, the system lets assistive apps both read and modify that property.

You can control which accessor methods the assistive app can use by overriding [`isAccessibilitySelectorAllowed(_:)`](nsaccessibilityprotocol/isaccessibilityselectorallowed(_:).md). Return [`true`](https://developer.apple.com/documentation/Swift/true) if the assistive app can call the selector; otherwise, return [`false`](https://developer.apple.com/documentation/Swift/false).

## Topics

### Configuring accessibility
- [func isAccessibilityElement() -> Bool](nsaccessibilityprotocol/isaccessibilityelement.md)
  Returns a Boolean value that determines whether the accessibility element participates in the accessibility hierarchy.
- [func setAccessibilityElement(Bool)](nsaccessibilityprotocol/setaccessibilityelement(_:).md)
  Sets a Boolean value that determines whether the accessibility element participates in the accessibility hierarchy.
- [func isAccessibilityEnabled() -> Bool](nsaccessibilityprotocol/isaccessibilityenabled.md)
  Returns a Boolean value that determines whether the accessibility element responds to user events.
- [func setAccessibilityEnabled(Bool)](nsaccessibilityprotocol/setaccessibilityenabled(_:).md)
  Sets a Boolean value that determines whether the accessibility element responds to user events.
- [func accessibilityFrame() -> NSRect](nsaccessibilityprotocol/accessibilityframe.md)
  Returns the accessibility element’s frame in screen coordinates.
- [func setAccessibilityFrame(NSRect)](nsaccessibilityprotocol/setaccessibilityframe(_:).md)
  Sets the accessibility element’s frame in screen coordinates.
- [func accessibilityHelp() -> String?](nsaccessibilityprotocol/accessibilityhelp.md)
  Returns the help text for the accessibility element.
- [func setAccessibilityHelp(String?)](nsaccessibilityprotocol/setaccessibilityhelp(_:).md)
  Sets the help text for the accessibility element.
- [func accessibilityLabel() -> String?](nsaccessibilityprotocol/accessibilitylabel.md)
  Returns a short description of the accessibility element.
- [func setAccessibilityLabel(String?)](nsaccessibilityprotocol/setaccessibilitylabel(_:).md)
  Sets a short description of the accessibility element.
- [func accessibilityTitle() -> String?](nsaccessibilityprotocol/accessibilitytitle.md)
  Returns the title of the accessibility element—for example, a button’s visible text.
- [func setAccessibilityTitle(String?)](nsaccessibilityprotocol/setaccessibilitytitle(_:).md)
  Sets the title of the accessibility element.
- [func accessibilityValue() -> Any?](nsaccessibilityprotocol/accessibilityvalue.md)
  Returns the accessibility element’s value.
- [func setAccessibilityValue(Any?)](nsaccessibilityprotocol/setaccessibilityvalue(_:).md)
  Sets the accessibility element’s value.
- [func isAccessibilitySelectorAllowed(Selector) -> Bool](nsaccessibilityprotocol/isaccessibilityselectorallowed(_:).md)
  Returns a Boolean value that indicates whether assistive apps can invoke the specified selector on the accessibility element.
### Setting content and values
- [func accessibilityContents() -> [Any]?](nsaccessibilityprotocol/accessibilitycontents.md)
  Returns the contents of the current accessibility element.
- [func setAccessibilityContents([Any]?)](nsaccessibilityprotocol/setaccessibilitycontents(_:).md)
  Sets the contents of the current accessibility element.
- [func accessibilityCriticalValue() -> Any?](nsaccessibilityprotocol/accessibilitycriticalvalue.md)
  Returns the critical value for the level indicator.
- [func setAccessibilityCriticalValue(Any?)](nsaccessibilityprotocol/setaccessibilitycriticalvalue(_:).md)
  Sets the critical value for the level indicator.
- [func accessibilityIdentifier() -> String?](nsaccessibilityprotocol/accessibilityidentifier.md)
  Returns the accessibility element’s identity.
- [func setAccessibilityIdentifier(String?)](nsaccessibilityprotocol/setaccessibilityidentifier(_:).md)
  Sets the accessibility element’s identity.
- [func accessibilityMaxValue() -> Any?](nsaccessibilityprotocol/accessibilitymaxvalue.md)
  Returns the maximum value for the accessibility element.
- [func setAccessibilityMaxValue(Any?)](nsaccessibilityprotocol/setaccessibilitymaxvalue(_:).md)
  Sets the maximum value for the accessibility element.
- [func accessibilityMinValue() -> Any?](nsaccessibilityprotocol/accessibilityminvalue.md)
  Returns the minimum value for the accessibility element.
- [func setAccessibilityMinValue(Any?)](nsaccessibilityprotocol/setaccessibilityminvalue(_:).md)
  Sets the minimum value for the accessibility element.
- [func accessibilityOrientation() -> NSAccessibilityOrientation](nsaccessibilityprotocol/accessibilityorientation.md)
  Returns the orientation of the accessibility element.
- [func setAccessibilityOrientation(NSAccessibilityOrientation)](nsaccessibilityprotocol/setaccessibilityorientation(_:).md)
  Sets the orientation of the accessibility element.
- [func isAccessibilityProtectedContent() -> Bool](nsaccessibilityprotocol/isaccessibilityprotectedcontent.md)
  Returns a Boolean value that determines whether the accessibility element contains protected content.
- [func setAccessibilityProtectedContent(Bool)](nsaccessibilityprotocol/setaccessibilityprotectedcontent(_:).md)
  Sets a Boolean value that determines whether the accessibility element contains protected content.
- [func isAccessibilitySelected() -> Bool](nsaccessibilityprotocol/isaccessibilityselected.md)
  Returns a Boolean value that determines whether the accessibility element is currently in a selected state.
- [func setAccessibilitySelected(Bool)](nsaccessibilityprotocol/setaccessibilityselected(_:).md)
  Sets a Boolean value that determines whether the accessibility element is currently in a selected state.
- [func accessibilityURL() -> URL?](nsaccessibilityprotocol/accessibilityurl.md)
  Returns the URL for the accessibility element.
- [func setAccessibilityURL(URL?)](nsaccessibilityprotocol/setaccessibilityurl(_:).md)
  Sets the URL for the accessibility element.
- [func accessibilityValueDescription() -> String?](nsaccessibilityprotocol/accessibilityvaluedescription.md)
  Returns the human-readable description of the accessibility element’s value.
- [func setAccessibilityValueDescription(String?)](nsaccessibilityprotocol/setaccessibilityvaluedescription(_:).md)
  Sets the human-readable description of the accessibility element’s value.
- [func accessibilityWarningValue() -> Any?](nsaccessibilityprotocol/accessibilitywarningvalue.md)
  Returns the warning value for the level indicator.
- [func setAccessibilityWarningValue(Any?)](nsaccessibilityprotocol/setaccessibilitywarningvalue(_:).md)
  Sets the warning value for the level indicator.
- [enum NSAccessibilityOrientation](nsaccessibilityorientation.md)
  Values that indicate the orientation of accessibility elements, such as scroll bars and split views.
### Determining relationships
- [func accessibilityChildren() -> [Any]?](nsaccessibilityprotocol/accessibilitychildren.md)
  Returns the child accessibility elements in the accessibility hierarchy.
- [func setAccessibilityChildren([Any]?)](nsaccessibilityprotocol/setaccessibilitychildren(_:).md)
  Sets the child accessibility elements in the accessibility hierarchy.
- [func accessibilityChildrenInNavigationOrder() -> [any NSAccessibilityElementProtocol]?](nsaccessibilityprotocol/accessibilitychildreninnavigationorder.md)
  Returns the array of child accessibility elements in order for linear navigation.
- [func setAccessibilityChildrenInNavigationOrder([any NSAccessibilityElementProtocol]?)](nsaccessibilityprotocol/setaccessibilitychildreninnavigationorder(_:).md)
  Sets the array of child accessibility elements in order for linear navigation.
- [func accessibilityParent() -> Any?](nsaccessibilityprotocol/accessibilityparent.md)
  Returns the accessibility element’s parent in the accessibility hierarchy.
- [func setAccessibilityParent(Any?)](nsaccessibilityprotocol/setaccessibilityparent(_:).md)
  Sets the accessibility element’s parent in the accessibility hierarchy.
- [func accessibilitySelectedChildren() -> [Any]?](nsaccessibilityprotocol/accessibilityselectedchildren.md)
  Returns the accessibility element’s currently selected children.
- [func setAccessibilitySelectedChildren([Any]?)](nsaccessibilityprotocol/setaccessibilityselectedchildren(_:).md)
  Sets the accessibility element’s currently selected children.
- [func accessibilityTopLevelUIElement() -> Any?](nsaccessibilityprotocol/accessibilitytopleveluielement.md)
  Returns the top-level element that contains the accessibility element.
- [func setAccessibilityTopLevelUIElement(Any?)](nsaccessibilityprotocol/setaccessibilitytopleveluielement(_:).md)
  Sets the top-level element that contains the accessibility element.
- [func accessibilityVisibleChildren() -> [Any]?](nsaccessibilityprotocol/accessibilityvisiblechildren.md)
  Returns the accessibility element’s visible child accessibility elements.
- [func setAccessibilityVisibleChildren([Any]?)](nsaccessibilityprotocol/setaccessibilityvisiblechildren(_:).md)
  Sets the accessibility element’s visible child accessibility elements.
### Setting the focus
- [func accessibilityApplicationFocusedUIElement() -> Any?](nsaccessibilityprotocol/accessibilityapplicationfocuseduielement.md)
  Returns the child accessibility element with the current focus.
- [func setAccessibilityApplicationFocusedUIElement(Any?)](nsaccessibilityprotocol/setaccessibilityapplicationfocuseduielement(_:).md)
  Sets the child accessibility element with the current focus.
- [func isAccessibilityFocused() -> Bool](nsaccessibilityprotocol/isaccessibilityfocused.md)
  Returns a Boolean value that determines whether the accessibility element has the keyboard focus.
- [func setAccessibilityFocused(Bool)](nsaccessibilityprotocol/setaccessibilityfocused(_:).md)
  Sets a Boolean value that determines whether the accessibility element has the keyboard focus.
- [func accessibilityFocusedWindow() -> Any?](nsaccessibilityprotocol/accessibilityfocusedwindow.md)
  Returns the child window with the current focus.
- [func setAccessibilityFocusedWindow(Any?)](nsaccessibilityprotocol/setaccessibilityfocusedwindow(_:).md)
  Sets the child window with the current focus.
- [func accessibilitySharedFocusElements() -> [Any]?](nsaccessibilityprotocol/accessibilitysharedfocuselements.md)
  Returns the array of elements that shares the keyboard focus with the accessibility element.
- [func setAccessibilitySharedFocusElements([Any]?)](nsaccessibilityprotocol/setaccessibilitysharedfocuselements(_:).md)
  Sets the array of elements that shares the keyboard focus with the accessibility element.
### Assigning roles
- [func isAccessibilityRequired() -> Bool](nsaccessibilityprotocol/isaccessibilityrequired.md)
  Returns a Boolean value that determines whether the accessibility element must have content for successful submission of a form.
- [func setAccessibilityRequired(Bool)](nsaccessibilityprotocol/setaccessibilityrequired(_:).md)
  Sets a Boolean value that determines whether the accessibility element must have content for successful submission of a form.
- [func accessibilityRole() -> NSAccessibility.Role?](nsaccessibilityprotocol/accessibilityrole.md)
  Returns the type of interface element that the accessibility element represents.
- [func setAccessibilityRole(NSAccessibility.Role?)](nsaccessibilityprotocol/setaccessibilityrole(_:).md)
  Sets the type of interface element that the accessibility element represents.
- [func accessibilityRoleDescription() -> String?](nsaccessibilityprotocol/accessibilityroledescription.md)
  Returns a localized, human-intelligible description of the accessibility element’s role, such as .
- [func setAccessibilityRoleDescription(String?)](nsaccessibilityprotocol/setaccessibilityroledescription(_:).md)
  Sets the localized, human-intelligible description of the accessibility element’s role, such as .
- [func accessibilitySubrole() -> NSAccessibility.Subrole?](nsaccessibilityprotocol/accessibilitysubrole.md)
  Returns the specialized interface element type that the accessibility element represents.
- [func setAccessibilitySubrole(NSAccessibility.Subrole?)](nsaccessibilityprotocol/setaccessibilitysubrole(_:).md)
  Sets the specialized interface element type that the accessibility element represents.
- [NSAccessibility.Role](nsaccessibility-swift.struct/role.md)
  Values that describe types of objects that accessibility elements represent.
- [NSAccessibility.Subrole](nsaccessibility-swift.struct/subrole.md)
  Values that describe specialized object subtypes that accessibility elements represent.
### Assigning actions
- [func accessibilityCustomActions() -> [NSAccessibilityCustomAction]?](nsaccessibilityprotocol/accessibilitycustomactions.md)
  Returns the custom actions of the current accessibility element.
- [func setAccessibilityCustomActions([NSAccessibilityCustomAction]?)](nsaccessibilityprotocol/setaccessibilitycustomactions(_:).md)
  Sets the custom actions of the current accessibility element.
- [class NSAccessibilityCustomAction](nsaccessibilitycustomaction.md)
  A custom action to perform on an accessible object.
### Assigning rotors
- [func accessibilityCustomRotors() -> [NSAccessibilityCustomRotor]](nsaccessibilityprotocol/accessibilitycustomrotors.md)
  Returns the custom rotors of the current accessibility element.
- [func setAccessibilityCustomRotors([NSAccessibilityCustomRotor])](nsaccessibilityprotocol/setaccessibilitycustomrotors(_:).md)
  Sets the custom rotors of the current accessibility element.
- [class NSAccessibilityCustomRotor](nsaccessibilitycustomrotor.md)
  A context-sensitive function that helps VoiceOver users find the next instance of a related accessibility element.
### Configuring text elements
- [func accessibilityInsertionPointLineNumber() -> Int](nsaccessibilityprotocol/accessibilityinsertionpointlinenumber.md)
  Returns the line number that contains the insertion point.
- [func setAccessibilityInsertionPointLineNumber(Int)](nsaccessibilityprotocol/setaccessibilityinsertionpointlinenumber(_:).md)
  Sets the line number that contains the insertion point.
- [func accessibilityNumberOfCharacters() -> Int](nsaccessibilityprotocol/accessibilitynumberofcharacters.md)
  Returns the number of characters in the text.
- [func setAccessibilityNumberOfCharacters(Int)](nsaccessibilityprotocol/setaccessibilitynumberofcharacters(_:).md)
  Sets the number of characters in the text.
- [func accessibilityPlaceholderValue() -> String?](nsaccessibilityprotocol/accessibilityplaceholdervalue.md)
  Returns the placeholder value for the accessibility element.
- [func setAccessibilityPlaceholderValue(String?)](nsaccessibilityprotocol/setaccessibilityplaceholdervalue(_:).md)
  Sets the placeholder value for the accessibility element.
- [func accessibilitySelectedText() -> String?](nsaccessibilityprotocol/accessibilityselectedtext.md)
  Returns the currently selected text.
- [func setAccessibilitySelectedText(String?)](nsaccessibilityprotocol/setaccessibilityselectedtext(_:).md)
  Sets the currently selected text.
- [func accessibilitySelectedTextRange() -> NSRange](nsaccessibilityprotocol/accessibilityselectedtextrange.md)
  Returns the range of the currently selected text.
- [func setAccessibilitySelectedTextRange(NSRange)](nsaccessibilityprotocol/setaccessibilityselectedtextrange(_:).md)
  Sets the range of the currently selected text.
- [func accessibilitySelectedTextRanges() -> [NSValue]?](nsaccessibilityprotocol/accessibilityselectedtextranges.md)
  Returns an array of ranges for the currently selected text.
- [func setAccessibilitySelectedTextRanges([NSValue]?)](nsaccessibilityprotocol/setaccessibilityselectedtextranges(_:).md)
  Sets an array of ranges for the currently selected text.
- [func accessibilitySharedCharacterRange() -> NSRange](nsaccessibilityprotocol/accessibilitysharedcharacterrange.md)
  Returns the range of characters that the accessibility element displays.
- [func setAccessibilitySharedCharacterRange(NSRange)](nsaccessibilityprotocol/setaccessibilitysharedcharacterrange(_:).md)
  Sets the range of characters that the accessibility element displays.
- [func accessibilitySharedTextUIElements() -> [Any]?](nsaccessibilityprotocol/accessibilitysharedtextuielements.md)
  Returns the other elements that share text with the accessibility element.
- [func setAccessibilitySharedTextUIElements([Any]?)](nsaccessibilityprotocol/setaccessibilitysharedtextuielements(_:).md)
  Sets the other elements that share text with the accessibility element.
- [func accessibilityVisibleCharacterRange() -> NSRange](nsaccessibilityprotocol/accessibilityvisiblecharacterrange.md)
  Returns the range of visible characters in the document.
- [func setAccessibilityVisibleCharacterRange(NSRange)](nsaccessibilityprotocol/setaccessibilityvisiblecharacterrange(_:).md)
  Sets the range of visible characters in the document.
- [func accessibilityString(for: NSRange) -> String?](nsaccessibilityprotocol/accessibilitystring(for:).md)
  Returns the substring for the specified range.
- [func accessibilityAttributedString(for: NSRange) -> NSAttributedString?](nsaccessibilityprotocol/accessibilityattributedstring(for:).md)
  Returns the attributed substring for the specified range of characters.
- [func accessibilityRTF(for: NSRange) -> Data?](nsaccessibilityprotocol/accessibilityrtf(for:).md)
  Returns the rich text format (RTF) data that describes the specified range of characters.
- [func accessibilityFrame(for: NSRange) -> NSRect](nsaccessibilityprotocol/accessibilityframe(for:).md)
  Returns the rectangle that encloses the specified range of characters.
- [func accessibilityLine(for: Int) -> Int](nsaccessibilityprotocol/accessibilityline(for:).md)
  Returns the line number for the line that contains the specified character index.
- [func accessibilityRange(for: Int) -> NSRange](nsaccessibilityprotocol/accessibilityrange(for:)-6kv3.md)
  Returns the range of characters for the glyph that includes the specified character.
- [func accessibilityStyleRange(for: Int) -> NSRange](nsaccessibilityprotocol/accessibilitystylerange(for:).md)
  Returns a range of characters that all have the same style as the specified character.
- [func accessibilityRange(forLine: Int) -> NSRange](nsaccessibilityprotocol/accessibilityrange(forline:).md)
  Returns the range of characters in the specified line.
- [func accessibilityRange(for: NSPoint) -> NSRange](nsaccessibilityprotocol/accessibilityrange(for:)-1iudm.md)
  Returns the range of characters for the glyph at the specified point.
### Configuring windows
- [func accessibilityActivationPoint() -> NSPoint](nsaccessibilityprotocol/accessibilityactivationpoint.md)
  Returns the activation point for the user interface element.
- [func setAccessibilityActivationPoint(NSPoint)](nsaccessibilityprotocol/setaccessibilityactivationpoint(_:).md)
  Sets the activation point for the user interface element.
- [func isAccessibilityAlternateUIVisible() -> Bool](nsaccessibilityprotocol/isaccessibilityalternateuivisible.md)
  Returns the Boolean value that determines whether the accessibility element’s alternative UI is currently visible.
- [func setAccessibilityAlternateUIVisible(Bool)](nsaccessibilityprotocol/setaccessibilityalternateuivisible(_:).md)
  Sets the Boolean value that determines whether the accessibility element’s alternative UI is currently visible.
- [func accessibilityCancelButton() -> Any?](nsaccessibilityprotocol/accessibilitycancelbutton.md)
  Returns the child accessibility element that represents the window’s cancel button.
- [func setAccessibilityCancelButton(Any?)](nsaccessibilityprotocol/setaccessibilitycancelbutton(_:).md)
  Sets the child accessibility element that represents the window’s cancel button.
- [func accessibilityCloseButton() -> Any?](nsaccessibilityprotocol/accessibilityclosebutton.md)
  Returns the child accessibility element that represents the window’s close button.
- [func setAccessibilityCloseButton(Any?)](nsaccessibilityprotocol/setaccessibilityclosebutton(_:).md)
  Sets the child accessibility element that represents the window’s close button.
- [func accessibilityDefaultButton() -> Any?](nsaccessibilityprotocol/accessibilitydefaultbutton.md)
  Returns the child accessibility element that represents the window’s default button.
- [func setAccessibilityDefaultButton(Any?)](nsaccessibilityprotocol/setaccessibilitydefaultbutton(_:).md)
  Sets the child accessibility element that represents the window’s default button.
- [func accessibilityFullScreenButton() -> Any?](nsaccessibilityprotocol/accessibilityfullscreenbutton.md)
  Returns the child accessibility element that represents the window’s full-screen button.
- [func setAccessibilityFullScreenButton(Any?)](nsaccessibilityprotocol/setaccessibilityfullscreenbutton(_:).md)
  Sets the child accessibility element that represents the window’s full-screen button.
- [func accessibilityGrowArea() -> Any?](nsaccessibilityprotocol/accessibilitygrowarea.md)
  Returns the child accessibility element that represents the window’s grow area.
- [func setAccessibilityGrowArea(Any?)](nsaccessibilityprotocol/setaccessibilitygrowarea(_:).md)
  Sets the child accessibility element that represents the window’s grow area.
- [func isAccessibilityMain() -> Bool](nsaccessibilityprotocol/isaccessibilitymain.md)
  Returns a Boolean value that determines whether the window is the app’s main window.
- [func setAccessibilityMain(Bool)](nsaccessibilityprotocol/setaccessibilitymain(_:).md)
  Sets a Boolean value that determines whether the window is the app’s main window.
- [func accessibilityMinimizeButton() -> Any?](nsaccessibilityprotocol/accessibilityminimizebutton.md)
  Returns the child accessibility element that represents the window’s minimize button.
- [func setAccessibilityMinimizeButton(Any?)](nsaccessibilityprotocol/setaccessibilityminimizebutton(_:).md)
  Sets the child accessibility element that represents the window’s minimize button.
- [func isAccessibilityMinimized() -> Bool](nsaccessibilityprotocol/isaccessibilityminimized.md)
  Returns the Boolean value that determines whether the window is in a minimized state.
- [func setAccessibilityMinimized(Bool)](nsaccessibilityprotocol/setaccessibilityminimized(_:).md)
  Sets the Boolean value that determines whether the window is in a minimized state.
- [func isAccessibilityModal() -> Bool](nsaccessibilityprotocol/isaccessibilitymodal.md)
  Returns a Boolean value that determines whether the window is modal.
- [func setAccessibilityModal(Bool)](nsaccessibilityprotocol/setaccessibilitymodal(_:).md)
  Sets a Boolean value that determines whether the window is modal.
- [func accessibilityProxy() -> Any?](nsaccessibilityprotocol/accessibilityproxy.md)
  Returns the child accessibility element that represents the window’s proxy icon.
- [func setAccessibilityProxy(Any?)](nsaccessibilityprotocol/setaccessibilityproxy(_:).md)
  Sets the child accessibility element that represents the window’s proxy icon.
- [func accessibilityShownMenu() -> Any?](nsaccessibilityprotocol/accessibilityshownmenu.md)
  Returns the menu currently displaying for the accessibility element.
- [func setAccessibilityShownMenu(Any?)](nsaccessibilityprotocol/setaccessibilityshownmenu(_:).md)
  Sets the menu currently displaying for the accessibility element.
- [func accessibilityToolbarButton() -> Any?](nsaccessibilityprotocol/accessibilitytoolbarbutton.md)
  Returns the child accessibility element that represents the window’s toolbar button.
- [func setAccessibilityToolbarButton(Any?)](nsaccessibilityprotocol/setaccessibilitytoolbarbutton(_:).md)
  Sets the child accessibility element that represents the window’s toolbar button.
- [func accessibilityWindow() -> Any?](nsaccessibilityprotocol/accessibilitywindow.md)
  Returns the window that contains the accessibility element.
- [func setAccessibilityWindow(Any?)](nsaccessibilityprotocol/setaccessibilitywindow(_:).md)
  Sets the window that contains the accessibility element.
- [func accessibilityZoomButton() -> Any?](nsaccessibilityprotocol/accessibilityzoombutton.md)
  Returns the child accessibility element that represents the window’s zoom button.
- [func setAccessibilityZoomButton(Any?)](nsaccessibilityprotocol/setaccessibilityzoombutton(_:).md)
  Sets the child accessibility element that represents the window’s zoom button.
### Managing apps
- [func accessibilityExtrasMenuBar() -> Any?](nsaccessibilityprotocol/accessibilityextrasmenubar.md)
  Returns the icon for the app’s menu bar extra.
- [func setAccessibilityExtrasMenuBar(Any?)](nsaccessibilityprotocol/setaccessibilityextrasmenubar(_:).md)
  Sets the icon for the app’s menu bar extra.
- [func isAccessibilityFrontmost() -> Bool](nsaccessibilityprotocol/isaccessibilityfrontmost.md)
  Returns a Boolean value that determines whether the app is the frontmost app.
- [func setAccessibilityFrontmost(Bool)](nsaccessibilityprotocol/setaccessibilityfrontmost(_:).md)
  Sets a Boolean value that determines whether the app is the frontmost app.
- [func isAccessibilityHidden() -> Bool](nsaccessibilityprotocol/isaccessibilityhidden.md)
  Returns a Boolean value that determines whether the app is in a hidden state.
- [func setAccessibilityHidden(Bool)](nsaccessibilityprotocol/setaccessibilityhidden(_:).md)
  Sets a Boolean value that determines whether the app is in a hidden state.
- [func accessibilityMainWindow() -> Any?](nsaccessibilityprotocol/accessibilitymainwindow.md)
  Returns the app’s main window.
- [func setAccessibilityMainWindow(Any?)](nsaccessibilityprotocol/setaccessibilitymainwindow(_:).md)
  Sets the app’s main window.
- [func accessibilityMenuBar() -> Any?](nsaccessibilityprotocol/accessibilitymenubar.md)
  Returns the app’s menu bar.
- [func setAccessibilityMenuBar(Any?)](nsaccessibilityprotocol/setaccessibilitymenubar(_:).md)
  Sets the app’s menu bar.
- [func accessibilityWindows() -> [Any]?](nsaccessibilityprotocol/accessibilitywindows.md)
  Returns an array that contains all the app’s windows.
- [func setAccessibilityWindows([Any]?)](nsaccessibilityprotocol/setaccessibilitywindows(_:).md)
  Sets the array that contains all the app’s windows.
### Configuring grid views
- [func accessibilityColumnCount() -> Int](nsaccessibilityprotocol/accessibilitycolumncount.md)
  Returns the number of columns in the accessibility element’s grid.
- [func setAccessibilityColumnCount(Int)](nsaccessibilityprotocol/setaccessibilitycolumncount(_:).md)
  Sets the number of columns in the accessibility element’s grid.
- [func isAccessibilityOrderedByRow() -> Bool](nsaccessibilityprotocol/isaccessibilityorderedbyrow.md)
  Returns a Boolean value that determines whether the accessibility element’s grid is in row major order or in column major order.
- [func setAccessibilityOrderedByRow(Bool)](nsaccessibilityprotocol/setaccessibilityorderedbyrow(_:).md)
  Sets a Boolean value that determines whether the element’s grid is in row major order or in column major order.
- [func accessibilityRowCount() -> Int](nsaccessibilityprotocol/accessibilityrowcount.md)
  Returns the number of rows in the accessibility element’s grid.
- [func setAccessibilityRowCount(Int)](nsaccessibilityprotocol/setaccessibilityrowcount(_:).md)
  Sets the number of rows in the accessibility element’s grid.
### Configuring scroll views
- [func accessibilityHorizontalScrollBar() -> Any?](nsaccessibilityprotocol/accessibilityhorizontalscrollbar.md)
  Returns the horizontal scroll bar for the scroll view.
- [func setAccessibilityHorizontalScrollBar(Any?)](nsaccessibilityprotocol/setaccessibilityhorizontalscrollbar(_:).md)
  Sets the horizontal scroll bar for the scroll view.
- [func accessibilityVerticalScrollBar() -> Any?](nsaccessibilityprotocol/accessibilityverticalscrollbar.md)
  Returns the vertical scroll bar for the scroll view.
- [func setAccessibilityVerticalScrollBar(Any?)](nsaccessibilityprotocol/setaccessibilityverticalscrollbar(_:).md)
  Sets the vertical scroll bar for the scroll view.
### Configuring table and outline views
- [func accessibilityColumnHeaderUIElements() -> [Any]?](nsaccessibilityprotocol/accessibilitycolumnheaderuielements.md)
  Returns the column header accessibility elements for the table or outline.
- [func setAccessibilityColumnHeaderUIElements([Any]?)](nsaccessibilityprotocol/setaccessibilitycolumnheaderuielements(_:).md)
  Sets the column header accessibility elements for the table or outline.
- [func accessibilityColumns() -> [Any]?](nsaccessibilityprotocol/accessibilitycolumns.md)
  Returns the column accessibility elements for the table or outline.
- [func setAccessibilityColumns([Any]?)](nsaccessibilityprotocol/setaccessibilitycolumns(_:).md)
  Sets the column accessibility elements for the table or outline.
- [func accessibilityColumnTitles() -> [Any]?](nsaccessibilityprotocol/accessibilitycolumntitles.md)
  Returns the column titles for the accessibility element.
- [func setAccessibilityColumnTitles([Any]?)](nsaccessibilityprotocol/setaccessibilitycolumntitles(_:).md)
  Sets the column titles for the accessibility element.
- [func isAccessibilityExpanded() -> Bool](nsaccessibilityprotocol/isaccessibilityexpanded.md)
  Returns a Boolean value that determines whether the accessibility element is in an expanded state.
- [func setAccessibilityExpanded(Bool)](nsaccessibilityprotocol/setaccessibilityexpanded(_:).md)
  Sets a Boolean value that determines whether accessibility element is in an expanded state.
- [func accessibilityHeader() -> Any?](nsaccessibilityprotocol/accessibilityheader.md)
  Returns the header for the table view.
- [func setAccessibilityHeader(Any?)](nsaccessibilityprotocol/setaccessibilityheader(_:).md)
  Sets the header for the table view.
- [func accessibilityIndex() -> Int](nsaccessibilityprotocol/accessibilityindex.md)
  Returns the index of the row or column that the accessibility element represents.
- [func setAccessibilityIndex(Int)](nsaccessibilityprotocol/setaccessibilityindex(_:).md)
  Sets the index of the row or column that the accessibility element represents.
- [func accessibilityRowHeaderUIElements() -> [Any]?](nsaccessibilityprotocol/accessibilityrowheaderuielements.md)
  Returns the row header accessibility elements for the table or outline.
- [func setAccessibilityRowHeaderUIElements([Any]?)](nsaccessibilityprotocol/setaccessibilityrowheaderuielements(_:).md)
  Sets the row header accessibility elements for the table or outline.
- [func accessibilityRows() -> [Any]?](nsaccessibilityprotocol/accessibilityrows.md)
  Returns the row accessibility elements for the table or outline.
- [func setAccessibilityRows([Any]?)](nsaccessibilityprotocol/setaccessibilityrows(_:).md)
  Sets the row accessibility elements for the table or outline.
- [func accessibilitySelectedColumns() -> [Any]?](nsaccessibilityprotocol/accessibilityselectedcolumns.md)
  Returns the currently selected columns for the table or outline.
- [func setAccessibilitySelectedColumns([Any]?)](nsaccessibilityprotocol/setaccessibilityselectedcolumns(_:).md)
  Sets the currently selected columns for the table or outline.
- [func accessibilitySelectedRows() -> [Any]?](nsaccessibilityprotocol/accessibilityselectedrows.md)
  Returns the currently selected rows for the table or outline.
- [func setAccessibilitySelectedRows([Any]?)](nsaccessibilityprotocol/setaccessibilityselectedrows(_:).md)
  Sets the currently selected rows for the table or outline.
- [func accessibilitySortDirection() -> NSAccessibilitySortDirection](nsaccessibilityprotocol/accessibilitysortdirection.md)
  Returns the accessibility element’s sort direction.
- [func setAccessibilitySortDirection(NSAccessibilitySortDirection)](nsaccessibilityprotocol/setaccessibilitysortdirection(_:).md)
  Sets the accessibility element’s sort direction.
- [func accessibilityVisibleColumns() -> [Any]?](nsaccessibilityprotocol/accessibilityvisiblecolumns.md)
  Returns the visible columns for the table or outline.
- [func setAccessibilityVisibleColumns([Any]?)](nsaccessibilityprotocol/setaccessibilityvisiblecolumns(_:).md)
  Sets the visible columns for the table or outline.
- [func accessibilityVisibleRows() -> [Any]?](nsaccessibilityprotocol/accessibilityvisiblerows.md)
  Returns the visible rows for the table or outline.
- [func setAccessibilityVisibleRows([Any]?)](nsaccessibilityprotocol/setaccessibilityvisiblerows(_:).md)
  Sets the visible rows for the table or outline.
- [enum NSAccessibilitySortDirection](nsaccessibilitysortdirection.md)
  Values that indicate the sort direction of a column.
### Configuring outline rows
- [func isAccessibilityDisclosed() -> Bool](nsaccessibilityprotocol/isaccessibilitydisclosed.md)
  Returns a Boolean value that determines whether the row is disclosing other rows.
- [func setAccessibilityDisclosed(Bool)](nsaccessibilityprotocol/setaccessibilitydisclosed(_:).md)
  Sets a Boolean value that determines whether the row is disclosing other rows.
- [func accessibilityDisclosedByRow() -> Any?](nsaccessibilityprotocol/accessibilitydisclosedbyrow.md)
  Returns the row disclosing the current row.
- [func setAccessibilityDisclosedByRow(Any?)](nsaccessibilityprotocol/setaccessibilitydisclosedbyrow(_:).md)
  Sets the row disclosing the current row.
- [func accessibilityDisclosedRows() -> Any?](nsaccessibilityprotocol/accessibilitydisclosedrows.md)
  Returns the rows that the current row discloses.
- [func setAccessibilityDisclosedRows(Any?)](nsaccessibilityprotocol/setaccessibilitydisclosedrows(_:).md)
  Sets the rows that the current row discloses.
- [func accessibilityDisclosureLevel() -> Int](nsaccessibilityprotocol/accessibilitydisclosurelevel.md)
  Returns the indention level for the row.
- [func setAccessibilityDisclosureLevel(Int)](nsaccessibilityprotocol/setaccessibilitydisclosurelevel(_:).md)
  Sets the indention level for the row.
### Configuring cell-based tables
- [func accessibilityColumnIndexRange() -> NSRange](nsaccessibilityprotocol/accessibilitycolumnindexrange.md)
  Returns the column index range of the cell.
- [func setAccessibilityColumnIndexRange(NSRange)](nsaccessibilityprotocol/setaccessibilitycolumnindexrange(_:).md)
  Sets the column index range of the cell.
- [func accessibilityRowIndexRange() -> NSRange](nsaccessibilityprotocol/accessibilityrowindexrange.md)
  Returns the row index range of the cell.
- [func setAccessibilityRowIndexRange(NSRange)](nsaccessibilityprotocol/setaccessibilityrowindexrange(_:).md)
  Sets the row index range of the cell.
- [func accessibilitySelectedCells() -> [Any]?](nsaccessibilityprotocol/accessibilityselectedcells.md)
  Returns the currently selected cells for the table.
- [func setAccessibilitySelectedCells([Any]?)](nsaccessibilityprotocol/setaccessibilityselectedcells(_:).md)
  Sets the currently selected cells for the table.
- [func accessibilityVisibleCells() -> [Any]?](nsaccessibilityprotocol/accessibilityvisiblecells.md)
  Returns the visible cells for the table.
- [func setAccessibilityVisibleCells([Any]?)](nsaccessibilityprotocol/setaccessibilityvisiblecells(_:).md)
  Sets the visible cells for the table.
- [func accessibilityCell(forColumn: Int, row: Int) -> Any?](nsaccessibilityprotocol/accessibilitycell(forcolumn:row:).md)
  Returns the cell at the specified column and row.
### Configuring layout
- [func accessibilityHandles() -> [Any]?](nsaccessibilityprotocol/accessibilityhandles.md)
  Returns the drag handle elements for the layout item element.
- [func setAccessibilityHandles([Any]?)](nsaccessibilityprotocol/setaccessibilityhandles(_:).md)
  Sets the drag handle accessibility elements for the layout item element.
- [func accessibilityHorizontalUnits() -> NSAccessibilityUnits](nsaccessibilityprotocol/accessibilityhorizontalunits.md)
  Returns the units that the layout area uses for horizontal values.
- [func setAccessibilityHorizontalUnits(NSAccessibilityUnits)](nsaccessibilityprotocol/setaccessibilityhorizontalunits(_:).md)
  Sets the units that the layout area uses for horizontal values.
- [func accessibilityHorizontalUnitDescription() -> String?](nsaccessibilityprotocol/accessibilityhorizontalunitdescription.md)
  Returns the description of the layout area’s horizontal units.
- [func setAccessibilityHorizontalUnitDescription(String?)](nsaccessibilityprotocol/setaccessibilityhorizontalunitdescription(_:).md)
  Sets the description of the layout area’s horizontal units.
- [func accessibilityVerticalUnits() -> NSAccessibilityUnits](nsaccessibilityprotocol/accessibilityverticalunits.md)
  Returns the units that the layout area uses for vertical values.
- [func setAccessibilityVerticalUnits(NSAccessibilityUnits)](nsaccessibilityprotocol/setaccessibilityverticalunits(_:).md)
  Sets the units that the layout area uses for vertical values.
- [func accessibilityVerticalUnitDescription() -> String?](nsaccessibilityprotocol/accessibilityverticalunitdescription.md)
  Returns the description of the layout area’s vertical units.
- [func setAccessibilityVerticalUnitDescription(String?)](nsaccessibilityprotocol/setaccessibilityverticalunitdescription(_:).md)
  Sets the description of the layout area’s vertical units.
- [func accessibilityLayoutPoint(forScreenPoint: NSPoint) -> NSPoint](nsaccessibilityprotocol/accessibilitylayoutpoint(forscreenpoint:).md)
  Converts the provided point in screen coordinates to a point in the layout area’s coordinate system.
- [func accessibilityLayoutSize(forScreenSize: NSSize) -> NSSize](nsaccessibilityprotocol/accessibilitylayoutsize(forscreensize:).md)
  Converts the provided size in screen coordinates to a size in the layout area’s coordinate system.
- [func accessibilityScreenPoint(forLayoutPoint: NSPoint) -> NSPoint](nsaccessibilityprotocol/accessibilityscreenpoint(forlayoutpoint:).md)
  Converts the provided point in the layout area’s coordinates to a point in the screen’s coordinate system.
- [func accessibilityScreenSize(forLayoutSize: NSSize) -> NSSize](nsaccessibilityprotocol/accessibilityscreensize(forlayoutsize:).md)
  Converts the provided size in the layout area’s coordinates to a size in the screen’s coordinate system.
### Configuring sliders
- [func accessibilityAllowedValues() -> [NSNumber]?](nsaccessibilityprotocol/accessibilityallowedvalues.md)
  Returns the allowed values for the slider accessibility element.
- [func setAccessibilityAllowedValues([NSNumber]?)](nsaccessibilityprotocol/setaccessibilityallowedvalues(_:).md)
  Sets the allowed values for the slider accessibility element.
- [func accessibilityLabelUIElements() -> [Any]?](nsaccessibilityprotocol/accessibilitylabeluielements.md)
  Returns the child label elements for the slider accessibility element.
- [func setAccessibilityLabelUIElements([Any]?)](nsaccessibilityprotocol/setaccessibilitylabeluielements(_:).md)
  Sets the child label elements for the slider accessibility element.
- [func accessibilityLabelValue() -> Float](nsaccessibilityprotocol/accessibilitylabelvalue.md)
  Returns the value of the label accessibility element.
- [func setAccessibilityLabelValue(Float)](nsaccessibilityprotocol/setaccessibilitylabelvalue(_:).md)
  Sets the value of the label accessibility element.
### Configuring split views
- [func accessibilityNextContents() -> [Any]?](nsaccessibilityprotocol/accessibilitynextcontents.md)
  Returns the contents that follow the divider accessibility element.
- [func setAccessibilityNextContents([Any]?)](nsaccessibilityprotocol/setaccessibilitynextcontents(_:).md)
  Sets the contents that follow the divider accessibility element.
- [func accessibilityPreviousContents() -> [Any]?](nsaccessibilityprotocol/accessibilitypreviouscontents.md)
  Returns the contents that precede the divider accessibility element.
- [func setAccessibilityPreviousContents([Any]?)](nsaccessibilityprotocol/setaccessibilitypreviouscontents(_:).md)
  Sets the contents that precede the divider accessibility element.
- [func accessibilitySplitters() -> [Any]?](nsaccessibilityprotocol/accessibilitysplitters.md)
  Returns an array that contains the views and splitter bar from the split view.
- [func setAccessibilitySplitters([Any]?)](nsaccessibilityprotocol/setaccessibilitysplitters(_:).md)
  Sets the array that contains the views and splitter bar from the split view.
### Configuring tabs and toolbars
- [func accessibilityOverflowButton() -> Any?](nsaccessibilityprotocol/accessibilityoverflowbutton.md)
  Returns the overflow button for the toolbar.
- [func setAccessibilityOverflowButton(Any?)](nsaccessibilityprotocol/setaccessibilityoverflowbutton(_:).md)
  Sets the overflow button for the toolbar.
- [func accessibilityTabs() -> [Any]?](nsaccessibilityprotocol/accessibilitytabs.md)
  Returns the tab accessibility elements for the tab view.
- [func setAccessibilityTabs([Any]?)](nsaccessibilityprotocol/setaccessibilitytabs(_:).md)
  Sets the tab accessibility elements for the tab view.
### Configuring ruler views
- [func accessibilityMarkerGroupUIElement() -> Any?](nsaccessibilityprotocol/accessibilitymarkergroupuielement.md)
  Returns the user interface element that functions as a marker group for the ruler accessibility element.
- [func setAccessibilityMarkerGroupUIElement(Any?)](nsaccessibilityprotocol/setaccessibilitymarkergroupuielement(_:).md)
  Sets the user interface element that functions as a marker group for the ruler accessibility element.
- [func accessibilityMarkerTypeDescription() -> String?](nsaccessibilityprotocol/accessibilitymarkertypedescription.md)
  Returns the human-readable description of the marker type.
- [func setAccessibilityMarkerTypeDescription(String?)](nsaccessibilityprotocol/setaccessibilitymarkertypedescription(_:).md)
  Sets the human-readable description of the marker type.
- [func accessibilityMarkerUIElements() -> [Any]?](nsaccessibilityprotocol/accessibilitymarkeruielements.md)
  Returns the array of marker accessibility elements for the ruler.
- [func setAccessibilityMarkerUIElements([Any]?)](nsaccessibilityprotocol/setaccessibilitymarkeruielements(_:).md)
  Sets the array of marker accessibility elements for the ruler.
- [func accessibilityMarkerValues() -> Any?](nsaccessibilityprotocol/accessibilitymarkervalues.md)
  Returns the marker values for the ruler.
- [func setAccessibilityMarkerValues(Any?)](nsaccessibilityprotocol/setaccessibilitymarkervalues(_:).md)
  Sets the marker values for the ruler.
- [func accessibilityRulerMarkerType() -> NSAccessibilityRulerMarkerType](nsaccessibilityprotocol/accessibilityrulermarkertype.md)
  Returns the type of markers for the ruler.
- [func setAccessibilityRulerMarkerType(NSAccessibilityRulerMarkerType)](nsaccessibilityprotocol/setaccessibilityrulermarkertype(_:).md)
  Sets the type of markers for the ruler.
- [func accessibilityUnits() -> NSAccessibilityUnits](nsaccessibilityprotocol/accessibilityunits.md)
  Returns the units for the ruler.
- [func setAccessibilityUnits(NSAccessibilityUnits)](nsaccessibilityprotocol/setaccessibilityunits(_:).md)
  Sets the units used for the ruler.
- [func accessibilityUnitDescription() -> String?](nsaccessibilityprotocol/accessibilityunitdescription.md)
  Returns the human-readable description of the ruler’s units.
- [func setAccessibilityUnitDescription(String?)](nsaccessibilityprotocol/setaccessibilityunitdescription(_:).md)
  Sets the human-readable description of the ruler’s units.
- [enum NSAccessibilityRulerMarkerType](nsaccessibilityrulermarkertype.md)
  Values that indicate the marker type of an accessibility element.
- [enum NSAccessibilityUnits](nsaccessibilityunits.md)
  Values that indicate the unit values of a ruler or layout area.
### Managing documents and editing
- [func accessibilityDocument() -> String?](nsaccessibilityprotocol/accessibilitydocument.md)
  Returns the URL for the file that the accessibility element represents.
- [func setAccessibilityDocument(String?)](nsaccessibilityprotocol/setaccessibilitydocument(_:).md)
  Sets the URL for the file that the accessibility element represents.
- [func isAccessibilityEdited() -> Bool](nsaccessibilityprotocol/isaccessibilityedited.md)
  Returns a Boolean value that indicates whether the accessibility element is in an edited state.
- [func setAccessibilityEdited(Bool)](nsaccessibilityprotocol/setaccessibilityedited(_:).md)
  Sets a Boolean value that indicates whether the accessibility element is in an edited state.
- [func accessibilityFilename() -> String?](nsaccessibilityprotocol/accessibilityfilename.md)
  Returns the filename for the file that the accessibility element represents.
- [func setAccessibilityFilename(String?)](nsaccessibilityprotocol/setaccessibilityfilename(_:).md)
  Sets the filename for the file that the accessibility element represents.
### Configuring linkage elements
- [func accessibilityLinkedUIElements() -> [Any]?](nsaccessibilityprotocol/accessibilitylinkeduielements.md)
  Returns the elements that have links with the accessibility element.
- [func setAccessibilityLinkedUIElements([Any]?)](nsaccessibilityprotocol/setaccessibilitylinkeduielements(_:).md)
  Sets the elements that have links with the accessibility element.
- [func accessibilityServesAsTitleForUIElements() -> [Any]?](nsaccessibilityprotocol/accessibilityservesastitleforuielements.md)
  Returns the list of elements that the accessibility element is a title for.
- [func setAccessibilityServesAsTitleForUIElements([Any]?)](nsaccessibilityprotocol/setaccessibilityservesastitleforuielements(_:).md)
  Sets the list of elements that the accessibility element is a title for.
- [func accessibilityTitleUIElement() -> Any?](nsaccessibilityprotocol/accessibilitytitleuielement.md)
  Returns the static text element that represents the accessibility element’s title.
- [func setAccessibilityTitleUIElement(Any?)](nsaccessibilityprotocol/setaccessibilitytitleuielement(_:).md)
  Sets the static text element that represents the accessibility element’s title.
### Configuring search fields
- [func accessibilityClearButton() -> Any?](nsaccessibilityprotocol/accessibilityclearbutton.md)
  Returns the clear button for the search field.
- [func setAccessibilityClearButton(Any?)](nsaccessibilityprotocol/setaccessibilityclearbutton(_:).md)
  Sets the clear button for the search field.
- [func accessibilitySearchButton() -> Any?](nsaccessibilityprotocol/accessibilitysearchbutton.md)
  Returns the search button for the search field.
- [func setAccessibilitySearchButton(Any?)](nsaccessibilityprotocol/setaccessibilitysearchbutton(_:).md)
  Sets the search button for the search field.
- [func accessibilitySearchMenu() -> Any?](nsaccessibilityprotocol/accessibilitysearchmenu.md)
  Returns the search menu for the search field.
- [func setAccessibilitySearchMenu(Any?)](nsaccessibilityprotocol/setaccessibilitysearchmenu(_:).md)
  Sets the search menu for the search field.
### Confirming and canceling operations
- [func accessibilityPerformCancel() -> Bool](nsaccessibilityprotocol/accessibilityperformcancel.md)
  Cancels the current operation.
- [func accessibilityPerformConfirm() -> Bool](nsaccessibilityprotocol/accessibilityperformconfirm.md)
  Simulates pressing Return in the accessibility element.
### Selecting elements
- [func accessibilityPerformPick() -> Bool](nsaccessibilityprotocol/accessibilityperformpick.md)
  Selects the accessibility element.
- [func accessibilityPerformPress() -> Bool](nsaccessibilityprotocol/accessibilityperformpress.md)
  Simulates clicking the accessibility element.
### Searching elements
- [let NSAccessibilitySearchCurrentElementKey: String](nsaccessibilitysearchcurrentelementkey.md)
- [let NSAccessibilitySearchCurrentRangeKey: String](nsaccessibilitysearchcurrentrangekey.md)
- [let NSAccessibilitySearchDirectionKey: String](nsaccessibilitysearchdirectionkey.md)
- [let NSAccessibilitySearchDirectionNext: String](nsaccessibilitysearchdirectionnext.md)
- [let NSAccessibilitySearchDirectionPrevious: String](nsaccessibilitysearchdirectionprevious.md)
- [struct NSAccessibilitySearchKey](nsaccessibilitysearchkey.md)
### Showing user interface elements
- [func accessibilityPerformShowAlternateUI() -> Bool](nsaccessibilityprotocol/accessibilityperformshowalternateui.md)
  Displays the accessibility element’s alternative UI.
- [func accessibilityPerformShowDefaultUI() -> Bool](nsaccessibilityprotocol/accessibilityperformshowdefaultui.md)
  Returns to the accessibility element’s original UI.
- [func accessibilityPerformShowMenu() -> Bool](nsaccessibilityprotocol/accessibilityperformshowmenu.md)
  Displays the menu accessibility element.
- [func accessibilityPerformRaise() -> Bool](nsaccessibilityprotocol/accessibilityperformraise.md)
  Brings the window to the front.
### Incrementing, decrementing, and deleting values
- [func accessibilityIncrementButton() -> Any?](nsaccessibilityprotocol/accessibilityincrementbutton.md)
  Returns the increment button for the stepper accessibility element.
- [func setAccessibilityIncrementButton(Any?)](nsaccessibilityprotocol/setaccessibilityincrementbutton(_:).md)
  Sets the increment button for the stepper accessibility element.
- [func accessibilityDecrementButton() -> Any?](nsaccessibilityprotocol/accessibilitydecrementbutton.md)
  Returns the decrement button for the stepper accessibility element.
- [func setAccessibilityDecrementButton(Any?)](nsaccessibilityprotocol/setaccessibilitydecrementbutton(_:).md)
  Sets the decrement button for the stepper accessibility element.
- [func accessibilityPerformIncrement() -> Bool](nsaccessibilityprotocol/accessibilityperformincrement.md)
  Increments the accessibility element’s value.
- [func accessibilityPerformDecrement() -> Bool](nsaccessibilityprotocol/accessibilityperformdecrement.md)
  Decrements the accessibility element’s value.
- [func accessibilityPerformDelete() -> Bool](nsaccessibilityprotocol/accessibilityperformdelete.md)
  Deletes the accessibility element’s value.
### Managing notifications
- [static func post(element: Any, notification: NSAccessibility.Notification)](nsaccessibility-swift.struct/post(element:notification:).md)
  Sends a notification to any observing assistive apps.
- [static func post(element: Any, notification: NSAccessibility.Notification, userInfo: [NSAccessibility.NotificationUserInfoKey : Any]?)](nsaccessibility-swift.struct/post(element:notification:userinfo:).md)
  Sends a notification and an optional user info dictionary to any observing assistive apps.
- [NSAccessibility.Notification](nsaccessibility-swift.struct/notification.md)
  The name of the notification.
- [NSAccessibility.NotificationUserInfoKey](nsaccessibility-swift.struct/notificationuserinfokey.md)
  The key in the user info dictionary for a notification.
### Handling errors
- [static let ErrorCodeExceptionInfo: String](nsaccessibility-swift.struct/errorcodeexceptioninfo.md)
  An integer error code for debugging.
### Supporting types
- [struct NSAccessibility](nsaccessibility-swift.struct.md)
  A namespace for accessibility symbols for AppKit apps.
### Instance methods
- [func accessibilityAttributedUserInputLabels() -> [NSAttributedString]?](nsaccessibilityprotocol/accessibilityattributeduserinputlabels.md)
- [func accessibilityUserInputLabels() -> [String]?](nsaccessibilityprotocol/accessibilityuserinputlabels.md)
- [func setAccessibilityAttributedUserInputLabels([NSAttributedString]?)](nsaccessibilityprotocol/setaccessibilityattributeduserinputlabels(_:).md)
- [func setAccessibilityUserInputLabels([String]?)](nsaccessibilityprotocol/setaccessibilityuserinputlabels(_:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSAccessibilityElement](nsaccessibilityelement-swift.class.md)
- [NSActionCell](nsactioncell.md)
- [NSApplication](nsapplication.md)
- [NSBackgroundExtensionView](nsbackgroundextensionview.md)
- [NSBox](nsbox.md)
- [NSBrowser](nsbrowser.md)
- [NSBrowserCell](nsbrowsercell.md)
- [NSButton](nsbutton.md)
- [NSButtonCell](nsbuttoncell.md)
- [NSCell](nscell.md)
- [NSClipView](nsclipview.md)
- [NSCollectionView](nscollectionview.md)
- [NSColorPanel](nscolorpanel.md)
- [NSColorWell](nscolorwell.md)
- [NSComboBox](nscombobox.md)
- [NSComboBoxCell](nscomboboxcell.md)
- [NSComboButton](nscombobutton.md)
- [NSControl](nscontrol.md)
- [NSDatePicker](nsdatepicker.md)
- [NSDatePickerCell](nsdatepickercell.md)
- [NSDrawer](nsdrawer.md)
- [NSFontPanel](nsfontpanel.md)
- [NSForm](nsform.md)
- [NSFormCell](nsformcell.md)
- [NSGlassEffectContainerView](nsglasseffectcontainerview.md)
- [NSGlassEffectView](nsglasseffectview.md)
- [NSGridView](nsgridview.md)
- [NSImageCell](nsimagecell.md)
- [NSImageView](nsimageview.md)
- [NSLevelIndicator](nslevelindicator.md)
- [NSLevelIndicatorCell](nslevelindicatorcell.md)
- [NSMatrix](nsmatrix.md)
- [NSMenu](nsmenu.md)
- [NSMenuItem](nsmenuitem.md)
- [NSMenuItemCell](nsmenuitemcell.md)
- [NSOpenGLView](nsopenglview.md)
- [NSOpenPanel](nsopenpanel.md)
- [NSOutlineView](nsoutlineview.md)
- [NSPanel](nspanel.md)
- [NSPathCell](nspathcell.md)
- [NSPathComponentCell](nspathcomponentcell.md)
- [NSPathControl](nspathcontrol.md)
- [NSPopUpButton](nspopupbutton.md)
- [NSPopUpButtonCell](nspopupbuttoncell.md)
- [NSPopover](nspopover.md)
- [NSPredicateEditor](nspredicateeditor.md)
- [NSProgressIndicator](nsprogressindicator.md)
- [NSRuleEditor](nsruleeditor.md)
- [NSRulerView](nsrulerview.md)
- [NSSavePanel](nssavepanel.md)
- [NSScrollView](nsscrollview.md)
- [NSScroller](nsscroller.md)
- [NSScrubber](nsscrubber.md)
- [NSScrubberArrangedView](nsscrubberarrangedview.md)
- [NSScrubberImageItemView](nsscrubberimageitemview.md)
- [NSScrubberItemView](nsscrubberitemview.md)
- [NSScrubberSelectionView](nsscrubberselectionview.md)
- [NSScrubberTextItemView](nsscrubbertextitemview.md)
- [NSSearchField](nssearchfield.md)
- [NSSearchFieldCell](nssearchfieldcell.md)
- [NSSecureTextField](nssecuretextfield.md)
- [NSSecureTextFieldCell](nssecuretextfieldcell.md)
- [NSSegmentedCell](nssegmentedcell.md)
- [NSSegmentedControl](nssegmentedcontrol.md)
- [NSSlider](nsslider.md)
- [NSSliderAccessory](nsslideraccessory.md)
- [NSSliderCell](nsslidercell.md)
- [NSSplitView](nssplitview.md)
- [NSStackView](nsstackview.md)
- [NSStatusBarButton](nsstatusbarbutton.md)
- [NSStepper](nsstepper.md)
- [NSStepperCell](nssteppercell.md)
- [NSSwitch](nsswitch.md)
- [NSTabView](nstabview.md)
- [NSTableCellView](nstablecellview.md)
- [NSTableHeaderCell](nstableheadercell.md)
- [NSTableHeaderView](nstableheaderview.md)
- [NSTableRowView](nstablerowview.md)
- [NSTableView](nstableview.md)
- [NSText](nstext.md)
- [NSTextAttachmentCell](nstextattachmentcell-swift.class.md)
- [NSTextField](nstextfield.md)
- [NSTextFieldCell](nstextfieldcell.md)
- [NSTextInsertionIndicator](nstextinsertionindicator.md)
- [NSTextView](nstextview.md)
- [NSTokenField](nstokenfield.md)
- [NSTokenFieldCell](nstokenfieldcell.md)
- [NSView](nsview.md)
- [NSVisualEffectView](nsvisualeffectview.md)
- [NSWindow](nswindow.md)

## See Also

- [struct NSAccessibility](nsaccessibility-swift.struct.md)
  A namespace for accessibility symbols for AppKit apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol)*