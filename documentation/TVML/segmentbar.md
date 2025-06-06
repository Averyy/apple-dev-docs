# segmentBar

**Framework**: TVML

Displays a list of segment bar items.

#### Overview

The `segmentBar` element contains a list of `segmentBarItem` elements that are displayed horizontally. Use the remote to move the cursor between the contained `segmentBarItem` elements. Here’s an example that has a title and subtitle above a segment bar that contains one item.

```xml
<segmentBarHeader>
   <title>Title</title>
   <subtitle>Subtitle</subtitle>
   <segmentBar>
      <segmentBarItem>
         <title>Title</title>
      </segmentBarItem>
   </segmentBar>
</segmentBarHeader>
```

##### Subelements of Segmentbar

- [`segmentBarItem`](segmentbaritem.md)

##### Elements That Use Segmentbar

- [`segmentBarHeader`](segmentbarheader.md)

## Topics

### Valid TVML Styles
- [color](color.md)
  Changes the color of an element.
- [margin](margin.md)
  Specifies the spacing around an element.
- [tv-highlight-color](tv-highlight-color.md)
  Changes an element’s color when it comes into focus.
### Valid TVML Attributes
- [autoHighlight](autohighlight.md)
  Specifies that the element should initially be in focus.
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
- [segmentBarHeader](segmentbarheader.md)
  Displays information above a segment bar.
- [segmentBarItem](segmentbaritem.md)
  Provides titles inside of a segment bar.
- [tumblerBar](tumblerbar.md)
  Displays a list of `tumblerItem` elements.
- [tumblerItem](tumbleritem.md)
  Contains title information for a tumbler header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/segmentbar)*