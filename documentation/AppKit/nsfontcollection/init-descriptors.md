# init(descriptors:)

**Framework**: AppKit  
**Kind**: init

Returns a font collection matching the given descriptors.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init(descriptors queryDescriptors: [NSFontDescriptor])
```

#### Return Value

The font collection matching the given descriptors.

## Parameters

- `queryDescriptors`: The descriptors used to match the returned collection.

## See Also

- [init?(locale: Locale)](nsfontcollection/init(locale:).md)
  Returns a collection of fonts matching the given locale.
- [init?(name: NSFontCollection.Name)](nsfontcollection/init(name:).md)
  Creates a named font collection object.
- [init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)](nsfontcollection/init(name:visibility:).md)
  Creates a font collection with the specified name and font visibility.
- [class var withAllAvailableDescriptors: NSFontCollection](nsfontcollection/withallavailabledescriptors.md)
  The font collection that matches all registered fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/init(descriptors:))*