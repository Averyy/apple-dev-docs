# init(catalogName:colorName:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a color object using the specified asset catalog and color names.

**Availability**:
- macOS

## Declaration

```swift
init?(catalogName listName: NSColorList.Name, colorName: NSColor.Name)
```

```objc
+ (NSColor *) colorWithCatalogName:(NSColorListName) listName colorName:(NSColorName) colorName;
```

## Return Value

The color object.

## Discussion

This method searches the app’s main bundle for an asset catalog with the specified name. It then creates a color object based on the asset whose name matches the value in `colorName`.

## Parameters

- `listName`: The name of the asset catalog in which to find the specified color; this may be a standard color catalog.
- `colorName`: The name of the color. Note that the color must be defined in the named color space to retrieve it with this method.

## See Also

### Related Documentation
- [var catalogNameComponent: NSColorList.Name](./catalognamecomponent.md)
  The catalog containing the color’s name.
- [var localizedCatalogNameComponent: String](./localizedcatalognamecomponent.md)
  The localized version of the catalog name containing the color.
- [var colorNameComponent: NSColor.Name](./colornamecomponent.md)
  The name of the color.
### Loading color objects from asset catalogs
- [init?(named: NSColor.Name)](./init%28named%29.md)
  Creates a color object from the provided name, which corresponds to a color in the default asset catalog of the app’s main bundle.
- [init?(named: NSColor.Name, bundle: Bundle?)](./init%28named,bundle%29.md)
  Creates a color object from the provided name, which corresponds to a color in the default asset catalog of the specified bundle.
- [typealias Name](./name.md)
  The name of a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(catalogname:colorname:))*