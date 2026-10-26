# paletteMenuWithColors:titles:templateImage:selectionHandler:

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates a palette style menu displaying user-selectable color tags that tint using the specified array of colors.

**Availability**:
- macOS 14.0+

## Declaration

```objc
+ (instancetype) paletteMenuWithColors:(NSArray<NSColor *> *) colors titles:(NSArray<NSString *> *) itemTitles templateImage:(NSImage *) image selectionHandler:(void (^)(NSMenu *)) onSelectionChange;
```

#### Return Value

A menu in the palette presentation style.

## Parameters

- `colors`: The display colors for the menu items.
- `itemTitles`: The menu item titles.
- `image`: The image the system displays for the menu items.
- `onSelectionChange`: The closure to invoke when someone selects the menu item.

## See Also

### Working with Palettes
- [+ paletteMenuWithColors:titles:selectionHandler:](./palettemenuwithcolors_titles_selectionhandler_.md)
  Creates a palette style menu displaying user-selectable color tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/palettemenuwithcolors:titles:templateimage:selectionhandler:)*