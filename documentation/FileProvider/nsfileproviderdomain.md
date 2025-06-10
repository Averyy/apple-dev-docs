# NSFileProviderDomain

**Framework**: File Provider  
**Kind**: class

A File Provider extension’s domain.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class NSFileProviderDomain
```

#### Overview

You can use domains to partition a file provider’s content. When you use domains, a single file provider can act as if multiple file providers were installed, and users can dynamically switch from one domain to another. You can use domains to represent different accounts or locations.

By default, a File Provider extension has no domain. You can register domains by calling the [`NSFileProviderManager`](nsfileprovidermanager.md) class’s [`add(_:completionHandler:)`](nsfileprovidermanager/add(_:completionhandler:).md) method. A new [`NSFileProviderExtension`](nsfileproviderextension.md) instance is created for each domain that you register. The [`NSFileProviderExtension`](nsfileproviderextension.md) object’s [`domain`](nsfileproviderextension/domain.md) property indicates which domain the file provider belongs to. Any items returned by that file provider also belong to the domain.

## Topics

### Creating domains
- [init(identifier: NSFileProviderDomainIdentifier, displayName: String, pathRelativeToDocumentStorage: String)](nsfileproviderdomain/init(identifier:displayname:pathrelativetodocumentstorage:).md)
  Returns a newly instantiated domain.
- [init(identifier: NSFileProviderDomainIdentifier, displayName: String)](nsfileproviderdomain/init(identifier:displayname:).md)
  Creates a new file provider domain with the specified identifier and display name.
- [struct NSFileProviderDomainIdentifier](nsfileproviderdomainidentifier.md)
  A unique identifier for a file provider’s domain.
- [init(displayName: String, userInfo: [AnyHashable : Any], volumeURL: URL?)](nsfileproviderdomain/init(displayname:userinfo:volumeurl:).md)
  Creates a new file provider domain with the specified URL and display name.
### Accessing data
- [var displayName: String](nsfileproviderdomain/displayname.md)
  The name of the domain displayed in the user interface.
- [var identifier: NSFileProviderDomainIdentifier](nsfileproviderdomain/identifier.md)
  The domain’s unique identifier.
- [var isReplicated: Bool](nsfileproviderdomain/isreplicated.md)
- [var backingStoreIdentity: Data?](nsfileproviderdomain/backingstoreidentity.md)
  A unique identifier for the backing store used by the system.
- [var pathRelativeToDocumentStorage: String](nsfileproviderdomain/pathrelativetodocumentstorage.md)
  The path of the domain’s subdirectory relative to the file provider’s shared container.
- [var isHidden: Bool](nsfileproviderdomain/ishidden.md)
  A Boolean value that determines whether the domain is visible to users.
- [var userEnabled: Bool](nsfileproviderdomain/userenabled.md)
  A Boolean value that indicates whether the user has enabled or disabled the domain.
- [var isDisconnected: Bool](nsfileproviderdomain/isdisconnected.md)
  A Boolean value indicating that the domain is present, but disconnected from the file extension.
- [var supportsSyncingTrash: Bool](nsfileproviderdomain/supportssyncingtrash.md)
- [var userInfo: [AnyHashable : Any]?](nsfileproviderdomain/userinfo.md)
- [var volumeUUID: UUID?](nsfileproviderdomain/volumeuuid.md)
### Syncing Desktop and Documents folders
- [var replicatedKnownFolders: NSFileProviderKnownFolders](nsfileproviderdomain/replicatedknownfolders.md)
  A list of known folders that the domain currently replicates.
- [var supportedKnownFolders: NSFileProviderKnownFolders](nsfileproviderdomain/supportedknownfolders.md)
  A list of known folders that the domain can replicate.
- [struct NSFileProviderKnownFolders](nsfileproviderknownfolders.md)
  Constants that identify known folders.
### Supporting search
- [var supportsStringSearchRequest: Bool](nsfileproviderdomain/supportsstringsearchrequest.md)
  A Boolean value that indicates whether the provider supports search.
### Testing
- [var testingModes: NSFileProviderDomain.TestingModes](nsfileproviderdomain/testingmodes-swift.property.md)
  A mode that gives the File Provider extension more control over the system’s behavior during testing.
- [NSFileProviderDomain.TestingModes](nsfileproviderdomain/testingmodes-swift.struct.md)
  Modes that modify the system’s behavior while testing.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain)*