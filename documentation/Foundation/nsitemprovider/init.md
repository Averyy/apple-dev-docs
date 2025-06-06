# init()

**Framework**: Foundation  
**Kind**: init

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

## See Also

- [convenience init?(contentsOf: URL!)](nsitemprovider/init(contentsof:).md)
  Provides data-backed content from an existing file.
- [convenience init(contentsOf: URL, contentType: UTType?, openInPlace: Bool, coordinated: Bool, visibility: NSItemProviderRepresentationVisibility)](nsitemprovider/init(contentsof:contenttype:openinplace:coordinated:visibility:).md)
  Provides data-backed content from an existing file with the specified parameters.
- [init(item: (any NSSecureCoding)?, typeIdentifier: String?)](nsitemprovider/init(item:typeidentifier:).md)
  Creates an item provider with an object, according to the item provider type coercion policy.
- [convenience init(object: any NSItemProviderWriting)](nsitemprovider/init(object:).md)
  Creates a new item provider, employing a specified object’s type identifiers to specify the data representations eligible for the provider to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/init())*