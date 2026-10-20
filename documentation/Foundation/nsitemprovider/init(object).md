# init(object:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a new item provider, employing a specified object’s type identifiers to specify the data representations eligible for the provider to load.

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
convenience init(object: any NSItemProviderWriting)
```

```objc
- (instancetype) initWithObject:(id<NSItemProviderWriting>) object;
```

## Parameters

- `object`: An object containing the data you want to provide.

## See Also

### Creating an item provider
- [convenience init?(contentsOf: URL!)](./init%28contentsof%29.md)
  Provides data-backed content from an existing file.
- [convenience init(contentsOf: URL, contentType: UTType?, openInPlace: Bool, coordinated: Bool, visibility: NSItemProviderRepresentationVisibility)](./init%28contentsof,contenttype,openinplace,coordinated,visibility%29.md)
  Provides data-backed content from an existing file with the specified parameters.
- [init(item: (any NSSecureCoding)?, typeIdentifier: String?)](./init%28item,typeidentifier%29.md)
  Creates an item provider with an object, according to the item provider type coercion policy.
- [init()](./init%28%29.md)
  Creates an empty item provider to which you can later register a data or file representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/init(object:))*