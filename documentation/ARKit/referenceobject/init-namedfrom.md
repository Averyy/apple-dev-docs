# init(named:from:)

**Framework**: ARKit  
**Kind**: init

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

- [init(from: URL) async throws](referenceobject/init(from:).md)
  Creates a reference object from a URL you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/referenceobject/init(named:from:))*