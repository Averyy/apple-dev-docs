# NSExtension

**Framework**: Bundle Resources  
**Kind**: dictionary

The properties of an app extension.

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
### Attributes
- [NSExtensionAttributes](information-property-list/nsextension/nsextensionattributes.md)
  Properties of an app extension.
### Authentication
- [ASAccountAuthenticationModificationPasswordGenerationRequirements](information-property-list/nsextension/asaccountauthenticationmodificationpasswordgenerationrequirements.md)
  The rules the system satisfies when generating a strong password for your extension during an automatic upgrade.
- [ASAccountAuthenticationModificationSupportsStrongPasswordChange](information-property-list/nsextension/asaccountauthenticationmodificationsupportsstrongpasswordchange.md)
  A Boolean value that indicates whether the extension supports upgrading a user’s password to a strong password.
- [ASAccountAuthenticationModificationSupportsUpgradeToSignInWithApple](information-property-list/nsextension/asaccountauthenticationmodificationsupportsupgradetosigninwithapple.md)
  A Boolean value that indicates whether the extension supports upgrading from using password authentication to using Sign in with Apple.
### File Provider
- [NSExtensionFileProviderActions](information-property-list/nsextension/nsextensionfileprovideractions.md)
  The custom actions for a File Provider extension.
- [NSExtensionFileProviderDocumentGroup](information-property-list/nsextension/nsextensionfileproviderdocumentgroup.md)
  The identifier of a shared container that can be accessed by a Document Picker extension and its associated File Provider extension.
- [NSExtensionFileProviderSupportsEnumeration](information-property-list/nsextension/nsextensionfileprovidersupportsenumeration.md)
  A Boolean value that indicates whether a File Provider extension enumerates its content.
- [NSExtensionFileProviderDownloadPipelineDepth](information-property-list/nsextension/nsextensionfileproviderdownloadpipelinedepth.md)
  The per-domain limit of concurrent calls that a file provider extension can make to fetch data from remote storage.
- [NSExtensionFileProviderUploadPipelineDepth](information-property-list/nsextension/nsextensionfileprovideruploadpipelinedepth.md)
  The per-domain limit of concurrent calls that a file provider extension can make to upload data.
### Intents
- [IntentsSupported](information-property-list/nsextension/intentssupported.md)
  The names of the intents that an extension supports.
### Professional Video Applications
- [ProExtensionAttributes](information-property-list/nsextension/proextensionattributes.md)
  A dictionary that specifies the minimum size of the floating window in which Final Cut Pro hosts the extension view.
- [ProExtensionPrincipalClass](information-property-list/nsextension/proextensionprincipalclass.md)
  The name of the class with the principal implementation of your extension.
- [ProExtensionPrincipalViewControllerClass](information-property-list/nsextension/proextensionprincipalviewcontrollerclass.md)
  The name of the principal view controller class of your extension.
- [ProExtensionUUID](information-property-list/nsextension/proextensionuuid.md)
  A UUID string that uniquely identifies your extension to the Compressor app.
### SafariServices
- [SFSafariContentScript](information-property-list/nsextension/sfsafaricontentscript.md)
  The content scripts for a Safari extension.
- [SFSafariContextMenu](information-property-list/nsextension/sfsafaricontextmenu.md)
  The context menu items for a Safari extension.
- [SFSafariStyleSheet](information-property-list/nsextension/sfsafaristylesheet.md)
  The style sheet for a Safari extension.
- [SFSafariToolbarItem](information-property-list/nsextension/sfsafaritoolbaritem.md)
  The items to add to the toolbar for a Safari extension.
- [SFSafariWebsiteAccess](information-property-list/nsextension/sfsafariwebsiteaccess.md)
  The webpages a Safari extension can access.

## See Also

- [NSServices](information-property-list/nsservices.md)
  The services provided by an app.
- [WKExtensionDelegateClassName](information-property-list/wkextensiondelegateclassname.md)
  The name of your watchOS app’s extension delegate.
- [UIApplicationShortcutWidget](information-property-list/uiapplicationshortcutwidget.md)
  The bundle ID of the widget that’s available as a Home screen quick action in apps that have more than one widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension)*