# NSFileProviderDomainVersion

**Framework**: File Provider  
**Kind**: class

An opaque object that identifies a specific version of a domain.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class NSFileProviderDomainVersion
```

#### Overview

The file provider extension is responsible for assigning and updating the domain version. To specify the domain version, adopt the [`NSFileProviderDomainState`](nsfileproviderdomainstate.md) protocol. The system then calls your extension’s [`domainVersion`](nsfileproviderdomainstate/domainversion.md) method to read the current version.

The system reads the domain version after you call:

- The [`createItem(basedOn:fields:contents:options:request:completionHandler:)`](nsfileproviderreplicatedextension/createitem(basedon:fields:contents:options:request:completionhandler:).md) completion handler
- The [`modifyItem(_:baseVersion:changedFields:contents:options:request:completionHandler:)`](nsfileproviderreplicatedextension/modifyitem(_:baseversion:changedfields:contents:options:request:completionhandler:).md) completion handler
- The [`deleteItem(identifier:baseVersion:options:request:completionHandler:)`](nsfileproviderreplicatedextension/deleteitem(identifier:baseversion:options:request:completionhandler:).md) completion handler
- The [`item(for:request:completionHandler:)`](nsfileproviderreplicatedextension/item(for:request:completionhandler:).md) completion handler
- The [`finishEnumerating(upTo:)`](nsfileproviderenumerationobserver/finishenumerating(upto:).md) or [`finishEnumeratingWithError(_:)`](nsfileproviderenumerationobserver/finishenumeratingwitherror(_:).md) method when enumerating the materialized set.

The system always reads the domain version on the same dispatch queue as the completion handler.

Your extension defines when the domain version changes. When you update the version, call the [`signalEnumerator(for:completionHandler:)`](nsfileprovidermanager/signalenumerator(for:completionhandler:).md) and passing the [`workingSet`](nsfileprovideritemidentifier/workingset.md) constant as the `containerItemIdentifier` property. This notifies the system of the update. The system ignores any lower versions.

When the system discovers a change on disk, it associates that change with the current domain version. It then includes the version in the [`NSFileProviderRequest`](nsfileproviderrequest.md) object passed to the file provider extension.

Only file provider extensions based on the [`NSFileProviderReplicatedExtension`](nsfileproviderreplicatedextension.md) use instances of this class. Each version object is immutable. You can use them as keys in a dictionary.

## Topics

### Creating Versions
- [func next() -> NSFileProviderDomainVersion](nsfileproviderdomainversion/next.md)
  Creates a new version that supersedes the current version.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [protocol NSFileProviderDomainState](nsfileproviderdomainstate.md)
  An object that contains global state data about the domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomainversion)*