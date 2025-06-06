# nowPlayingMenuItem

**Framework**: TVML

Displays information about currently playing audio.

#### Overview

The `nowPlayingMenuItem` element is used to display information about audio playing in a `menuBarTemplate`. The `nowPlayingMenuItem` element automatically appears and disappears from the menu bar as the audio session starts and stops. Here’s an example of a menu bar with the now playing information and two menu items.

```xml
<menuBar>
   <nowPlayingMenuItem>
      <title>Now Playing Info</title>
   </nowPlayingMenuItem>
   <menuItem>
      <title>Item 1</title>
   <menuItem>
   <menuItem>
      <title>Item 2</title>
   <menuItem>
</menuBar>
```

##### Subelement of Nowplayingmenuitem

- [`title`](title.md)

##### Elements That Use Nowplayingmenuitem

- [`menuBar`](menubar.md)

## Topics

### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [menuBar](menubar.md)
  Displays menu items along the top of the screen.
- [menuItem](menuitem.md)
  Displays a label for an item.
- [segmentBar](segmentbar.md)
  Displays a list of segment bar items.
- [segmentBarHeader](segmentbarheader.md)
  Displays information above a segment bar.
- [segmentBarItem](segmentbaritem.md)
  Provides titles inside of a segment bar.
- [tumblerBar](tumblerbar.md)
  Displays a list of `tumblerItem` elements.
- [tumblerItem](tumbleritem.md)
  Contains title information for a tumbler header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/nowplayingmenuitem)*