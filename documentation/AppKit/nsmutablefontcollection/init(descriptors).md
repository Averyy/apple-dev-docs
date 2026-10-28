# init(descriptors:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a mutable font collection containing the fonts that match the specified font descriptors.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init(descriptors queryDescriptors: [NSFontDescriptor])
```

```objc
+ (NSMutableFontCollection *) fontCollectionWithDescriptors:(NSArray<NSFontDescriptor *> *) queryDescriptors;
```

## Return Value

A mutable font collection object.

## Parameters

- `queryDescriptors`: One or more query descriptors describing the fonts to include in the collection.

## See Also

### Creating a Font Collection
- [init(locale: Locale)](./init%28locale%29.md)
  Creates a mutable font collection containing fonts suitable for the specified locale.
- [init?(name: NSFontCollection.Name)](./init%28name%29.md)
  Creates a mutable named font collection object.
- [init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)](./init%28name,visibility%29.md)
  Creates a mutable font collection with the specified name and font visibility.
- [class var withAllAvailableDescriptors: NSMutableFontCollection](./withallavailabledescriptors.md)
  The mutable font collection that matches all registered fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/init(descriptors:))*