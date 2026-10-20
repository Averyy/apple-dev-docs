# NSColor.Name

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

The name of a color.

**Availability**:
- macOS

## Declaration

```swift
typealias Name = String
```

```c
typedef NSString * NSColorName;
```

## See Also

### Loading color objects from asset catalogs
- [init?(named: NSColor.Name)](./init%28named%29.md)
  Creates a color object from the provided name, which corresponds to a color in the default asset catalog of the app’s main bundle.
- [init?(named: NSColor.Name, bundle: Bundle?)](./init%28named,bundle%29.md)
  Creates a color object from the provided name, which corresponds to a color in the default asset catalog of the specified bundle.
- [init?(catalogName: NSColorList.Name, colorName: NSColor.Name)](./init%28catalogname,colorname%29.md)
  Creates a color object using the specified asset catalog and color names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/name)*