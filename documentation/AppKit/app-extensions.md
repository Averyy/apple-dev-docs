# App Extensions

**Framework**: AppKit

Extend your app’s basic functionality to other parts of the system.

## Topics

### Extension Support
- [class NSExtensionContext](../Foundation/NSExtensionContext.md)
  The host app context from which an app extension is invoked.
- [protocol NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
  The interface an app extension uses to respond to a request from a host app.
### Quick Actions
- [Add Functionality to Finder with Action Extensions](add-functionality-to-finder-with-action-extensions.md)
  Implement Action Extensions to provide quick access to commonly used features of your app.
- [NSExtensionServiceAllowsFinderPreviewItem](../BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/NSExtensionServiceAllowsFinderPreviewItem.md)
  A Boolean value indicating whether the extension appears in the Finder Preview pane and Quick Actions menu.
- [NSExtensionServiceFinderPreviewLabel](../BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/NSExtensionServiceFinderPreviewLabel.md)
  A name for display when the extension appears in the Finder Preview pane and Quick Actions menu.
- [NSExtensionServiceFinderPreviewIconName](../BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/NSExtensionServiceFinderPreviewIconName.md)
  The name of an icon for display when the extension appears in the Finder Preview pane and Quick Actions menu.
- [NSExtensionServiceAllowsTouchBarItem](../BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/NSExtensionServiceAllowsTouchBarItem.md)
  A Boolean value indicating whether the extension appears as a Quick Action in the Touch Bar.
- [NSExtensionServiceTouchBarLabel](../BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/NSExtensionServiceTouchBarLabel.md)
  A name for display when the extension appears as a Quick Action in the Touch Bar.
- [NSExtensionServiceTouchBarIconName](../BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/NSExtensionServiceTouchBarIconName.md)
  The name of an icon for display when the extension appears as a Quick Action in the Touch Bar
- [NSExtensionServiceTouchBarBezelColorName](../BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/NSExtensionServiceTouchBarBezelColorName.md)
  The color to use for the bezel around the extension when it appears as a Quick Action in the Touch Bar.
### Mail Extensions
- [Build Mail App Extensions](../MailKit/build-mail-app-extensions.md)
  Create app extensions that block content, perform message and composing actions, and help message security.
### UTI Subtypes for Data Detector Types
- [let NSTypeIdentifierAddressText: String](nstypeidentifieraddresstext.md)
- [let NSTypeIdentifierDateText: String](nstypeidentifierdatetext.md)
- [let NSTypeIdentifierPhoneNumberText: String](nstypeidentifierphonenumbertext.md)
- [let NSTypeIdentifierTransitInformationText: String](nstypeidentifiertransitinformationtext.md)

## See Also

- [App and Environment](app-and-environment.md)
  Learn about the objects that you use to interact with the system.
- [Documents, Data, and Pasteboard](documents-data-and-pasteboard.md)
  Organize your app’s data and preferences, and share that data on the pasteboard or in iCloud.
- [Cocoa Bindings](cocoa-bindings.md)
  Automatically synchronize your data model with your app’s interface using Cocoa Bindings.
- [Resource Management](resource-management.md)
  Manage the storyboards and nib files containing your app’s user interface, and learn how to load data that is stored in resource files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/app-extensions)*