# menuItem

**Framework**: TVML

Displays a label for an item.

#### Overview

One or more `menuItem` elements are used inside of a `menuBar` element to indicate the available elements. Here’s an example with two items inside of a menu bar.

```xml
<menuBar>
   <menuItem id="navigation_top_movies" data-identifier="list">
      <title>Top Movies</title>
   </menuItem>
   <menuItem id="navigation_genres" data-identifier="index">
      <title>Genres</title>
   </menuItem>
</menuBar>
```

##### Subelements of Menuitem

- [`title`](title.md)

##### Elements That Use Menuitem

- [`menuBar`](menubar.md)
- [`section`](section.md)

## See Also

- [menuBar](menubar.md)
  Displays menu items along the top of the screen.
- [nowPlayingMenuItem](nowplayingmenuitem.md)
  Displays information about currently playing audio.
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

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/menuitem)*