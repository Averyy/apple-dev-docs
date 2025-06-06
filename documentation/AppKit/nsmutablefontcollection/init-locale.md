# init(locale:)

**Framework**: AppKit  
**Kind**: init

Creates a mutable font collection containing fonts suitable for the specified locale.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init(locale: Locale)
```

#### Return Value

A mutable collection of fonts matching the specified locale.

## Parameters

- `locale`: The locale associated with the fonts you want.

## See Also

- [init(descriptors: [NSFontDescriptor])](nsmutablefontcollection/init(descriptors:).md)
  Creates a mutable font collection containing the fonts that match the specified font descriptors.
- [init?(name: NSFontCollection.Name)](nsmutablefontcollection/init(name:).md)
  Creates a mutable named font collection object.
- [init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)](nsmutablefontcollection/init(name:visibility:).md)
  Creates a mutable font collection with the specified name and font visibility.
- [class var withAllAvailableDescriptors: NSMutableFontCollection](nsmutablefontcollection/withallavailabledescriptors.md)
  The mutable font collection that matches all registered fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/init(locale:))*