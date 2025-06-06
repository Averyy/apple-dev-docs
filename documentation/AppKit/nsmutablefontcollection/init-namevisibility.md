# init(name:visibility:)

**Framework**: AppKit  
**Kind**: init

Creates a mutable font collection with the specified name and font visibility.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)
```

#### Return Value

A mutable font collection object.

## Parameters

- `name`: The name to apply to the font collection.
- `visibility`: The visibility of the fonts in the collection.

## See Also

- [init(descriptors: [NSFontDescriptor])](nsmutablefontcollection/init(descriptors:).md)
  Creates a mutable font collection containing the fonts that match the specified font descriptors.
- [init(locale: Locale)](nsmutablefontcollection/init(locale:).md)
  Creates a mutable font collection containing fonts suitable for the specified locale.
- [init?(name: NSFontCollection.Name)](nsmutablefontcollection/init(name:).md)
  Creates a mutable named font collection object.
- [class var withAllAvailableDescriptors: NSMutableFontCollection](nsmutablefontcollection/withallavailabledescriptors.md)
  The mutable font collection that matches all registered fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/init(name:visibility:))*