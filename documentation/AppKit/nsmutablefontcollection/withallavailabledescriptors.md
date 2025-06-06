# withAllAvailableDescriptors

**Framework**: AppKit  
**Kind**: property

The mutable font collection that matches all registered fonts.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@NSCopying
class var withAllAvailableDescriptors: NSMutableFontCollection { get }
```

## See Also

- [init(descriptors: [NSFontDescriptor])](nsmutablefontcollection/init(descriptors:).md)
  Creates a mutable font collection containing the fonts that match the specified font descriptors.
- [init(locale: Locale)](nsmutablefontcollection/init(locale:).md)
  Creates a mutable font collection containing fonts suitable for the specified locale.
- [init?(name: NSFontCollection.Name)](nsmutablefontcollection/init(name:).md)
  Creates a mutable named font collection object.
- [init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)](nsmutablefontcollection/init(name:visibility:).md)
  Creates a mutable font collection with the specified name and font visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/withallavailabledescriptors)*