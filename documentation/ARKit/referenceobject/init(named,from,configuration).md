# init(named:from:configuration:)

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Initializes a reference object from a bundle, with reference object configuration.

**Availability**:
- visionOS 27.0+

## Declaration

```swift
init(named: String, from bundle: Bundle? = nil, configuration: ReferenceObject.Configuration) async throws
```

#### Discussion

> **Throws**: `ObjectTrackingProvider.Error`

## Parameters

- `named`: Name of object to load in bundle.
- `bundle`: Bundle to load from. The main Bundle is used if unspecified.
- `configuration`: Configuration to use for tracking this object.

## See Also

### Creating reference objects
- [init(from: URL) async throws](./init%28from%29.md)
  Creates a reference object from a URL you provide.
- [init(named: String, from: Bundle?) async throws](./init%28named,from%29.md)
  Creates a reference object from a bundle.
- [init(from: URL, configuration: ReferenceObject.Configuration) async throws](./init%28from,configuration%29.md)
  Initializes a reference object from a URL, with reference object configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/referenceobject/init(named:from:configuration:))*