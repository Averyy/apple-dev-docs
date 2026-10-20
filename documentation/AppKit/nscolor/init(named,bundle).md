# init(named:bundle:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a color object from the provided name, which corresponds to a color in the default asset catalog of the specified bundle.

**Availability**:
- macOS 10.13+

## Declaration

```swift
init?(named name: NSColor.Name, bundle: Bundle?)
```

```objc
+ (NSColor *) colorNamed:(NSColorName) name bundle:(NSBundle *) bundle;
```

## Parameters

- `name`: The name of the color to find.
- `bundle`: The app bundle.

## See Also

### Loading color objects from asset catalogs
- [init?(named: NSColor.Name)](./init%28named%29.md)
  Creates a color object from the provided name, which corresponds to a color in the default asset catalog of the app’s main bundle.
- [init?(catalogName: NSColorList.Name, colorName: NSColor.Name)](./init%28catalogname,colorname%29.md)
  Creates a color object using the specified asset catalog and color names.
- [typealias Name](./name.md)
  The name of a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(named:bundle:))*