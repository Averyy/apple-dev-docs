# segmentBarHeader

**Framework**: TVML

Displays information above a segment bar.

#### Overview

The `segmentBarHeader` element displays information that is used to describe the contents of a `segmentBar` element. Here’s an example that has a title and subtitle above a segment bar that contains one item.

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

##### Subelements of Segmentbarheader

- [`segmentBar`](segmentbar.md)
- [`subtitle`](subtitle.md)
- [`title`](title.md)

##### Elements That Use Segmentbarheader

- [`list`](list.md)

## Topics

### Valid TVML Styles
- [margin](margin.md)
  Specifies the spacing around an element.
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
- [segmentBarItem](segmentbaritem.md)
  Provides titles inside of a segment bar.
- [tumblerBar](tumblerbar.md)
  Displays a list of `tumblerItem` elements.
- [tumblerItem](tumbleritem.md)
  Contains title information for a tumbler header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/segmentbarheader)*