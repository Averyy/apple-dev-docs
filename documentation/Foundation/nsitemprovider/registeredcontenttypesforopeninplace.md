# registeredContentTypesForOpenInPlace

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Registered content types that the system can load as open-in-place files.

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
var registeredContentTypesForOpenInPlace: [UTType] { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSArray<UTType *> * registeredContentTypesForOpenInPlace;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSArray<UTType *> * registeredContentTypesForOpenInPlace;
```

## See Also

### Registering content types
- [var registeredContentTypes: [UTType]](./registeredcontenttypes.md)
  Registered content types in the order the app registers each type.
- [func registeredContentTypes(conformingTo: UTType) -> [UTType]](./registeredcontenttypes%28conformingto%29.md)
  Returns an array of registered content types that conform to a specified content type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registeredcontenttypesforopeninplace)*