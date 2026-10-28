# init(identifier:request:applicationGroupIdentifier:)

**Framework**: Background Assets  
**Kind**: init  
**Role**: Initializer

Creates a download that uses the specified identifier and App Group.

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3

## Declaration

```swift
convenience init(identifier: String, request: URLRequest, applicationGroupIdentifier: String)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier request:(NSURLRequest *) request applicationGroupIdentifier:(NSString *) applicationGroupIdentifier;
```

## Discussion

The system requires that all URL requests use Hypertext Transfer Protocol Secure (HTTPS). The [`priority`](../badownload/priority-swift.property.md) of the created download is [`default`](../badownload/priority-swift.struct/default.md).

## Parameters

- `identifier`: An app-specific string that uniquely identifies the downloadable asset.
- `request`: A URL request that provides request-specific information, such as URL, request type, and body data.
- `applicationGroupIdentifier`: The identifier of the App Group where the system stores finished downloads. For more information about App Groups, see [Configuring app groups](../../Xcode/configuring-app-groups.md).

## See Also

### Creating a download
- [init(identifier: String, request: URLRequest, essential: Bool, fileSize: Int, applicationGroupIdentifier: String, priority: BADownload.Priority)](./init%28identifier,request,essential,filesize,applicationgroupidentifier,priority%29.md)
- [convenience init(identifier: String, request: URLRequest, fileSize: Int, applicationGroupIdentifier: String)](./init%28identifier,request,filesize,applicationgroupidentifier%29.md)
- [convenience init(identifier: String, request: URLRequest, applicationGroupIdentifier: String, priority: BADownload.Priority)](./init%28identifier,request,applicationgroupidentifier,priority%29.md)
  Creates a prioritized download that uses the specified identifier and App Group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baurldownload/init(identifier:request:applicationgroupidentifier:))*