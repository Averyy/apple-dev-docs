# registeredContentTypes(conformingTo:)

**Framework**: Foundation  
**Kind**: method

Returns an array of registered content types that conform to a specified content type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func registeredContentTypes(conformingTo contentType: UTType) -> [UTType]
```

#### Return Value

An array of registered content types.

## Parameters

- `contentType`: The specified content type.

## See Also

- [var registeredContentTypes: [UTType]](nsitemprovider/registeredcontenttypes.md)
  Registered content types in the order the app registers each type.
- [var registeredContentTypesForOpenInPlace: [UTType]](nsitemprovider/registeredcontenttypesforopeninplace.md)
  Registered content types that the system can load as open-in-place files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registeredcontenttypes(conformingto:))*