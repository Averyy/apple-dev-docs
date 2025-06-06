# menuBar

**Framework**: TVML

Displays menu items along the top of the screen.

#### Overview

Users can navigate left and right to move between `menuBar` elements. Here’s an example of a menu bar with two items inside of a `menuBarTemplate` element.

```xml
<menuBarTemplate>
    <menuBar>
        <menuItem id="navigation_top_movies" data-identifier="list">
            <title>Top Movies</title>
        </menuItem>
        <menuItem id="navigation_genres" data-identifier="index">
            <title>Genres</title>
        </menuItem>
    </menuBar>
</menuBarTemplate>
```

You can also add view elements to the left and right sides of the menu bar. The left `leadingAccessoryView` and right `trailingAccessoryView` can be any simple element, including [`Display Elements`](display-elements.md), [`Multimedia Elements`](multimedia-elements.md), and [`Text Elements`](text-elements.md). Accessory views can also be row elements.

To add the equivalent of a [`leadingAccessoryView`](https://developer.apple.com/documentation/UIKit/UITabBar/leadingAccessoryView), add any supported element before the [`menuBar`](menubar.md) opening tag, as shown here:

```xml
<menuBarTemplate>
    <img src="path to images on your server/leading_icon.png"/>
    <menuBar>
        <menuItem id="navigation_top_movies" data-identifier="list">
            <title>Top Movies</title>
        </menuItem>
    </menuBar>
</menuBarTemplate>
```

To add the equivalent of a [`trailingAccessoryView`](https://developer.apple.com/documentation/UIKit/UITabBar/trailingAccessoryView), add any supported element after the [`menuBar`](menubar.md) closing tag, as shown here:

```xml
<menuBarTemplate>
    <menuBar>
        <menuItem id="navigation_top_movies" data-identifier="list">
            <title>Top Movies</title>
        </menuItem>
    </menuBar>
    <img src="path to images on your server/trailing_icon.png"/>
</menuBarTemplate>
```

##### Subelements of Menubar

- [`menuItem`](menuitem.md)
- [`section`](section.md)

##### Elements That Use Menubar

- [`mainTemplate`](maintemplate.md)
- [`menuBarTemplate`](menubartemplate.md)

## Topics

### Valid TVML Style
- [tv-tint-color](tv-tint-color.md)
  Sets the tint color for an element.
### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

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
- [tumblerItem](tumbleritem.md)
  Contains title information for a tumbler header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/menubar)*