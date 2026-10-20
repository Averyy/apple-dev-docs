# init(name:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a mutable named font collection object.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init?(name: NSFontCollection.Name)
```

```objc
+ (NSMutableFontCollection *) fontCollectionWithName:(NSFontCollectionName) name;
```

#### Return Value

A mutable font collection object.

## Parameters

- `name`: The name to apply to the font collection.

## See Also

### Creating a Font Collection
- [init(descriptors: [NSFontDescriptor])](./init%28descriptors%29.md)
  Creates a mutable font collection containing the fonts that match the specified font descriptors.
- [init(locale: Locale)](./init%28locale%29.md)
  Creates a mutable font collection containing fonts suitable for the specified locale.
- [init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)](./init%28name,visibility%29.md)
  Creates a mutable font collection with the specified name and font visibility.
- [class var withAllAvailableDescriptors: NSMutableFontCollection](./withallavailabledescriptors.md)
  The mutable font collection that matches all registered fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/init(name:))*