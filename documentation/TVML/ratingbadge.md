# ratingBadge

**Framework**: TVML

Displays an image used to rate a product.

#### Overview

The `ratingBadge` element contains a link to an image that is to be displayed. This element is commonly used to display a small image inside of a `reviewCard` element. Here’s an example of a review with a fresh rating from Rotten Tomatoes.

```xml
<reviewCard>
    <breviewBadge src="resource://tomato-fresh-m" />
    <title>WWDC Review</title>
    <description>Brief review here</description>
    <text>Ravi Patel June, 8 2015</text>
</reviewCard>
```

##### Contained in

- [`organizer`](organizer.md)
- [`ratingCard`](ratingcard.md)
- [`reviewCard`](reviewcard.md)

## Topics

### Valid TVML Styles
- [margin](margin.md)
  Specifies the spacing around an element.
- [tv-rating-style](tv-rating-style.md)
  Sets the displayed image for rating a product.
- [tv-tint-color](tv-tint-color.md)
  Sets the tint color for an element.
### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.
- [value](value.md)
  Specifies the value used for a fillable element.

## See Also

- [badge](badge.md)
  A small image displayed alongside or on top of another image.
- [seasonBadge](seasonbadge.md)
  Displays an image that indicates the season for an associated media item.
- [textBadge](textbadge.md)
  Displays text associated with an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/ratingbadge)*