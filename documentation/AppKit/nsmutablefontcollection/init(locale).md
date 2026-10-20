# init(locale:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a mutable font collection containing fonts suitable for the specified locale.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init(locale: Locale)
```

```objc
+ (NSMutableFontCollection *) fontCollectionWithLocale:(NSLocale *) locale;
```

#### Return Value

A mutable collection of fonts matching the specified locale.

## Parameters

- `locale`: The locale associated with the fonts you want.

## See Also

### Creating a Font Collection
- [init(descriptors: [NSFontDescriptor])](./init%28descriptors%29.md)
  Creates a mutable font collection containing the fonts that match the specified font descriptors.
- [init?(name: NSFontCollection.Name)](./init%28name%29.md)
  Creates a mutable named font collection object.
- [init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)](./init%28name,visibility%29.md)
  Creates a mutable font collection with the specified name and font visibility.
- [class var withAllAvailableDescriptors: NSMutableFontCollection](./withallavailabledescriptors.md)
  The mutable font collection that matches all registered fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/init(locale:))*