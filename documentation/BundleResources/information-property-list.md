# Information Property List

**Framework**: Bundle Resources  
**Kind**: struct

A resource containing key-value pairs that identify and configure a bundle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Mentions

- [Placing content in a bundle](placing-content-in-a-bundle.md)

#### Discussion

Bundles, which represent executables of different kinds, contain an information property list file. This collection of key-value pairs specifies how the system should interpret the associated bundle. Some key-value pairs characterize the bundle itself, while others configure the app, framework, or other entity that the bundle represents. Some keys are required, while others are specific to particular features of the executable.

The information property list file always has the name `Info.plist`. The file name is case-sensitive and must begin with a capital letter `I`. Its location within the bundle depends on both the bundle type and the platform. For example, iOS app bundles store the file in the bundle’s root directory, whereas macOS app bundles place the `Info.plist` file in the `Contents` directory.

To access an information property list, you use an instance of the [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) class, which represents a bundle on disk. You can get the value for a few common keys by accessing properties of the bundle instance. For example, the [`bundleIdentifier`](https://developer.apple.com/documentation/Foundation/Bundle/bundleIdentifier) property contains the value associated with the [`CFBundleIdentifier`](information-property-list/cfbundleidentifier.md) key. You can obtain the value for an arbitrary key using the [`object(forInfoDictionaryKey:)`](https://developer.apple.com/documentation/Foundation/Bundle/object(forInfoDictionaryKey:)) method.

To create an information property list for a bundle, you typically rely on Xcode to prepare the file for your apps and other executable targets, as described in [`Managing Your App’s Information Property List`](managing-your-app-s-information-property-list.md).

## Topics

### Essentials
- [Managing Your App’s Information Property List](managing-your-app-s-information-property-list.md)
  Create and customize an information property list file for your app using Xcode.
### Core settings
- [Bundle configuration](bundle-configuration.md)
  Define basic characteristics of a bundle, like its name, type, and version.
- [User interface](user-interface.md)
  Configure an app’s scenes, storyboards, icons, fonts, and other user interface elements.
- [App execution](app-execution.md)
  Control app launch, execution, and termination.
### Services
- [Protected resources](protected-resources.md)
  Control an app’s access to protected system services and user data.
- [Data and storage](data-and-storage.md)
  Regulate documents, URLs, and other kinds of data movement and storage.
- [App services](app-services.md)
  Configure services provided by the app, like support for giving directions or using game controllers.
- [Kernel and drivers](kernel-and-drivers.md)
  Configure device drivers provided by the app.
### AVFoundation
- [NSAlwaysAllowMicrophoneModeControl](information-property-list/nsalwaysallowmicrophonemodecontrol.md)
  A Boolean value that indicates if a person can configure a microphone mode regardless of whether the microphone is in an active state.
### BrowserEngineKit
- [BEEmbeddedWebBrowserEngine](information-property-list/beembeddedwebbrowserengine.md)
- [BEEmbeddedWebBrowserEngineVersion](information-property-list/beembeddedwebbrowserengineversion.md)
### Dictionaries
- [IOParentMatch](information-property-list/ioparentmatch.md)
- [IOPropertyMatch](information-property-list/iopropertymatch.md)
  The device-specific keys the system must match in order to use your driver.
- [NSPinnedCAIdentities](information-property-list/nspinnedcaidentities.md)
  A list of allowed Certificate Authority certificates for a given domain name.
- [NSPinnedLeafIdentities](information-property-list/nspinnedleafidentities.md)
  A list of allowed leaf certificates for a given domain name.
### Type Aliases
- [IOClass](information-property-list/ioclass.md)
  The name of the class to instantiate from your driver.
- [IOMatchCategory](information-property-list/iomatchcategory.md)
- [IONameMatch](information-property-list/ionamematch.md)
  One or more strings that contain the names of possible provider objects in the system registry.
- [IOPathMatch](information-property-list/iopathmatch.md)
- [IOProviderClass](information-property-list/ioproviderclass.md)
  The name of the class that your driver expects to provide the implementation for its provider object.
- [IOResourceMatch](information-property-list/ioresourcematch.md)
  One or more system-specific or device-specific resources that your driver requires.
- [IOUserClass](information-property-list/iouserclass.md)
  The name of your driver’s main class, which is the entry point for interacting with your driver’s code.
- [IOUserClientClass](information-property-list/iouserclientclass.md)
  The name of the class to instantiate when the system requires a client connection to the driver.
- [IOUserServerName](information-property-list/iouserservername.md)
  The name that the system uses to facilitate communication between your driver and other clients.
- [NSCriticalMessagingUsageDescription](information-property-list/nscriticalmessagingusagedescription.md)
- [NSExceptionAllowsInsecureHTTPLoads](information-property-list/nsexceptionallowsinsecurehttploads.md)
  A Boolean value indicating whether to allow insecure HTTP loads.
- [NSExceptionMinimumTLSVersion](information-property-list/nsexceptionminimumtlsversion.md)
  The minimum Transport Layer Security (TLS) version for network connections.
- [NSExceptionRequiresForwardSecrecy](information-property-list/nsexceptionrequiresforwardsecrecy.md)
  A Boolean value indicating whether to override the perfect forward secrecy requirement.
- [NSIncludesSubdomains](information-property-list/nsincludessubdomains.md)
  A Boolean value that indicates whether to extend the configuration to subdomains of the given domain.
- [NSRequiresCertificateTransparency](information-property-list/nsrequirescertificatetransparency.md)
  An obsolete Boolean value indicating whether to require Certificate Transparency.
- [OSAScriptingDefinition](information-property-list/osascriptingdefinition.md)
- [ProvidesOneTimeCodes](information-property-list/providesonetimecodes.md)
  Allows this credential provider to show up in one-time-code text fields, to allowing filling time-based verification codes.
- [ProvidesTextToInsert](information-property-list/providestexttoinsert.md)
  Allows this credential provider to show up in the system AutoFill context menu, so that it can fill text in any text field.
- [SupportsConditionalPasskeyRegistration](information-property-list/supportsconditionalpasskeyregistration.md)
  Indicates that the credential provider supports automatic passkey upgrades.

## See Also

- [Entitlements](entitlements.md)
  Key-value pairs that grant an executable permission to use a service or technology.
- [Privacy manifest files](privacy-manifest-files.md)
  Describe the data your app or third-party SDK collects and the reasons required APIs it uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list)*