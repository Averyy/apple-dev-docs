# notFound

**Framework**: Photos  
**Kind**: property  
**Role**: Type Property

The global identifier used in an array slot for items that couldn’t be found.

**Availability**:
- macOS 10.13+ - Deprecated in 12.0

> **Deprecated**: Check for PHPhotosErrorIdentifierNotFound in PHCloudIdentifierMapping.error

## Declaration

```swift
class var notFound: PHCloudIdentifier { get }
```

```objc
@property (class, nonatomic, readonly) PHCloudIdentifier * notFoundIdentifier;
```

## See Also

### Using Cloud Identifiers
- [init(stringValue: String)](./init%28stringvalue%29.md)
  Deserializes a cloud identifier from its string value.
- [var stringValue: String](./stringvalue.md)
  A string version of the cloud identifier to use in serialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcloudidentifier/notfound)*