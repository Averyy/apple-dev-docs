# init(name:visibility:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a font collection with the specified name and font visibility.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)
```

```objc
+ (NSFontCollection *) fontCollectionWithName:(NSFontCollectionName) name visibility:(NSFontCollectionVisibility) visibility;
```

## Return Value

The font collection with the specified name and visibility.

## Parameters

- `name`: The name of the collection.
- `visibility`: The visibility of the collection.

## See Also

### Creating Font Collections
- [init(descriptors: [NSFontDescriptor])](./init%28descriptors%29.md)
  Returns a font collection matching the given descriptors.
- [init?(locale: Locale)](./init%28locale%29.md)
  Returns a collection of fonts matching the given locale.
- [init?(name: NSFontCollection.Name)](./init%28name%29.md)
  Creates a named font collection object.
- [class var withAllAvailableDescriptors: NSFontCollection](./withallavailabledescriptors.md)
  The font collection that matches all registered fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/init(name:visibility:))*