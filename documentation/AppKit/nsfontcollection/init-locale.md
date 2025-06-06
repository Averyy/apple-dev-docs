# init(locale:)

**Framework**: AppKit  
**Kind**: init

Returns a collection of fonts matching the given locale.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init?(locale: Locale)
```

#### Return Value

A collection of fonts matching the given locale.

## Parameters

- `locale`: The locale to match.

## See Also

- [init(descriptors: [NSFontDescriptor])](nsfontcollection/init(descriptors:).md)
  Returns a font collection matching the given descriptors.
- [init?(name: NSFontCollection.Name)](nsfontcollection/init(name:).md)
  Creates a named font collection object.
- [init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)](nsfontcollection/init(name:visibility:).md)
  Creates a font collection with the specified name and font visibility.
- [class var withAllAvailableDescriptors: NSFontCollection](nsfontcollection/withallavailabledescriptors.md)
  The font collection that matches all registered fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/init(locale:))*