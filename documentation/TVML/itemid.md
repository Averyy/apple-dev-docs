# itemID

**Framework**: TVML

Mark elements for reuse during DOM updates.

#### Overview

Use the `itemID` attribute to identify which elements are considered the same so they can be reused during DOM updates. When recreating the DOM, TVMLKit makes any necessary changes at the view level while retaining existing cells that have not been modified.

##### Values for Itemid

##### Elements That Use Itemid

- [`productBundleTemplate`](productbundletemplate.md)
- [`productTemplate`](producttemplate.md)
- [`searchTemplate`](searchtemplate.md)
- [`stackTemplate`](stacktemplate.md)

`itemID` can only be used with the following elements inside of the above templates:

- [`grid`](grid.md)
- [`section`](section.md) in the `grid` or `shelf` element
- [`shelf`](shelf.md)
- Any element that can appear in a `shelf`/`section` or `grid`/`section` combination

## See Also

- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [needsMoreThreshold](needsmorethreshold.md)
  Sets the amount of remaining screen lengths before firing the needs more event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/itemid)*