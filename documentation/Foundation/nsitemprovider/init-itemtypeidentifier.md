# init(item:typeIdentifier:)

**Framework**: Foundation  
**Kind**: init

Creates an item provider with an object, according to the item provider type coercion policy.

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
init(item: (any NSSecureCoding)?, typeIdentifier: String?)
```

#### Return Value

An item provider for the specified item.

#### Discussion

Use this method to initialize an item provider for objects in your app. The item provider registers your object with the specified type. Subsequent requests for that same type return the specified `item`.

## Parameters

- `item`: An object containing the data you want to provide. You may specify   for this parameter and register items and types later.
- `typeIdentifier`: A string that represents the UTI of the item. If   is not  , this parameter must not be  .

## See Also

- [convenience init?(contentsOf: URL!)](nsitemprovider/init(contentsof:).md)
  Provides data-backed content from an existing file.
- [convenience init(contentsOf: URL, contentType: UTType?, openInPlace: Bool, coordinated: Bool, visibility: NSItemProviderRepresentationVisibility)](nsitemprovider/init(contentsof:contenttype:openinplace:coordinated:visibility:).md)
  Provides data-backed content from an existing file with the specified parameters.
- [init()](nsitemprovider/init.md)
  Creates an empty item provider to which you can later register a data or file representation.
- [convenience init(object: any NSItemProviderWriting)](nsitemprovider/init(object:).md)
  Creates a new item provider, employing a specified object’s type identifiers to specify the data representations eligible for the provider to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/init(item:typeidentifier:))*