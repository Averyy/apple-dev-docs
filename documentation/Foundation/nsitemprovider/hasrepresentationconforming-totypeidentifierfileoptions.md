# hasRepresentationConforming(toTypeIdentifier:fileOptions:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier and to specified open-in-place behavior.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func hasRepresentationConforming(toTypeIdentifier typeIdentifier: String, fileOptions: NSItemProviderFileOptions = []) -> Bool
```

#### Discussion

To check all registered UTIs for type conformance, pass the value `0` in the `fileOptions` parameter.

## See Also

- [func canLoadObject(ofClass: any NSItemProviderReading.Type) -> Bool](nsitemprovider/canloadobject(ofclass:)-3eig9.md)
  Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [func canLoadObject<T>(ofClass: T.Type) -> Bool](nsitemprovider/canloadobject(ofclass:)-40grc.md)
  Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [func hasItemConformingToTypeIdentifier(String) -> Bool](nsitemprovider/hasitemconformingtotypeidentifier(_:).md)
  Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier file options parameter with a value of zero.
- [var registeredTypeIdentifiers: [String]](nsitemprovider/registeredtypeidentifiers.md)
  Returns the array of type identifiers for the item provider, in the same order they were registered.
- [func registeredTypeIdentifiers(fileOptions: NSItemProviderFileOptions) -> [String]](nsitemprovider/registeredtypeidentifiers(fileoptions:).md)
  Returns an array with a subset of type identifiers for the item provider, according to the specified file options, in the same order they were registered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/hasrepresentationconforming(totypeidentifier:fileoptions:))*