# NSExtensionAttributes

**Framework**: Bundle Resources  
**Kind**: dictionary

Properties of an app extension.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- macOS 10.10+
- visionOS 1.0+

## Topics

### Appearance and Presentation
- [NSExtensionActionWantsFullScreenPresentation](information-property-list/nsextension/nsextensionactionwantsfullscreenpresentation.md)
  A Boolean value indicating whether the Action extension is presented in full screen.
- [NSExtensionMainStoryboard](information-property-list/nsextension/nsextensionmainstoryboard.md)
  The name of the app extension’s main storyboard file.
- [NSExtensionOverridesHostUIAppearance](information-property-list/nsextension/nsextensionoverrideshostuiappearance.md)
  A Boolean value indicating whether the app extension ignores appearance changes made by the host app.
- [NSExtensionPointIdentifier](information-property-list/nsextension/nsextensionpointidentifier.md)
  The extension point that supports an app extension.
- [NSExtensionPrincipalClass](information-property-list/nsextension/nsextensionprincipalclass.md)
  The custom class that implements an app extension’s primary view or functionality.
- [NSExtensionActivationRule](information-property-list/nsextension/nsextensionattributes/nsextensionactivationrule.md)
  The semantic data types that a Share or Action extension supports.
- [NSExtensionJavaScriptPreprocessingFile](information-property-list/nsextension/nsextensionattributes/nsextensionjavascriptpreprocessingfile.md)
  The name of a JavaScript file supplied by a Share or Action extension.
### Core Spotlight
- [CSSupportedContentTypes](information-property-list/nsextension/nsextensionattributes/cssupportedcontenttypes.md)
### Credential providers
- [ASCredentialProviderExtensionCapabilities](information-property-list/nsextension/nsextensionattributes/ascredentialproviderextensioncapabilities.md)
  The credential types supported by a credential provider extension, and whether it presents a user interface.
### Intents
- [IntentsSupported](information-property-list/nsextension/intentssupported.md)
  The names of the intents that an extension supports.
- [SupportedMediaCategories](information-property-list/nsextension/nsextensionattributes/supportedmediacategories.md)
  Types of media supported by an app extension’s media-playing intents.
### Mail
- [MEComposeSession](information-property-list/nsextension/nsextensionattributes/mecomposesession.md)
- [MEExtensionCapabilities](information-property-list/nsextension/nsextensionattributes/meextensioncapabilities.md)
### Photos
- [PHProjectExtensionDefinesProjectTypes](information-property-list/nsextension/nsextensionattributes/phprojectextensiondefinesprojecttypes.md)
  A Boolean value indicating whether the Photos app gets a list of supported project types from an extension.
- [PHSupportedMediaTypes](information-property-list/nsextension/nsextensionattributes/phsupportedmediatypes.md)
  The types of assets a Photo Editing extension can edit.
### Quick Actions
- [NSExtensionServiceAllowsFinderPreviewItem](information-property-list/nsextension/nsextensionattributes/nsextensionserviceallowsfinderpreviewitem.md)
  A Boolean value indicating whether the extension appears in the Finder Preview pane and Quick Actions menu.
- [NSExtensionServiceFinderPreviewIconName](information-property-list/nsextension/nsextensionattributes/nsextensionservicefinderpreviewiconname.md)
  The name of an icon for display when the extension appears in the Finder Preview pane and Quick Actions menu.
- [NSExtensionServiceFinderPreviewLabel](information-property-list/nsextension/nsextensionattributes/nsextensionservicefinderpreviewlabel.md)
  A name for display when the extension appears in the Finder Preview pane and Quick Actions menu.
- [NSExtensionServiceRoleType](information-property-list/nsextension/nsextensionattributes/nsextensionserviceroletype.md)
  The type of task an Action extension performs.
### Toolbar
- [NSExtensionServiceAllowsToolbarItem](information-property-list/nsextension/nsextensionattributes/nsextensionserviceallowstoolbaritem.md)
  A Boolean value indicating whether an Action extension displays an item in a window’s toolbar.
- [NSExtensionServiceToolbarIconFile](information-property-list/nsextension/nsextensionattributes/nsextensionservicetoolbariconfile.md)
  The image for an Action extension’s toolbar item.
