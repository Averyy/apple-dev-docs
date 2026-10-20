# init(from:)

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Creates a reference object from a URL you provide.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
init(from url: URL) async throws
```

## Parameters

- `url`: Local path to the reference object model.

## See Also

### Creating reference objects
- [init(named: String, from: Bundle?) async throws](./init%28named,from%29.md)
  Creates a reference object from a bundle.
- [init(from: URL, configuration: ReferenceObject.Configuration) async throws](./init%28from,configuration%29.md)
  Initializes a reference object from a URL, with reference object configuration.
- [init(named: String, from: Bundle?, configuration: ReferenceObject.Configuration) async throws](./init%28named,from,configuration%29.md)
  Initializes a reference object from a bundle, with reference object configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/referenceobject/init(from:))*