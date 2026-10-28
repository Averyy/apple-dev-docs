# registeredTypeIdentifiers(fileOptions:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an array with a subset of type identifiers for the item provider, according to the specified file options, in the same order they were registered.

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
func registeredTypeIdentifiers(fileOptions: NSItemProviderFileOptions = []) -> [String]
```

```objc
- (NSArray<NSString *> *) registeredTypeIdentifiersWithFileOptions:(NSItemProviderFileOptions) fileOptions;
```

## Return Value

An array of type identifier strings.

## Discussion

To access the array of all registered UTIs, pass the value `0` in the `fileOptions` parameter.

## Parameters

- `fileOptions`: An array of [`NSItemProviderFileOptions`](../nsitemproviderfileoptions.md).

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
- [var registeredTypeIdentifiers: [String]](./registeredtypeidentifiers.md)
  Returns the array of type identifiers for the item provider, in the same order they were registered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registeredtypeidentifiers(fileoptions:))*