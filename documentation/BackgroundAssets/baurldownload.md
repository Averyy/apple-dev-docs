# BAURLDownload

**Framework**: Background Assets  
**Kind**: class

An object that represents a remote asset to download.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
class BAURLDownload
```

## Topics

### Creating a download
- [init(identifier: String, request: URLRequest, essential: Bool, fileSize: Int, applicationGroupIdentifier: String, priority: BADownload.Priority)](baurldownload/init(identifier:request:essential:filesize:applicationgroupidentifier:priority:).md)
- [convenience init(identifier: String, request: URLRequest, fileSize: Int, applicationGroupIdentifier: String)](baurldownload/init(identifier:request:filesize:applicationgroupidentifier:).md)
- [convenience init(identifier: String, request: URLRequest, applicationGroupIdentifier: String)](baurldownload/init(identifier:request:applicationgroupidentifier:).md)
  Creates a download that uses the specified identifier and App Group.
- [convenience init(identifier: String, request: URLRequest, applicationGroupIdentifier: String, priority: BADownload.Priority)](baurldownload/init(identifier:request:applicationgroupidentifier:priority:).md)
  Creates a prioritized download that uses the specified identifier and App Group.

## Relationships

### Inherits From
- [BADownload](badownload.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class BADownload](badownload.md)
  An object that represents an in-progress or concluded asset download.
- [BADownload.Priority](badownload/priority-swift.struct.md)
  A type that determines the execution priority of a scheduled asset download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baurldownload)*