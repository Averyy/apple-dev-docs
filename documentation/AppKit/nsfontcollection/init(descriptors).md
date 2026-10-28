# init(descriptors:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns a font collection matching the given descriptors.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init(descriptors queryDescriptors: [NSFontDescriptor])
```

```objc
+ (NSFontCollection *) fontCollectionWithDescriptors:(NSArray<NSFontDescriptor *> *) queryDescriptors;
```

## Return Value

The font collection matching the given descriptors.

## Parameters

- `queryDescriptors`: The descriptors used to match the returned collection.

## See Also

### Creating Font Collections
- [init?(locale: Locale)](./init%28locale%29.md)
  Returns a collection of fonts matching the given locale.
- [init?(name: NSFontCollection.Name)](./init%28name%29.md)
  Creates a named font collection object.
- [init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)](./init%28name,visibility%29.md)
  Creates a font collection with the specified name and font visibility.
- [class var withAllAvailableDescriptors: NSFontCollection](./withallavailabledescriptors.md)
  The font collection that matches all registered fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/init(descriptors:))*