# init(name:visibility:)

**Framework**: AppKit  
**Kind**: init

Creates a font collection with the specified name and font visibility.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)
```

#### Return Value

The font collection with the specified name and visibility.

## Parameters

- `name`: The name of the collection.
- `visibility`: The visibility of the collection.

## See Also

- [init(descriptors: [NSFontDescriptor])](nsfontcollection/init(descriptors:).md)
  Returns a font collection matching the given descriptors.
- [init?(locale: Locale)](nsfontcollection/init(locale:).md)
  Returns a collection of fonts matching the given locale.
- [init?(name: NSFontCollection.Name)](nsfontcollection/init(name:).md)
  Creates a named font collection object.
- [class var withAllAvailableDescriptors: NSFontCollection](nsfontcollection/withallavailabledescriptors.md)
  The font collection that matches all registered fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/init(name:visibility:))*