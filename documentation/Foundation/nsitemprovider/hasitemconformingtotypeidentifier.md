# hasItemConformingToTypeIdentifier(_:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier file options parameter with a value of zero.

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
func hasItemConformingToTypeIdentifier(_ typeIdentifier: String) -> Bool
```

## Parameters

- `typeIdentifier`: A string that represents the desired UTI.

## See Also

- [func canLoadObject(ofClass: any NSItemProviderReading.Type) -> Bool](nsitemprovider/canloadobject(ofclass:)-3eig9.md)
  Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [func canLoadObject<T>(ofClass: T.Type) -> Bool](nsitemprovider/canloadobject(ofclass:)-40grc.md)
  Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [func hasRepresentationConforming(toTypeIdentifier: String, fileOptions: NSItemProviderFileOptions) -> Bool](nsitemprovider/hasrepresentationconforming(totypeidentifier:fileoptions:).md)
  Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier and to specified open-in-place behavior.
- [var registeredTypeIdentifiers: [String]](nsitemprovider/registeredtypeidentifiers.md)
  Returns the array of type identifiers for the item provider, in the same order they were registered.
- [func registeredTypeIdentifiers(fileOptions: NSItemProviderFileOptions) -> [String]](nsitemprovider/registeredtypeidentifiers(fileoptions:).md)
  Returns an array with a subset of type identifiers for the item provider, according to the specified file options, in the same order they were registered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/hasitemconformingtotypeidentifier(_:))*