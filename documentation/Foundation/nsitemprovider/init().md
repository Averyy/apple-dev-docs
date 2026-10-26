# init()

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates an empty item provider to which you can later register a data or file representation.

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
init()
```

```objc
- (instancetype) init;
```

## See Also

### Creating an item provider
- [convenience init?(contentsOf: URL!)](./init%28contentsof%29.md)
  Provides data-backed content from an existing file.
- [convenience init(contentsOf: URL, contentType: UTType?, openInPlace: Bool, coordinated: Bool, visibility: NSItemProviderRepresentationVisibility)](./init%28contentsof,contenttype,openinplace,coordinated,visibility%29.md)
  Provides data-backed content from an existing file with the specified parameters.
- [init(item: (any NSSecureCoding)?, typeIdentifier: String?)](./init%28item,typeidentifier%29.md)
  Creates an item provider with an object, according to the item provider type coercion policy.
- [convenience init(object: any NSItemProviderWriting)](./init%28object%29.md)
  Creates a new item provider, employing a specified object’s type identifiers to specify the data representations eligible for the provider to load.
- [- initWithContentsOfURL:contentType:openInPlace:coordinated:visibility:](./initwithcontentsofurl_contenttype_openinplace_coordinated_visibility_.md)
  Provides data-backed content from an existing file with the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/init())*