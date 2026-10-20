# init(contentsOf:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Provides data-backed content from an existing file.

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
convenience init?(contentsOf fileURL: URL!)
```

```objc
- (instancetype) initWithContentsOfURL:(NSURL *) fileURL;
```

#### Return Value

An item provider for the specified file, or `nil` if an error occurs.

#### Discussion

The system uses the URL’s filename extension to select an appropriate universal type identifier. If the system can’t determine a specific universal type identifier based on the filename extension, it assigns the `public.data` universal type identifier for the file.

## Parameters

- `fileURL`: The URL of the file to use for the item provider’s data. The item provider uses the filename extension to determine the universal type identifier for the associated data.

## See Also

### Related Documentation
- [App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214)
### Creating an item provider
- [convenience init(contentsOf: URL, contentType: UTType?, openInPlace: Bool, coordinated: Bool, visibility: NSItemProviderRepresentationVisibility)](./init%28contentsof,contenttype,openinplace,coordinated,visibility%29.md)
  Provides data-backed content from an existing file with the specified parameters.
- [init(item: (any NSSecureCoding)?, typeIdentifier: String?)](./init%28item,typeidentifier%29.md)
  Creates an item provider with an object, according to the item provider type coercion policy.
- [init()](./init%28%29.md)
  Creates an empty item provider to which you can later register a data or file representation.
- [convenience init(object: any NSItemProviderWriting)](./init%28object%29.md)
  Creates a new item provider, employing a specified object’s type identifiers to specify the data representations eligible for the provider to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/init(contentsof:))*