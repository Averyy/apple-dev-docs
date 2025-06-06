# UIButton

**Framework**: Uikit  
**Kind**: class

A control that executes your custom code in response to user interactions.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIButton
```

## Mentions

- [Choosing a user interface idiom for your Mac app](choosing-a-user-interface-idiom-for-your-mac-app.md)
- [Supporting VoiceOver in your app](supporting-voiceover-in-your-app.md)
- [Attaching gesture recognizers to UIKit controls](attaching-gesture-recognizers-to-uikit-controls.md)
- [Adding user-focusable elements to a tvOS app](adding-user-focusable-elements-to-a-tvos-app.md)

#### Overview

When you tap a button, or select a button that has focus, the button performs any actions attached to it. You communicate the purpose of a button using a text label, an image, or both. The appearance of buttons is configurable, so you can tint buttons or format titles to match the design of your app. You can add buttons to your interface programmatically or using Interface Builder.

![A screenshot showing three buttons. The first button shows the label “Button”. The second button shows an image of a plus sign in a circle. The third button shows an image of a lowercase “i” in a circle.](https://docs-assets.developer.apple.com/published/abe7c4c3472254b2d40bb7dc8bfb8d5b/media-2557338.png)

When adding a button to your interface, perform the following steps:

- Set the type of the button at creation time.
- Supply a title string or image; size the button appropriately for your content.
- Connect one or more action methods to the button.
- Set up Auto Layout rules to govern the size and position of the button in your interface.
- Provide accessibility information and localized strings.

> ❗ **Important**:  An app built with Mac Catalyst running in macOS 11 throws an exception when calling a button’s [`addGestureRecognizer(_:)`](uiview/addgesturerecognizer(_:).md) method when [`buttonType`](uibutton/buttontype-swift.property.md) is [`UIButton.ButtonType.system`](uibutton/buttontype-swift.enum/system.md) and the user interface idiom is [`UIUserInterfaceIdiom.mac`](uiuserinterfaceidiom/mac.md).

##### Respond to Button Taps

Buttons use the target-action design pattern to notify your app when the user taps the button. Rather than handle touch events directly, you assign action methods to the button and designate which events trigger calls to your methods. At runtime, the button handles all incoming touch events and calls your methods in response.

You connect a button to your action method using the [`addTarget(_:action:for:)`](uicontrol/addtarget(_:action:for:).md) method or by creating a connection in Interface Builder. The signature of an action method takes one of three forms, as shown in the following code. Choose the form that provides the information that you need to respond to the button tap.

##### Configure a Buttons Appearance

A button’s type defines its basic appearance and behavior. You specify the type of a button at creation time using the [`init(type:)`](uibutton/init(type:).md) method or in your storyboard file. After creating a button, you can’t change its type. The most commonly used button types are the Custom and System types, but use the other types when appropriate.

> **Note**:  To configure the appearance of all buttons in your app, use the appearance proxy object. The [`UIButton`](uibutton.md) class implements the [`appearance()`](uiappearance/appearance().md) class method, which you can use to fetch the appearance proxy for all buttons in your app.

###### Configure Button States

Buttons have five states that define their appearance: default, highlighted, focused, selected, and disabled. When you add a button to your interface, it’s in the default state initially, which means the button is enabled and the user isn’t interacting with it. As the user interacts with the button, its state changes to the other values. For example, when the user taps a button with a title, the button moves to the highlighted state.

When configuring a button either programmatically or in Interface Builder, you specify attributes for each state separately. In Interface Builder, use the State Config control in the Attributes inspector to choose the appropriate state and then configure the other attributes. If you don’t specify attributes for a particular state, the [`UIButton`](uibutton.md) class provides a reasonable default behavior. For example, a disabled button is normally dimmed and doesn’t display a highlight when tapped. Other properties of this class, such as the [`adjustsImageWhenHighlighted`](uibutton/adjustsimagewhenhighlighted.md) and [`adjustsImageWhenDisabled`](uibutton/adjustsimagewhendisabled.md) properties, let you alter the default behavior in specific cases.

###### Provide Content

The content of a button consists of a title string or image that you specify. The content you specify is used to configure the [`UILabel`](uilabel.md) and [`UIImageView`](uiimageview.md) object managed by the button itself. You can access these objects using the [`titleLabel`](uibutton/titlelabel.md) or [`imageView`](uibutton/imageview.md) properties and modify their values directly. The methods of this class also provide a convenient shortcut for configuring the appearance of your string or image.

Normally, you configure a button using either a title or an image and size the button accordingly. Buttons can also have a background image, which is positioned behind the content you specify. It’s possible to specify both an image and a title for buttons, which results in the appearance shown in the following image. You can access the current content of a button using the indicated properties.

![Providing a title and image for a button.](https://docs-assets.developer.apple.com/published/b18fd0e1e20cf9a7e61095bb304cda2c/media-3081016%402x.png)

When setting the content of a button, you must specify the title, image, and appearance attributes for each state separately. If you don’t customize the content for a particular state, the button uses the values associated with the Default state and adds any appropriate customizations. For example, in the highlighted state, an image-based button draws a highlight on top of the default image if no custom image is provided.

###### Customize Tint Color

You can specify a custom button tint using the [`tintColor`](uibutton/tintcolor.md) property. This property sets the color of the button image and text. If you don’t explicitly set a tint color, the button uses its superview’s tint color.

###### Specify Edge Insets

Use insets to add or remove space around the content in your custom or system buttons. You can specify separate insets for your button’s title ([`titleEdgeInsets`](uibutton/titleedgeinsets.md)), image ([`imageEdgeInsets`](uibutton/imageedgeinsets.md)), and both the title and image together ([`contentEdgeInsets`](uibutton/contentedgeinsets.md)). When applied, insets affect the corresponding content rectangle of the button, which the Auto Layout engine uses to determine the button’s position.

There should be no reason for you to adjust the edge insets for info, contact, or disclosure buttons.

##### Configure Button Attributes in Interface Builder

The following table lists the core attributes that you configure for buttons in Interface Builder.

| Attribute | Description |
| --- | --- |
| Type | The button type. This attribute determines the default settings for many other button attributes. The value of this attribute can’t be changed at runtime, but you can access it using the [`buttonType`](uibutton/buttontype-swift.property.md) property. |
| State Config | The state selector. After selecting a value in this control, changes to the button’s attributes apply to the specified state. |
| Title | The button’s title. You can specify a button’s title as a plain string or attributed string. |
| (Title Font and Attributes) | The font and other attributes to apply to the button’s title string. The specific configuration options depends on whether you specified a plain string or attributed string for the button’s title. For a plain string, you can customize the font, text color, and shadow color. For an attributed string, you can specify alignment, text direction, indentation, hyphenation, and many other options. |
| Image | The button’s foreground image. Typically, you use template images for a button’s foreground, but you may specify any image in your Xcode project. |
| Background | The button’s background image. The background image is displayed behind its title and foreground image. |

The following table lists attributes that affect the button’s appearance.

| Attribute | Description |
| --- | --- |
| Shadow Offset | The offsets and behavior of the button’s shadow. Shadows affect title strings only. Enable the Reverses on Highlight option to change the highlighting of the shadow when the button state changes to or from the highlighted state. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Configure the offsets programmatically using the [`shadowOffset`](uilabel/shadowoffset.md) property of the button’s [`titleLabel`](uibutton/titlelabel.md) object. Configure the highlighting behavior using the [`reversesTitleShadowWhenHighlighted`](uibutton/reversestitleshadowwhenhighlighted.md) property. |
| Drawing | The drawing behavior of the button. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) When the Shows Touch On Highlight ([`showsTouchWhenHighlighted`](uibutton/showstouchwhenhighlighted.md)) option is enabled, the button adds a white glow to the part of a button that the user touches. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) When the Highlighted Adjusts Image ([`adjustsImageWhenHighlighted`](uibutton/adjustsimagewhenhighlighted.md)) option is enabled, button images get darker when it’s in the highlighted state. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) When the Disabled Adjusts Image ([`adjustsImageWhenDisabled`](uibutton/adjustsimagewhendisabled.md)) option is enabled, the image is dimmed when the button is disabled. |
| Line Break | The line breaking options for the button’s text. Use this attribute to define how the button’s title is modified to fit the available space. |

The following table lists the edge inset attributes for buttons. Use edge inset buttons to alter the rectangle for the button’s content.

| Attribute | Description |
| --- | --- |
| Edge | The edge insets to configure. You can specify separate edge insets for the button’s overall content, its title, and its image. |
| Inset | The inset values. Positive values shrink the corresponding edge, moving it closer to the center of the button. Negative values expand the edge, moving it away from the center of the button. Access these values at runtime using the [`contentEdgeInsets`](uibutton/contentedgeinsets.md), [`titleEdgeInsets`](uibutton/titleedgeinsets.md), and [`imageEdgeInsets`](uibutton/imageedgeinsets.md) properties. |

For information about the button’s inherited Interface Builder attributes, see [`UIControl`](uicontrol.md) and [`UIView`](uiview.md).

##### Support Localization

To internationalize a button, specify a localized string for the button’s title text. (You may also localize a button’s image as appropriate.)

When using storyboards to build your interface, use Xcode’s base internationalization feature to configure the localizations your project supports. When you add a localization, Xcode creates a strings file for that localization. When configuring your interface programmatically, use the system’s built-in support for loading localized strings and resources. For more information about internationalizing your interface, see [`Internationalization and Localization Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i).

