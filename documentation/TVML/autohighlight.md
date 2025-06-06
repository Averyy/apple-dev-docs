# autoHighlight

**Framework**: Tvml

Specifies that the element should initially be in focus.

#### Overview

Use the `autoHighlight` attribute to denote the element that is initially in focus. Both the containing element and one child element must be set to `true`. Remove the `autoHighlight` attribute from your element to disable initial focus.

##### Values for Autohighlight

##### Elements That Use Autohighlight

- [`alertTemplate`](alerttemplate.md) that contains `button` elements
- [`catalogTemplate`](catalogtemplate.md) that contains `listItemLockup` elements
- [`compilationTemplate`](compilationtemplate.md) that contains `listItemLockup` elements
- [`descriptiveAlertTemplate`](descriptivealerttemplate.md) that contains `button` elements
- [`grid`](grid.md) that contains `lockup` elements
- [`listTemplate`](listtemplate.md) that contains `listItemLockup` elements
- [`paradeTemplate`](paradetemplate.md) that contains `listItemLockup` elements
- [`row`](row.md) that contains any `focusable` element
- [`segmentBar`](segmentbar.md) that contains `segmentBarItem` elements.
- [`shelf`](shelf.md) that contains `lockup` elements
- [`showcaseTemplate`](showcasetemplate.md) that contains `lockup` elements

> **Note**: The `shelf` and `grid` elements can only use the `autoHighlight` attribute when contained within a `productBundleTemplate`, `productTemplate`, or `stackTemplate`.

## See Also

- [binding](binding.md)
  Associates information in a data item with an element.
- [layoutDirection](layoutdirection.md)
  Specifies the direction in which text is displayed.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/TVML/autohighlight)*