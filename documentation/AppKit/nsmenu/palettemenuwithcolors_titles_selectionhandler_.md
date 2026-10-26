# paletteMenuWithColors:titles:selectionHandler:

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates a palette style menu displaying user-selectable color tags.

**Availability**:
- macOS 14.0+

## Declaration

```objc
+ (instancetype) paletteMenuWithColors:(NSArray<NSColor *> *) colors titles:(NSArray<NSString *> *) itemTitles selectionHandler:(void (^)(NSMenu *)) onSelectionChange;
```

#### Return Value

A menu in the palette presentation style.

## Parameters

- `colors`: The display colors for the menu items.
- `itemTitles`: The menu item titles.
- `onSelectionChange`: The closure to invoke when someone selects the menu item.

## See Also

### Working with Palettes
- [+ paletteMenuWithColors:titles:templateImage:selectionHandler:](./palettemenuwithcolors_titles_templateimage_selectionhandler_.md)
  Creates a palette style menu displaying user-selectable color tags that tint using the specified array of colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/palettemenuwithcolors:titles:selectionhandler:)*