##### Make Buttons Accessible

Buttons are accessible by default. The default accessibility traits for a button are Button and User Interaction Enabled.

The accessibility label, traits, and hint are spoken back to the user when VoiceOver is enabled on a device. The button’s title overwrites its accessibility label; even if you set a custom value for the label, VoiceOver speaks the value of the title. VoiceOver speaks this information when a user taps the button once. For example, when a user taps the Options button in Camera, VoiceOver speaks the following:

- `"Options. Button. Shows additional camera options."`

For more information about making iOS controls accessible, see the accessibility information in [`UIControl`](uicontrol.md). For general information about making your interface accessible, see [`Accessibility Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008785).

## Topics

### Creating buttons
- [init(frame: CGRect)](uibutton/init(frame:).md)
  Creates a new button with the specified frame.
- [convenience init(frame: CGRect, primaryAction: UIAction?)](uibutton/init(frame:primaryaction:).md)
  Creates a new button with the specified frame, registers the primary action event, and sets the title and image to the action’s title and image.
- [init?(coder: NSCoder)](uibutton/init(coder:).md)
  Creates a new button with data in an unarchiver.
### Creating buttons of a specific type
- [convenience init(type: UIButton.ButtonType)](uibutton/init(type:).md)
  Creates and returns a new button of the specified type.
- [convenience init(type: UIButton.ButtonType, primaryAction: UIAction?)](uibutton/init(type:primaryaction:).md)
  Creates a new button with the specified type, registers the primary action event, and sets the title and image to the action’s title and image.
- [UIButton.ButtonType](uibutton/buttontype-swift.enum.md)
  Specifies the style of a button.
### Creating system buttons
- [class func systemButton(with: UIImage, target: Any?, action: Selector?) -> Self](uibutton/systembutton(with:target:action:).md)
  Creates and returns a system type button with specified image, target, and action.
### Creating buttons from a configuration object
- [convenience init(configuration: UIButton.Configuration, primaryAction: UIAction?)](uibutton/init(configuration:primaryaction:).md)
  Creates a new button with the specified configuration and registers the primary action event.
- [UIButton.Configuration](uibutton/configuration-swift.struct.md)
  A configuration that specifies the appearance and behavior of a button and its contents.
### Managing the appearance with a configuration object
- [var configuration: UIButton.Configuration?](uibutton/configuration-5rlyb.md)
  The configuration for the button’s appearance.
- [var automaticallyUpdatesConfiguration: Bool](uibutton/automaticallyupdatesconfiguration.md)
  A Boolean value that determines whether the button configuration changes when button’s state changes.
- [func setNeedsUpdateConfiguration()](uibutton/setneedsupdateconfiguration.md)
  Requests the system update the button configuration.
- [func updateConfiguration()](uibutton/updateconfiguration.md)
  Updates the button configuration in response to a button state change.
- [var configurationUpdateHandler: UIButton.ConfigurationUpdateHandler?](uibutton/configurationupdatehandler-swift.property.md)
  A closure that executes when the button state changes.
- [typealias ConfigurationUpdateHandler](uibutton/configurationupdatehandler-swift.typealias.md)
  A closure to update the configuration of a button.
### Managing the title
- [var titleLabel: UILabel?](uibutton/titlelabel.md)
  A view that displays the value of the `currentTitle` property for a button.
- [func title(for: UIControl.State) -> String?](uibutton/title(for:).md)
  Returns the title associated with the specified state.
- [func setTitle(String?, for: UIControl.State)](uibutton/settitle(_:for:).md)
  Sets the title to use for the specified state.
- [func attributedTitle(for: UIControl.State) -> NSAttributedString?](uibutton/attributedtitle(for:).md)
  Returns the styled title associated with the specified state.
- [func setAttributedTitle(NSAttributedString?, for: UIControl.State)](uibutton/setattributedtitle(_:for:).md)
  Sets the styled title to use for the specified state.
- [func titleColor(for: UIControl.State) -> UIColor?](uibutton/titlecolor(for:).md)
  Returns the title color used for a state.
- [func setTitleColor(UIColor?, for: UIControl.State)](uibutton/settitlecolor(_:for:).md)
  Sets the color of the title to use for the specified state.
- [func titleShadowColor(for: UIControl.State) -> UIColor?](uibutton/titleshadowcolor(for:).md)
  Returns the shadow color of the title used for a state.
- [func setTitleShadowColor(UIColor?, for: UIControl.State)](uibutton/settitleshadowcolor(_:for:).md)
  Sets the color of the title shadow to use for the specified state.
### Managing images and tint color
- [func backgroundImage(for: UIControl.State) -> UIImage?](uibutton/backgroundimage(for:).md)
  Returns the background image used for a button state.
- [func image(for: UIControl.State) -> UIImage?](uibutton/image(for:).md)
  Returns the image used for a button state.
- [func setBackgroundImage(UIImage?, for: UIControl.State)](uibutton/setbackgroundimage(_:for:).md)
  Sets the background image to use for the specified button state.
- [func setImage(UIImage?, for: UIControl.State)](uibutton/setimage(_:for:).md)
  Sets the image to use for the specified state.
- [func preferredSymbolConfigurationForImage(in: UIControl.State) -> UIImage.SymbolConfiguration?](uibutton/preferredsymbolconfigurationforimage(in:).md)
  Returns the preferred symbol configuration for a button state.
- [func setPreferredSymbolConfiguration(UIImage.SymbolConfiguration?, forImageIn: UIControl.State)](uibutton/setpreferredsymbolconfiguration(_:forimagein:).md)
  Sets the preferred symbol configuration for a button state.
- [var tintColor: UIColor!](uibutton/tintcolor.md)
  The tint color to apply to the button title and image.
### Specifying the role
- [var role: UIButton.Role](uibutton/role-swift.property.md)
  The role of the button.
- [UIButton.Role](uibutton/role-swift.enum.md)
  Constants that describe the role of the button.
### Specifying the behavioral style
- [var behavioralStyle: UIBehavioralStyle](uibutton/behavioralstyle.md)
  The style that determines how the button behaves.
- [var preferredBehavioralStyle: UIBehavioralStyle](uibutton/preferredbehavioralstyle.md)
  The preferred behavioral style.
- [enum UIBehavioralStyle](uibehavioralstyle.md)
  Constants that indicate how a control behaves in apps built with Mac Catalyst.
### Getting the current state
- [var buttonType: UIButton.ButtonType](uibutton/buttontype-swift.property.md)
  The button type.
- [var currentTitle: String?](uibutton/currenttitle.md)
  The current title that is displayed on the button.
- [var currentAttributedTitle: NSAttributedString?](uibutton/currentattributedtitle.md)
  The current styled title that is displayed on the button.
- [var currentTitleColor: UIColor](uibutton/currenttitlecolor.md)
  The color used to display the title.
- [var currentTitleShadowColor: UIColor?](uibutton/currenttitleshadowcolor.md)
  The color of the title’s shadow.
- [var currentImage: UIImage?](uibutton/currentimage.md)
  The current image displayed on the button.
- [var currentBackgroundImage: UIImage?](uibutton/currentbackgroundimage.md)
  The current background image displayed on the button.
- [var currentPreferredSymbolConfiguration: UIImage.SymbolConfiguration?](uibutton/currentpreferredsymbolconfiguration.md)
  The current symbol size, style, and weight.
- [var imageView: UIImageView?](uibutton/imageview.md)
  The button’s image view.
- [var subtitleLabel: UILabel?](uibutton/subtitlelabel.md)
  The label that displays the text of the subtitle.
### Supporting pointer interactions
- [var isPointerInteractionEnabled: Bool](uibutton/ispointerinteractionenabled.md)
  A Boolean that enables pointer interaction.
- [var isHovered: Bool](uibutton/ishovered.md)
  A Boolean value that indicates whether a pointer effect is active.
- [var pointerStyleProvider: UIButton.PointerStyleProvider?](uibutton/pointerstyleprovider-y4eb.md)
  A closure that returns the pointer style to use when the pointer hovers over the button.
- [typealias PointerStyleProvider](uibutton/pointerstyleprovider-swift.typealias.md)
  A type alias defining a closure that returns a pointer style to apply to a button.
- [typealias UIButtonPointerStyleProvider](uibuttonpointerstyleprovider.md)
  A type alias defining a block that returns a pointer style to apply to a button.
### Supporting menu and toggle buttons
- [var menu: UIMenu?](uibutton/menu.md)
  A menu that the button displays.
- [var isHeld: Bool](uibutton/isheld.md)
  A Boolean value that indicates whether the button menu is visible.
- [var changesSelectionAsPrimaryAction: Bool](uibutton/changesselectionasprimaryaction.md)
  A Boolean value that indicates whether the button tracks a selection, either through a menu or a toggle.
- [var preferredMenuElementOrder: UIContextMenuConfiguration.ElementOrder](uibutton/preferredmenuelementorder.md)
  The preferred menu-element ordering strategy for the menu.
### Deprecated
- [Deprecated symbols](uibutton-deprecated-symbols.md)
  Symbols that buttons no longer support.

## Relationships

### Inherits From
- [UIControl](uicontrol.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [UIAccessibilityContentSizeCategoryImageAdjusting](uiaccessibilitycontentsizecategoryimageadjusting.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [Responding to control-based events using target-action](responding-to-control-based-events-using-target-action.md)
  Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [class UIControl](uicontrol.md)
  The base class for controls, which are visual elements that convey a specific action or intention in response to user interactions.
- [class UIColorWell](uicolorwell.md)
  A control that displays a color picker.
- [class UIDatePicker](uidatepicker.md)
  A control for inputting date and time values.
- [class UIPageControl](uipagecontrol.md)
  A control that displays a horizontal series of dots, each of which corresponds to a page in the app’s document or other data-model entity.
- [class UISegmentedControl](uisegmentedcontrol.md)
  A horizontal control that consists of multiple segments, each segment functioning as a discrete button.
- [class UISlider](uislider.md)
  A control for selecting a single value from a continuous range of values.
- [class UIStepper](uistepper.md)
  A control for incrementing or decrementing a value.
- [class UISwitch](uiswitch.md)
  A control that offers a binary choice, such as on/off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/UIKit/uibutton)*