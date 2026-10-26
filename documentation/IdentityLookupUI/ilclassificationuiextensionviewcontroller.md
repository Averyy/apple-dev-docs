# ILClassificationUIExtensionViewController

**Framework**: IdentityLookupUI  
**Kind**: class  
**Role**: Class

The superclass for an Unwanted Communication Reporting extension’s principal view controller.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
class ILClassificationUIExtensionViewController
```

```objc
@interface ILClassificationUIExtensionViewController : UIViewController
```

#### Overview

Subclass this view controller to create a user interface that gathers additional information from the user about the reported communication.

## Topics

### Collecting Data from the User
- [func prepare(for: ILClassificationRequest)](./ilclassificationuiextensionviewcontroller/prepare%28for%29.md)
  Notifies the view controller just before the system presents it to the user.
- [func classificationResponse(for: ILClassificationRequest) -> ILClassificationResponse](./ilclassificationuiextensionviewcontroller/classificationresponse%28for%29.md)
  Notifies the view controller when the user finishes entering data and presses the Done button.
### Managing the Request
- [var extensionContext: ILClassificationUIExtensionContext](./ilclassificationuiextensionviewcontroller/extensioncontext.md)
  The context for the current request.
- [class ILClassificationUIExtensionContext](./ilclassificationuiextensioncontext.md)
  An object that manages the state of the current request.

## Relationships

### Inherits From
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookupui/ilclassificationuiextensionviewcontroller)*