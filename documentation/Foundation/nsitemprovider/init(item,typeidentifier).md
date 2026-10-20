# init(item:typeIdentifier:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates an item provider with an object, according to the item provider type coercion policy.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.0

> **Deprecated**: Use initWithObject: instead.

## Declaration

```swift
init(item: (any NSSecureCoding)?, typeIdentifier: String?)
```

```objc
- (instancetype) initWithItem:(id<NSSecureCoding>) item typeIdentifier:(NSString *) typeIdentifier;
```

#### Return Value

An item provider for the specified item.

#### Discussion

Use this method to initialize an item provider for objects in your app. The item provider registers your object with the specified type. Subsequent requests for that same type return the specified `item`.

## Parameters

- `item`: An object containing the data you want to provide. You may specify `nil` for this parameter and register items and types later.
- `typeIdentifier`: A string that represents the UTI of the item. If `item` is not `nil`, this parameter must not be `nil`.

## See Also

### Creating an item provider
- [convenience init?(contentsOf: URL!)](./init%28contentsof%29.md)
  Provides data-backed content from an existing file.
- [convenience init(contentsOf: URL, contentType: UTType?, openInPlace: Bool, coordinated: Bool, visibility: NSItemProviderRepresentationVisibility)](./init%28contentsof,contenttype,openinplace,coordinated,visibility%29.md)
  Provides data-backed content from an existing file with the specified parameters.
- [init()](./init%28%29.md)
  Creates an empty item provider to which you can later register a data or file representation.
- [convenience init(object: any NSItemProviderWriting)](./init%28object%29.md)
  Creates a new item provider, employing a specified object’s type identifiers to specify the data representations eligible for the provider to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/init(item:typeidentifier:))*