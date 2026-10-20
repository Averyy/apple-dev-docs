# init(named:from:)

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Creates a reference object from a bundle.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
init(named: String, from bundle: Bundle? = nil) async throws
```

## Parameters

- `named`: Name of object to load in bundle.
- `bundle`: Bundle to load from. If unspecified, defaults to the main bundle.

## See Also

### Creating reference objects
- [init(from: URL) async throws](./init%28from%29.md)
  Creates a reference object from a URL you provide.
- [init(from: URL, configuration: ReferenceObject.Configuration) async throws](./init%28from,configuration%29.md)
  Initializes a reference object from a URL, with reference object configuration.
- [init(named: String, from: Bundle?, configuration: ReferenceObject.Configuration) async throws](./init%28named,from,configuration%29.md)
  Initializes a reference object from a bundle, with reference object configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/referenceobject/init(named:from:))*