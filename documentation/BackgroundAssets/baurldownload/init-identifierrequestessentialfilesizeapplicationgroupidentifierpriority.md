# init(identifier:request:essential:fileSize:applicationGroupIdentifier:priority:)

**Framework**: Background Assets  
**Kind**: init

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
init(identifier: String, request: URLRequest, essential: Bool, fileSize: Int, applicationGroupIdentifier: String, priority: BADownload.Priority)
```

## See Also

- [convenience init(identifier: String, request: URLRequest, fileSize: Int, applicationGroupIdentifier: String)](baurldownload/init(identifier:request:filesize:applicationgroupidentifier:).md)
- [convenience init(identifier: String, request: URLRequest, applicationGroupIdentifier: String)](baurldownload/init(identifier:request:applicationgroupidentifier:).md)
  Creates a download that uses the specified identifier and App Group.
- [convenience init(identifier: String, request: URLRequest, applicationGroupIdentifier: String, priority: BADownload.Priority)](baurldownload/init(identifier:request:applicationgroupidentifier:priority:).md)
  Creates a prioritized download that uses the specified identifier and App Group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baurldownload/init(identifier:request:essential:filesize:applicationgroupidentifier:priority:))*