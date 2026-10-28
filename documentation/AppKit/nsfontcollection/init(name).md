# init(name:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a named font collection object.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init?(name: NSFontCollection.Name)
```

```objc
+ (NSFontCollection *) fontCollectionWithName:(NSFontCollectionName) name;
```

## Return Value

The named font collection.

## Parameters

- `name`: The name of the collection.

## See Also

### Creating Font Collections
- [init(descriptors: [NSFontDescriptor])](./init%28descriptors%29.md)
  Returns a font collection matching the given descriptors.
- [init?(locale: Locale)](./init%28locale%29.md)
  Returns a collection of fonts matching the given locale.
- [init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)](./init%28name,visibility%29.md)
  Creates a font collection with the specified name and font visibility.
- [class var withAllAvailableDescriptors: NSFontCollection](./withallavailabledescriptors.md)
  The font collection that matches all registered fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/init(name:))*