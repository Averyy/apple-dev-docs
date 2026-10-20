# init(named:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a color object from the provided name, which corresponds to a color in the default asset catalog of the app’s main bundle.

**Availability**:
- macOS 10.13+

## Declaration

```swift
init?(named name: NSColor.Name)
```

```objc
+ (NSColor *) colorNamed:(NSColorName) name;
```

## Parameters

- `name`: The name of the color in the asset catalog.

## See Also

### Loading color objects from asset catalogs
- [init?(named: NSColor.Name, bundle: Bundle?)](./init%28named,bundle%29.md)
  Creates a color object from the provided name, which corresponds to a color in the default asset catalog of the specified bundle.
- [init?(catalogName: NSColorList.Name, colorName: NSColor.Name)](./init%28catalogname,colorname%29.md)
  Creates a color object using the specified asset catalog and color names.
- [typealias Name](./name.md)
  The name of a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(named:))*