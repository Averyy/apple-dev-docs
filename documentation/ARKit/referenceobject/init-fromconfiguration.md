# init(from:configuration:)

**Framework**: ARKit  
**Kind**: init

Initializes a reference object from a URL, with reference object configuration.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(from url: URL, configuration: ReferenceObject.Configuration) async throws
```

#### Discussion

> **Note**: `ObjectTrackingProvider.Error`

## Parameters

- `url`: Local path to the reference object model.
- `configuration`: Configuration to use for tracking this object.

## See Also

- [init(from: URL) async throws](referenceobject/init(from:).md)
  Creates a reference object from a URL you provide.
- [init(named: String, from: Bundle?) async throws](referenceobject/init(named:from:).md)
  Creates a reference object from a bundle.
- [init(named: String, from: Bundle?, configuration: ReferenceObject.Configuration) async throws](referenceobject/init(named:from:configuration:).md)
  Initializes a reference object from a bundle, with reference object configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/referenceobject/init(from:configuration:))*