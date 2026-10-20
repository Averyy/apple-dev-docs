# init(referenceImages:)

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Creates an image-tracking provider that tracks the reference images you supply.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
init(referenceImages: [ReferenceImage])
```

## Parameters

- `referenceImages`: An array of known images to track in a person’s surroundings.

## See Also

### Creating an image-tracking provider
- [static var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the current runtime environment supports image-tracking providers.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](./requiredauthorizations.md)
  The types of authorizations necessary for tracking images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/imagetrackingprovider/init(referenceimages:))*