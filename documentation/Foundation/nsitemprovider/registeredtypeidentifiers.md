# registeredTypeIdentifiers

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the array of type identifiers for the item provider, in the same order they were registered.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var registeredTypeIdentifiers: [String] { get }
```

```objc
@property (atomic, copy, readonly) NSArray<NSString *> * registeredTypeIdentifiers;
```

## See Also

### Querying the provider’s contents
- [func canLoadObject(ofClass: any NSItemProviderReading.Type) -> Bool](./canloadobject%28ofclass%29-3eig9.md)
  Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [func canLoadObject<T>(ofClass: T.Type) -> Bool](./canloadobject%28ofclass%29-40grc.md)
  Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [func hasItemConformingToTypeIdentifier(String) -> Bool](./hasitemconformingtotypeidentifier%28_%29.md)
  Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier file options parameter with a value of zero.
- [func hasRepresentationConforming(toTypeIdentifier: String, fileOptions: NSItemProviderFileOptions) -> Bool](./hasrepresentationconforming%28totypeidentifier,fileoptions%29.md)
  Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier and to specified open-in-place behavior.
- [func registeredTypeIdentifiers(fileOptions: NSItemProviderFileOptions) -> [String]](./registeredtypeidentifiers%28fileoptions%29.md)
  Returns an array with a subset of type identifiers for the item provider, according to the specified file options, in the same order they were registered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registeredtypeidentifiers)*