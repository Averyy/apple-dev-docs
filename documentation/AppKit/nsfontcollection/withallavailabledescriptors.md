# withAllAvailableDescriptors

**Framework**: AppKit  
**Kind**: property

The font collection that matches all registered fonts.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@NSCopying
class var withAllAvailableDescriptors: NSFontCollection { get }
```

#### Return Value

The collection of all fonts available to the current application.

## See Also

- [init(descriptors: [NSFontDescriptor])](nsfontcollection/init(descriptors:).md)
  Returns a font collection matching the given descriptors.
- [init?(locale: Locale)](nsfontcollection/init(locale:).md)
  Returns a collection of fonts matching the given locale.
- [init?(name: NSFontCollection.Name)](nsfontcollection/init(name:).md)
  Creates a named font collection object.
- [init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)](nsfontcollection/init(name:visibility:).md)
  Creates a font collection with the specified name and font visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/withallavailabledescriptors)*