# requiredAuthorizations

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

The types of authorizations necessary for tracking images.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static var requiredAuthorizations: [ARKitSession.AuthorizationType] { get }
```

## See Also

### Creating an image-tracking provider
- [init(referenceImages: [ReferenceImage])](./init%28referenceimages%29.md)
  Creates an image-tracking provider that tracks the reference images you supply.
- [static var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the current runtime environment supports image-tracking providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/imagetrackingprovider/requiredauthorizations)*