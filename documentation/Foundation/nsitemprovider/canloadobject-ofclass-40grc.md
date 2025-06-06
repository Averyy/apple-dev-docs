# canLoadObject(ofClass:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value indicating whether an item provider can load objects of a specified class.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func canLoadObject<T>(ofClass: T.Type) -> Bool where T : _ObjectiveCBridgeable, T._ObjectiveCType : NSItemProviderReading
```

## Parameters

- `ofClass`: The object class for comparison.

## See Also

- [func canLoadObject(ofClass: any NSItemProviderReading.Type) -> Bool](nsitemprovider/canloadobject(ofclass:)-3eig9.md)
  Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [func hasItemConformingToTypeIdentifier(String) -> Bool](nsitemprovider/hasitemconformingtotypeidentifier(_:).md)
  Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier file options parameter with a value of zero.
- [func hasRepresentationConforming(toTypeIdentifier: String, fileOptions: NSItemProviderFileOptions) -> Bool](nsitemprovider/hasrepresentationconforming(totypeidentifier:fileoptions:).md)
  Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier and to specified open-in-place behavior.
- [var registeredTypeIdentifiers: [String]](nsitemprovider/registeredtypeidentifiers.md)
  Returns the array of type identifiers for the item provider, in the same order they were registered.
- [func registeredTypeIdentifiers(fileOptions: NSItemProviderFileOptions) -> [String]](nsitemprovider/registeredtypeidentifiers(fileoptions:).md)
  Returns an array with a subset of type identifiers for the item provider, according to the specified file options, in the same order they were registered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/canloadobject(ofclass:)-40grc)*