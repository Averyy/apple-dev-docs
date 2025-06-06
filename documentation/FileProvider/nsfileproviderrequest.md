# NSFileProviderRequest

**Framework**: File Provider  
**Kind**: class

An object that provides information about the application requesting data from the File Provider extension.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class NSFileProviderRequest
```

## Topics

### Accessing Application Information
- [var domainVersion: NSFileProviderDomainVersion?](nsfileproviderrequest/domainversion.md)
  The version of the domain for the request.
- [var requestingExecutable: URL?](nsfileproviderrequest/requestingexecutable.md)
  The URL of the requesting executable.
- [var isFileViewerRequest: Bool](nsfileproviderrequest/isfileviewerrequest.md)
  A Boolean value that indicates whether the request came from Finder or related system file browsers.
- [var isSystemRequest: Bool](nsfileproviderrequest/issystemrequest.md)
  A Boolean value that indicates whether the request came from a system process.

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

## See Also

- [struct NSFileProviderItemFields](nsfileprovideritemfields.md)
  Fields that specify which of the item’s properties have changed.
- [class NSFileProviderItemVersion](nsfileprovideritemversion.md)
  The version of the item’s content and its metadata.
- [protocol NSFileProviderItemDecorating](nsfileprovideritemdecorating.md)
  Support for decorating items.
- [struct NSFileProviderItemDecorationIdentifier](nsfileprovideritemdecorationidentifier.md)
  A decoration identifier defined in the File Provider extension’s information property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderrequest)*