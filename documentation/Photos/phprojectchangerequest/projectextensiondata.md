# projectExtensionData

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

Compressed project-specific data to use in the change request.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var projectExtensionData: Data { get set }
```

```objc
@property (nonatomic, copy, readwrite) NSData * projectExtensionData;
```

#### Discussion

The total size of stored data is limited to 5 MB; attempting to store more data will result in an error. Don’t include rasterized images that can be locally cached. Limit stored data to compressed project-specific data.

## See Also

### Creating Change Requests
- [init(project: PHProject)](./init%28project%29.md)
  Creates a change request around the specified project.
- [var title: String](./title.md)
  The title of the change request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phprojectchangerequest/projectextensiondata)*