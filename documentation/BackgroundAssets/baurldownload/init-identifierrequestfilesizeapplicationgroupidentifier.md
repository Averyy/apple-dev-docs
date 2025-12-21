# init(identifier:request:fileSize:applicationGroupIdentifier:)

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
convenience init(identifier: String, request: URLRequest, fileSize: Int, applicationGroupIdentifier: String)
```

#### Discussion

Constructs a download object to represent the download of a asset located inside of the provided @c request.

## Parameters

- `identifier`: A unique identifier that is used to track the download across the app and extension.
- `request`: The request used to perform the download. The URL provided inside of the request must be a https scheme.
- `fileSize`: The size of the file to download. This field must be accurate in order to show the user accurate progress during app installation.   If the size does not match the file being downloaded, then the download will fail.
- `applicationGroupIdentifier`: The identifier of the application group that should used to store the finished download.

## See Also

- [init(identifier: String, request: URLRequest, essential: Bool, fileSize: Int, applicationGroupIdentifier: String, priority: BADownload.Priority)](baurldownload/init(identifier:request:essential:filesize:applicationgroupidentifier:priority:).md)
- [convenience init(identifier: String, request: URLRequest, applicationGroupIdentifier: String)](baurldownload/init(identifier:request:applicationgroupidentifier:).md)
  Creates a download that uses the specified identifier and App Group.
- [convenience init(identifier: String, request: URLRequest, applicationGroupIdentifier: String, priority: BADownload.Priority)](baurldownload/init(identifier:request:applicationgroupidentifier:priority:).md)
  Creates a prioritized download that uses the specified identifier and App Group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baurldownload/init(identifier:request:filesize:applicationgroupidentifier:))*