# init(referenceImages:)

**Framework**: ARKit  
**Kind**: init

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

- [static var isSupported: Bool](imagetrackingprovider/issupported.md)
  A Boolean value that indicates whether the current runtime environment supports image-tracking providers.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](imagetrackingprovider/requiredauthorizations.md)
  The types of authorizations necessary for tracking images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/imagetrackingprovider/init(referenceimages:))*