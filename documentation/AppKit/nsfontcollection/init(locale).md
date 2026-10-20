# init(locale:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns a collection of fonts matching the given locale.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init?(locale: Locale)
```

```objc
+ (NSFontCollection *) fontCollectionWithLocale:(NSLocale *) locale;
```

#### Return Value

A collection of fonts matching the given locale.

## Parameters

- `locale`: The locale to match.

## See Also

### Creating Font Collections
- [init(descriptors: [NSFontDescriptor])](./init%28descriptors%29.md)
  Returns a font collection matching the given descriptors.
- [init?(name: NSFontCollection.Name)](./init%28name%29.md)
  Creates a named font collection object.
- [init?(name: NSFontCollection.Name, visibility: NSFontCollection.Visibility)](./init%28name,visibility%29.md)
  Creates a font collection with the specified name and font visibility.
- [class var withAllAvailableDescriptors: NSFontCollection](./withallavailabledescriptors.md)
  The font collection that matches all registered fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/init(locale:))*