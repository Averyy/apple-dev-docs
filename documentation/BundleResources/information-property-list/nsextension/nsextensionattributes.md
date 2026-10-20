# NSExtensionAttributes

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

Properties of an app extension.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- macOS 10.10+
- visionOS 1.0+

## Details

- **Name**: `NSExtensionAttributes`
- **Type**: dictionary

## Topics

### Appearance and Presentation
- [NSExtensionActionWantsFullScreenPresentation](./nsextensionactionwantsfullscreenpresentation.md)
  A Boolean value indicating whether the Action extension is presented in full screen.
- [NSExtensionMainStoryboard](./nsextensionmainstoryboard.md)
  The name of the app extension’s main storyboard file.
- [NSExtensionOverridesHostUIAppearance](./nsextensionoverrideshostuiappearance.md)
  A Boolean value indicating whether the app extension ignores appearance changes made by the host app.
- [NSExtensionPointIdentifier](./nsextensionpointidentifier.md)
  The extension point that supports an app extension.
- [NSExtensionPrincipalClass](./nsextensionprincipalclass.md)
  The custom class that implements an app extension’s primary view or functionality.
- [NSExtensionActivationRule](./nsextensionattributes/nsextensionactivationrule.md)
  The semantic data types that a Share or Action extension supports.
- [NSExtensionJavaScriptPreprocessingFile](./nsextensionattributes/nsextensionjavascriptpreprocessingfile.md)
  The name of a JavaScript file supplied by a Share or Action extension.
### Core Spotlight
- [CSSupportedContentTypes](./nsextensionattributes/cssupportedcontenttypes.md)
### Credential providers
- [ASCredentialProviderExtensionCapabilities](./nsextensionattributes/ascredentialproviderextensioncapabilities.md)
  The credential types supported by a credential provider extension, and whether it presents a user interface.
### Intents
- [IntentsSupported](./intentssupported.md)
  The names of the intents that an extension supports.
- [SupportedMediaCategories](./nsextensionattributes/supportedmediacategories.md)
  Types of media supported by an app extension’s media-playing intents.
### Mail
- [MEComposeSession](./nsextensionattributes/mecomposesession.md)
- [MEExtensionCapabilities](./nsextensionattributes/meextensioncapabilities.md)
### Photos
- [PHProjectExtensionDefinesProjectTypes](./nsextensionattributes/phprojectextensiondefinesprojecttypes.md)
  A Boolean value indicating whether the Photos app gets a list of supported project types from an extension.
- [PHSupportedMediaTypes](./nsextensionattributes/phsupportedmediatypes.md)
  The types of assets a Photo Editing extension can edit.
### Quick Actions
- [NSExtensionServiceAllowsFinderPreviewItem](./nsextensionattributes/nsextensionserviceallowsfinderpreviewitem.md)
  A Boolean value indicating whether the extension appears in the Finder Preview pane and Quick Actions menu.
- [NSExtensionServiceFinderPreviewIconName](./nsextensionattributes/nsextensionservicefinderpreviewiconname.md)
  The name of an icon for display when the extension appears in the Finder Preview pane and Quick Actions menu.
- [NSExtensionServiceFinderPreviewLabel](./nsextensionattributes/nsextensionservicefinderpreviewlabel.md)
  A name for display when the extension appears in the Finder Preview pane and Quick Actions menu.
- [NSExtensionServiceRoleType](./nsextensionattributes/nsextensionserviceroletype.md)
  The type of task an Action extension performs.
### Toolbar
- [NSExtensionServiceAllowsToolbarItem](./nsextensionattributes/nsextensionserviceallowstoolbaritem.md)
  A Boolean value indicating whether an Action extension displays an item in a window’s toolbar.
- [NSExtensionServiceToolbarIconFile](./nsextensionattributes/nsextensionservicetoolbariconfile.md)
  The image for an Action extension’s toolbar item.
- [NSExtensionServiceToolbarPaletteLabel](./nsextensionattributes/nsextensionservicetoolbarpalettelabel.md)
  The label for an Action extension’s toolbar item.
### Touch Bar
- [NSExtensionServiceAllowsTouchBarItem](./nsextensionattributes/nsextensionserviceallowstouchbaritem.md)
  A Boolean value indicating whether the extension appears as a Quick Action in the Touch Bar.
- [NSExtensionServiceTouchBarBezelColorName](./nsextensionattributes/nsextensionservicetouchbarbezelcolorname.md)
  The color to use for the bezel around the extension when it appears as a Quick Action in the Touch Bar.
- [NSExtensionServiceTouchBarIconName](./nsextensionattributes/nsextensionservicetouchbariconname.md)
  The name of an icon for display when the extension appears as a Quick Action in the Touch Bar
- [NSExtensionServiceTouchBarLabel](./nsextensionattributes/nsextensionservicetouchbarlabel.md)
  A name for display when the extension appears as a Quick Action in the Touch Bar.
### UIKit
- [IDMessageFilterExtensionNetworkURL](./nsextensionattributes/idmessagefilterextensionnetworkurl.md)
  The server that a Message Filter app extension may defer a query to.
- [ILClassificationExtensionSMSReportDestination](./nsextensionattributes/ilclassificationextensionsmsreportdestination.md)
  The phone number that receives SMS messages when the user reports an SMS message or a call.
- [IsASCIICapable](./nsextensionattributes/isasciicapable.md)
  A Boolean value indicating whether a custom keyboard displays standard ASCII characters.
- [MSMessagesAppPresentationContextMessages](./nsextensionattributes/msmessagesapppresentationcontextmessages.md)
  The contexts that an iMessage app or sticker pack supports.
- [PrefersRightToLeft](./nsextensionattributes/prefersrighttoleft.md)
  A Boolean value indicating whether a keyboard extension supports right-to-left languages.
- [PrimaryLanguage](./nsextensionattributes/primarylanguage.md)
  The primary language for a keyboard extension.
- [RequestsOpenAccess](./nsextensionattributes/requestsopenaccess.md)
  A Boolean value indicating whether a custom keyboard uses a shared container and accesses the network.
- [UIDocumentPickerModes](./nsextensionattributes/uidocumentpickermodes.md)
  The modes that a Document Picker extension supports.
- [UIDocumentPickerSupportedFileTypes](./nsextensionattributes/uidocumentpickersupportedfiletypes.md)
  The Uniform Type Identifiers that a document picker extension supports.
- [UNNotificationExtensionCategory](./nsextensionattributes/unnotificationextensioncategory.md)
  The identifier of a category declared by the app extension.
- [UNNotificationExtensionDefaultContentHidden](./nsextensionattributes/unnotificationextensiondefaultcontenthidden.md)
  A Boolean value indicating whether only the app extension’s custom view controller is displayed in the notification interface.
- [UNNotificationExtensionInitialContentSizeRatio](./nsextensionattributes/unnotificationextensioninitialcontentsizeratio.md)
  The initial size of the view controller’s view for an app extension, expressed as a ratio of its height to its width.
- [UNNotificationExtensionOverridesDefaultTitle](./nsextensionattributes/unnotificationextensionoverridesdefaulttitle.md)
  A Boolean value indicating whether the title of the app extension’s view controller is used as the title of the notification.
- [UNNotificationExtensionUserInteractionEnabled](./nsextensionattributes/unnotificationextensionuserinteractionenabled.md)
  A Boolean value indicating whether user interactions in a custom notification are enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/nsextensionattributes)*