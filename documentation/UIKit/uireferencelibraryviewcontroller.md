# UIReferenceLibraryViewController

**Framework**: UIKit  
**Kind**: class

A view controller that displays a standard interface for looking up the definition of a word or term.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIReferenceLibraryViewController
```

#### Overview

A [`UIReferenceLibraryViewController`](uireferencelibraryviewcontroller.md) object should not be used to display wordlists, create a standalone dictionary app, or republish the content in any form.

You create and initialize a reference library view controller using the [`init(term:)`](uireferencelibraryviewcontroller/init(term:).md) method. You pass the term to define as the parameter to this method and the definition is displayed. You can present this view controller modally or as part of another interface. On iPad, you can set the reference library view controller as the content view controller of a [`UIPopoverController`](uipopovercontroller.md) object. Optionally, use the [`dictionaryHasDefinition(forTerm:)`](uireferencelibraryviewcontroller/dictionaryhasdefinition(forterm:).md) class method to check if a definition is available for a given term before creating an instance—for example, use this method if you want to change the user interface depending on whether a definition is available.

## Topics

### Creating a reference-library view controller
- [class func dictionaryHasDefinition(forTerm: String) -> Bool](uireferencelibraryviewcontroller/dictionaryhasdefinition(forterm:).md)
  Returns whether a definition is available for the given term.
- [init(term: String)](uireferencelibraryviewcontroller/init(term:).md)
  Initializes a newly created reference-library view controller to display the definition of the given term.
- [init(coder: NSCoder)](uireferencelibraryviewcontroller/init(coder:).md)
  Creates a reference-library view controller from data in an unarchiver.

## Relationships

### Inherits From
- [UIViewController](uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIStateRestoring](uistaterestoring.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uireferencelibraryviewcontroller)*