- [NSExtensionServiceToolbarPaletteLabel](information-property-list/nsextension/nsextensionattributes/nsextensionservicetoolbarpalettelabel.md)
  The label for an Action extension’s toolbar item.
### Touch Bar
- [NSExtensionServiceAllowsTouchBarItem](information-property-list/nsextension/nsextensionattributes/nsextensionserviceallowstouchbaritem.md)
  A Boolean value indicating whether the extension appears as a Quick Action in the Touch Bar.
- [NSExtensionServiceTouchBarBezelColorName](information-property-list/nsextension/nsextensionattributes/nsextensionservicetouchbarbezelcolorname.md)
  The color to use for the bezel around the extension when it appears as a Quick Action in the Touch Bar.
- [NSExtensionServiceTouchBarIconName](information-property-list/nsextension/nsextensionattributes/nsextensionservicetouchbariconname.md)
  The name of an icon for display when the extension appears as a Quick Action in the Touch Bar
- [NSExtensionServiceTouchBarLabel](information-property-list/nsextension/nsextensionattributes/nsextensionservicetouchbarlabel.md)
  A name for display when the extension appears as a Quick Action in the Touch Bar.
### UIKit
- [IDMessageFilterExtensionNetworkURL](information-property-list/nsextension/nsextensionattributes/idmessagefilterextensionnetworkurl.md)
  The server that a Message Filter app extension may defer a query to.
- [ILClassificationExtensionSMSReportDestination](information-property-list/nsextension/nsextensionattributes/ilclassificationextensionsmsreportdestination.md)
  The phone number that receives SMS messages when the user reports an SMS message or a call.
- [IsASCIICapable](information-property-list/nsextension/nsextensionattributes/isasciicapable.md)
  A Boolean value indicating whether a custom keyboard displays standard ASCII characters.
- [MSMessagesAppPresentationContextMessages](information-property-list/nsextension/nsextensionattributes/msmessagesapppresentationcontextmessages.md)
  The contexts that an iMessage app or sticker pack supports.
- [PrefersRightToLeft](information-property-list/nsextension/nsextensionattributes/prefersrighttoleft.md)
  A Boolean value indicating whether a keyboard extension supports right-to-left languages.
- [PrimaryLanguage](information-property-list/nsextension/nsextensionattributes/primarylanguage.md)
  The primary language for a keyboard extension.
- [RequestsOpenAccess](information-property-list/nsextension/nsextensionattributes/requestsopenaccess.md)
  A Boolean value indicating whether a custom keyboard uses a shared container and accesses the network.
- [UIDocumentPickerModes](information-property-list/nsextension/nsextensionattributes/uidocumentpickermodes.md)
  The modes that a Document Picker extension supports.
- [UIDocumentPickerSupportedFileTypes](information-property-list/nsextension/nsextensionattributes/uidocumentpickersupportedfiletypes.md)
  The Uniform Type Identifiers that a document picker extension supports.
- [UNNotificationExtensionCategory](information-property-list/nsextension/nsextensionattributes/unnotificationextensioncategory.md)
  The identifier of a category declared by the app extension.
- [UNNotificationExtensionDefaultContentHidden](information-property-list/nsextension/nsextensionattributes/unnotificationextensiondefaultcontenthidden.md)
  A Boolean value indicating whether only the app extension’s custom view controller is displayed in the notification interface.
- [UNNotificationExtensionInitialContentSizeRatio](information-property-list/nsextension/nsextensionattributes/unnotificationextensioninitialcontentsizeratio.md)
  The initial size of the view controller’s view for an app extension, expressed as a ratio of its height to its width.
- [UNNotificationExtensionOverridesDefaultTitle](information-property-list/nsextension/nsextensionattributes/unnotificationextensionoverridesdefaulttitle.md)
  A Boolean value indicating whether the title of the app extension’s view controller is used as the title of the notification.
- [UNNotificationExtensionUserInteractionEnabled](information-property-list/nsextension/nsextensionattributes/unnotificationextensionuserinteractionenabled.md)
  A Boolean value indicating whether user interactions in a custom notification are enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/nsextensionattributes)*