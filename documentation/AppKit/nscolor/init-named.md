# init(named:)

**Framework**: AppKit  
**Kind**: init

Creates a color object from the provided name, which corresponds to a color in the default asset catalog of the app’s main bundle.

**Availability**:
- macOS 10.13+

## Declaration

```swift
init?(named name: NSColor.Name)
```

## Parameters

- `name`: The name of the color in the asset catalog.

## See Also

- [init?(named: NSColor.Name, bundle: Bundle?)](nscolor/init(named:bundle:).md)
  Creates a color object from the provided name, which corresponds to a color in the default asset catalog of the specified bundle.
- [init?(catalogName: NSColorList.Name, colorName: NSColor.Name)](nscolor/init(catalogname:colorname:).md)
  Creates a color object using the specified asset catalog and color names.
- [typealias Name](nscolor/name.md)
  The name of a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(named:))*