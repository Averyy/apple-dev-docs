# identityBanner

**Framework**: TVML

Displays information about an artist or performer.

#### Overview

The `identityBanner` element displays information directly above the `collectionList` element and is used to briefly describe its contents. Here’s an example that displays available action movies that emphasize cars.

```xml
<stackTemplate>
    <identityBanner>
        <title>Available Action Movies</title>
        <subtitle>Cars</subtitle>
    </identityBanner>
    <collectionList>
        <shelf>
            <section>
                <lockup>
                    <img src="http://localhost:9001/images/Car_Movie_250x375_A.png" width="182" height="274" />
                    <title>Movie 1</title>
                </lockup>
                <lockup>
                    <img src="http://localhost:9001/images/Car_Movie_250x375_B.png" width="182" height="274" />
                    <title>Movie 2</title>
                </lockup>
            </section>
        </shelf>
    </collectionList>
</stackTemplate>
```

##### Subelements of Identifybanner

- [`row`](row.md)
- [`subtitle`](subtitle.md)
- [`title`](title.md)

##### Elements That Use Identitybanner

- [`stackTemplate`](stacktemplate.md)

## Topics

### Valid TVML Styles
- [margin](margin.md)
  Specifies the spacing around an element.
- [padding](padding.md)
  Specifies the padding between the border and contents of an element.
### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [banner](banner.md)
  Displays information along the top of a TVML page.
- [itemBanner](itembanner.md)
  Displays information associated with an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/identitybanner)*