# UIInputView

**Framework**: UIKit  
**Kind**: class

An object that displays and manages custom input for a view when that view becomes the first responder.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIInputView
```

#### Overview

The [`UIInputView`](uiinputview.md) class is designed to match the appearance of the standard system keyboard when used as an input view with a responder. When defining your own custom input views or input accessory views, you can use a [`UIInputView`](uiinputview.md) object as the root view and add any subviews you want to create your input view. The input view and its subviews receive tinting and blur effects based on the options you specify at initialization time.

> **Note**:  The effects offered by this class are applied only when the view is attached to a responder as either an input view or input accessory view. For subviews to receive style effects, they must conform to the [`UIAppearance`](uiappearance.md) protocol.

## Topics

### Initializing an input view
- [init(frame: CGRect, inputViewStyle: UIInputView.Style)](uiinputview/init(frame:inputviewstyle:).md)
  Initializes and returns an input view using the specified style information.
- [init?(coder: NSCoder)](uiinputview/init(coder:).md)
  Creates an input view from data in an unarchiver.
### Getting the input style
- [var inputViewStyle: UIInputView.Style](uiinputview/inputviewstyle.md)
  The style for the content of the view.
- [UIInputView.Style](uiinputview/style.md)
  Constants that indicate the appearance changes for an input view.
### Sizing the input view
- [var allowsSelfSizing: Bool](uiinputview/allowsselfsizing.md)
  A Boolean value that indicates whether the input view is responsible for its own size.

## Relationships

### Inherits From
- [UIView](uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [Creating a custom keyboard](creating-a-custom-keyboard.md)
  Add an extension to your Xcode project to provide systemwide customized text input.
- [class UIInputViewController](uiinputviewcontroller.md)
  The primary view controller for a custom keyboard app extension.
- [class UILexicon](uilexicon.md)
  A read-only array of term pairs, each in a lexicon entry object, for a custom keyboard.
- [class UILexiconEntry](uilexiconentry.md)
  A read-only term pair, available within a lexicon object, for a custom keyboard.
- [protocol UITextDocumentProxy](uitextdocumentproxy.md)
  An object that provides textual context to a custom keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputview)*