# tumblerItem

**Framework**: TVML

Contains title information for a tumbler header.

#### Overview

The user swipes left and right on the remote to display the previous and next `tumblerItem` elements inside of the tumbler header. Here’s an example of a tumbler bar containing two tumbler items.

```xml
<tumblerBar>
    <tumblerItem>
        <title>Title 1</title>
        <subtitle>5 Items</subtitle>
    </tumblerItem>
    <tumblerItem>
        <title>Title 2</title>
        <subtitle>12 Items</subtitle>
    </tumblerItem>
</tumblerBar>
```

##### Subelements of Tumbleritem

- [`subtitle`](subtitle.md)
- [`title`](title.md)

##### Elements That Use Tumberbaritem

- [`tumblerBar`](tumblerbar.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/tumbleritem)*