# init(stringValue:)

**Framework**: Photos  
**Kind**: init  
**Role**: Initializer

Deserializes a cloud identifier from its string value.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.0+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 13.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use initWithArchivalStringValue: instead

## Declaration

```swift
init(stringValue: String)
```

```objc
- (instancetype) initWithStringValue:(NSString *) stringValue;
```

## See Also

### Using Cloud Identifiers
- [var stringValue: String](./stringvalue.md)
  A string version of the cloud identifier to use in serialization.
- [class var notFound: PHCloudIdentifier](./notfound.md)
  The global identifier used in an array slot for items that couldn’t be found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcloudidentifier/init(stringvalue:))*