# initWithContentsOfURL:contentType:openInPlace:coordinated:visibility:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (instancetype) initWithContentsOfURL:(NSURL *) fileURL contentType:(UTType *) contentType openInPlace:(BOOL) openInPlace coordinated:(BOOL) coordinated visibility:(NSItemProviderRepresentationVisibility) visibility;
```

## Return Value

An item provider for the specified file or `nil` if an error occurred.

## Discussion

If [`openInPlace`](../nsitemproviderfileoptions/openinplace.md) is set to `false`, the system copies the file provided before the load handler returns.

## Parameters

- `fileURL`: The URL of the file to use for the item provider’s data.
- `contentType`: The content type of the specified file.
- `openInPlace`: `true` if the system opens the file in place.
- `coordinated`: `true` if the returned file must be accessed using [`NSFileCoordinator`](../nsfilecoordinator.md).
- `visibility`: The [`NSItemProviderRepresentationVisibility`](../nsitemproviderrepresentationvisibility.md) setting the system uses to identify which processes can see this content.

## See Also

### Creating an item provider
- [convenience init?(contentsOf: URL!)](./init%28contentsof%29.md)
  Provides data-backed content from an existing file.
- [init(item: (any NSSecureCoding)?, typeIdentifier: String?)](./init%28item,typeidentifier%29.md)
  Creates an item provider with an object, according to the item provider type coercion policy.
- [init()](./init%28%29.md)
  Creates an empty item provider to which you can later register a data or file representation.
- [convenience init(object: any NSItemProviderWriting)](./init%28object%29.md)
  Creates a new item provider, employing a specified object’s type identifiers to specify the data representations eligible for the provider to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/initwithcontentsofurl:contenttype:openinplace:coordinated:visibility:)*