# needsMoreThreshold

**Framework**: TVML

Sets the amount of remaining screen lengths before firing the needs more event.

#### Overview

Use the `needsMoreThreshold` attribute to specify when the needs more event is dispatched. When the designated threshold is met, the needs more event requests more data. Here’s an example that dispatches the needs more event when there are fewer than two screen lengths of information in the shelf to display.

```xml
<shelf needsMoreThreshold="2">
```

##### Values for Needsmorethreshold

##### Elements That Use Needsmorethreshold

- [`grid`](grid.md)
- [`shelf`](shelf.md)
- [`stackTemplate`](stacktemplate.md)

## See Also

- [binding](binding.md)
  Associates information in a data item with an element.
- [itemID](itemid.md)
  Mark elements for reuse during DOM updates.
- [prototype](prototype.md)
  Associates a data item type with an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/needsmorethreshold)*