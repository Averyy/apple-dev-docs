# init(identifier:request:applicationGroupIdentifier:)

**Framework**: Background Assets  
**Kind**: init

Creates a download that uses the specified identifier and App Group.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+

## Declaration

```swift
convenience init(identifier: String, request: URLRequest, applicationGroupIdentifier: String)
```

#### Discussion

The system requires that all URL requests use Hypertext Transfer Protocol Secure (HTTPS). The [`priority`](badownload/priority-swift.property.md) of the created download is [`default`](badownload/priority-swift.struct/default.md).

## Parameters

- `identifier`: An app-specific string that uniquely identifies the downloadable asset.
- `request`: A URL request that provides request-specific information, such as URL, request type, and body data.
- `applicationGroupIdentifier`: The identifier of the App Group where the system stores finished downloads. For more information about App Groups, see  .

## See Also

- [init(identifier: String, request: URLRequest, essential: Bool, fileSize: Int, applicationGroupIdentifier: String, priority: BADownload.Priority)](baurldownload/init(identifier:request:essential:filesize:applicationgroupidentifier:priority:).md)
- [convenience init(identifier: String, request: URLRequest, fileSize: Int, applicationGroupIdentifier: String)](baurldownload/init(identifier:request:filesize:applicationgroupidentifier:).md)
- [convenience init(identifier: String, request: URLRequest, applicationGroupIdentifier: String, priority: BADownload.Priority)](baurldownload/init(identifier:request:applicationgroupidentifier:priority:).md)
  Creates a prioritized download that uses the specified identifier and App Group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baurldownload/init(identifier:request:applicationgroupidentifier:))*