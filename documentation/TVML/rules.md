# rules

**Framework**: TVML

Contains the elements used in data binding and media queries.

#### Overview

The `rules` element contains a set of `specialize` elements that are used to modify existing elements. The `specialize` elements use data queries to determine how the existing element is modified. Here’s an example that sets the rules for a `button` element.

```xml
<rules>
    <specialize state="({progress}-greater-than:0) and ({progress}-less-than:1)">
        <button tag="button">
            <text>Resume</text>
        </button>
    </specialize>
    <specialize state="({progress}:0), ({progress}:1)">
        <button tag="button">
            <text>Play</text>
        </button>
    </specialize>
</rules>
```

##### Subelements of Rules

- [`specialize`](specialize.md)

##### Elements That Use Rules

The `rules` element can used by any other element.

## Topics

### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [prototypes](prototypes.md)
  Defines a group of elements that can be reused through binding.
- [specialize](specialize.md)
  Implements queries used for data binding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/rules)*