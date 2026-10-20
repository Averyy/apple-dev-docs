# withAllAvailableDescriptors

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The mutable font collection that matches all registered fonts.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@NSCopying
class var withAllAvailableDescriptors: NSMutableFontCollection { get }
```

```objc
@property (class, copy, readonly) NSMutableFontCollection * fontCollectionWithAllAvailableDescriptors;
```

## See Also

### Creating a Font Collection
- [init(descriptors: [NSFontDescriptor])](./init%28descriptors%29.md)
  Creates a mutable font collection containing the fonts that match the specified font descriptors.
- [init(locale: Locale)](./init%28locale%29.md)
  Creates a mutable font collection containing fonts suitable for the specified locale.
- [init?(name: NSFontCollection.Name)](./init%28name%29.md)
  Creates a mutable named font collection object.
- [init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)](./init%28name,visibility%29.md)
  Creates a mutable font collection with the specified name and font visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutablefontcollection/withallavailabledescriptors)*