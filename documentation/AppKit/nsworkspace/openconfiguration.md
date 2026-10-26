# NSWorkspace.OpenConfiguration

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

The configuration options for opening URLs or launching apps.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class OpenConfiguration
```

```objc
@interface NSWorkspaceOpenConfiguration : NSObject
```

#### Overview

Create an [`NSWorkspace.OpenConfiguration`](./openconfiguration.md) object before launching an app or opening a URL using the shared [`NSWorkspace`](../nsworkspace.md) object. Use the properties of this object to customize the behavior of the launched app or the handling of the URLs. For example, you might tell the app to hide itself immediately after launch.

## Topics

### Handling URLs
- [var requiresUniversalLinks: Bool](./openconfiguration/requiresuniversallinks.md)
  A Boolean value indicating whether you require the URL to have an associated universal link.
- [var isForPrinting: Bool](./openconfiguration/isforprinting.md)
  A Boolean value indicating whether you want to print the contents of documents and URLs instead of opening them.
### Specifying app-related behaviors
- [var activates: Bool](./openconfiguration/activates.md)
  A Boolean value indicating whether the system activates the app and brings it to the foreground.
- [var addsToRecentItems: Bool](./openconfiguration/addstorecentitems.md)
  A Boolean value indicating whether to add the app or documents to the Recent Items menu.
- [var allowsRunningApplicationSubstitution: Bool](./openconfiguration/allowsrunningapplicationsubstitution.md)
  A Boolean value that indicates whether to use a running instance of an application even if it’s at a different URL.
- [var createsNewApplicationInstance: Bool](./openconfiguration/createsnewapplicationinstance.md)
  A Boolean value indicating whether you want the system to launch a new instance of the app.
- [var hides: Bool](./openconfiguration/hides.md)
  A Boolean value indicating whether you want the app to hide itself after it launches.
- [var hidesOthers: Bool](./openconfiguration/hidesothers.md)
  A Boolean value indicating whether you want to hide all apps except the one that launched.
### Prompting the user
- [var promptsUserIfNeeded: Bool](./openconfiguration/promptsuserifneeded.md)
  A Boolean value indicating whether to display errors, authentication requests, or other UI elements to the user.
### Specifying launch attributes
- [var appleEvent: NSAppleEventDescriptor?](./openconfiguration/appleevent.md)
  The first Apple event to send to the new app.
- [var arguments: [String]](./openconfiguration/arguments.md)
  The set of command-line arguments to pass to a new app instance at launch time.
- [var environment: [String : String]](./openconfiguration/environment.md)
  The set of environment variables to set in a new app instance.
- [var architecture: cpu_type_t](./openconfiguration/architecture.md)
  The architecture version of the app to launch.
### Creating a workspace configuration object
- [+ configuration](../nsworkspaceopenconfiguration/configuration.md)
  Creates and returns a new workspace configuration object containing default values.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Environment
- [class NSWorkspace](../nsworkspace.md)
  A workspace that can launch other apps and perform a variety of file-handling services.
- [struct NSAppKitVersion](../nsappkitversion.md)
  Constants for determining which version of AppKit is available.
- [LSMinimumSystemVersion](../../BundleResources/information-property-list/lsminimumsystemversion.md)
  The minimum version of the operating system required for the app to run in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openconfiguration)*