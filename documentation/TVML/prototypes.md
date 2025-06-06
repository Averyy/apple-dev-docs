# prototypes

**Framework**: TVML

Defines a group of elements that can be reused through binding.

#### Overview

The `prototypes` element is used to bind data item types, simplifying the template layout. A single binding definition provides the ability to display any number of data items. For more information on data binding, see [`TVML Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/TVMLKitJS/Conceptual/TVMLProgrammingGuide/GeneratingContentForYourApp.html#//apple_ref/doc/uid/TP40016718-CH4-SW1). Here’s an example that uses the `prototypes` element to display an undefined number of `lockup` elements.

```xml
<prototypes>
    <lockup prototype="artwork">
        <img binding="@src:{url};" width="200" height="300"/>
        <title binding="textContent:{title};" />
    </lockup>
</prototypes>
<section binding="items:{images};" />
```

##### Subelements of Prototypes

`prototypes` can contain any element that can be contained by a `section` element. The child elements must implement the `prototype` attribute to bind the correct data items.

##### Elements That Use Prototypes

`The prototypes` element can be a used by any element.

## Topics

### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [rules](rules.md)
  Contains the elements used in data binding and media queries.
- [specialize](specialize.md)
  Implements queries used for data binding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/prototypes)*