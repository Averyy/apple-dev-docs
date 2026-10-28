# withAllAvailableDescriptors

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The font collection that matches all registered fonts.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@NSCopying
class var withAllAvailableDescriptors: NSFontCollection { get }
```

```objc
@property (class, copy, readonly) NSFontCollection * fontCollectionWithAllAvailableDescriptors;
```

## Return Value

The collection of all fonts available to the current application.

## See Also

### Creating Font Collections
- [init(descriptors: [NSFontDescriptor])](./init%28descriptors%29.md)
  Returns a font collection matching the given descriptors.
- [init?(locale: Locale)](./init%28locale%29.md)
  Returns a collection of fonts matching the given locale.
- [init?(name: NSFontCollection.Name)](./init%28name%29.md)
  Creates a named font collection object.
- [init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)](./init%28name,visibility%29.md)
  Creates a font collection with the specified name and font visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/withallavailabledescriptors)*