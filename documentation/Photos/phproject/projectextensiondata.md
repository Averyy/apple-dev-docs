# projectExtensionData

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

Data associated with the project extension.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var projectExtensionData: Data { get }
```

```objc
@property (nonatomic, readonly) NSData * projectExtensionData;
```

## Discussion

The total size of stored data is limited to 5 MB; attempting to store more data will result in an error. Don’t include rasterized images that can be locally cached. Limit stored data to compressed project-specific data.

## See Also

### Project Extension Properties
- [var hasProjectPreview: Bool](./hasprojectpreview.md)
  A property that indicates whether a project preview was previously set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phproject/projectextensiondata)*