# init(contentsOf:contentType:openInPlace:coordinated:visibility:)

**Framework**: Foundation  
**Kind**: init

Provides data-backed content from an existing file with the specified parameters.

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
convenience init(contentsOf fileURL: URL, contentType: UTType?, openInPlace: Bool = false, coordinated: Bool = false, visibility: NSItemProviderRepresentationVisibility = .all)
```

#### Discussion

If [`openInPlace`](nsitemproviderfileoptions/openinplace.md) is set to `false`, the system copies the file provided before the load handler returns.

## Parameters

- `fileURL`: The URL of the file to use for the item provider’s data.
- `contentType`: The content type of the specified file.
- `openInPlace`:   if the system opens the file in place.
- `coordinated`:   if the returned file must be accessed using  .
- `visibility`: The   setting the system uses to identify which processes can see this content.

## See Also

- [convenience init?(contentsOf: URL!)](nsitemprovider/init(contentsof:).md)
  Provides data-backed content from an existing file.
- [init(item: (any NSSecureCoding)?, typeIdentifier: String?)](nsitemprovider/init(item:typeidentifier:).md)
  Creates an item provider with an object, according to the item provider type coercion policy.
- [init()](nsitemprovider/init.md)
  Creates an empty item provider to which you can later register a data or file representation.
- [convenience init(object: any NSItemProviderWriting)](nsitemprovider/init(object:).md)
  Creates a new item provider, employing a specified object’s type identifiers to specify the data representations eligible for the provider to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/init(contentsof:contenttype:openinplace:coordinated:visibility:))*