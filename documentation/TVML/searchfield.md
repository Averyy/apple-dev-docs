# searchField

**Framework**: TVML

Displays an interactive text field used to search for content.

#### Overview

The `searchField` element creates a text field for user input. Different keyboards can be used to provide the best input experience for the user. Here’s an example that presents a search field along with three movies.

```xml
<searchTemplate>
    <searchField/>
    <shelf>
        <header>
            <title>Popular</title>
        </header>
        <section>
            <lockup>
                <img src="path to images on your server/Car_Movie_250x375_A.png" width="182" height="274" />
                <title>Movie 1</title>
            </lockup>
            <lockup>
                <img src="path to images on your server/Car_Movie_250x375_B.png" width="182" height="274" />
                <title>Movie 2</title>
            </lockup>
            <lockup>
                <img src="path to images on your server/Car_Movie_250x375_C.png" width="182" height="274" />
                <title>Movie 3</title>
            </lockup>
        </section>
    </shelf>
</searchTemplate>
```

##### Contained in

- [`searchTemplate`](searchtemplate.md)
- [`stackTemplate`](stacktemplate.md)

## Topics

### Valid TVML Attributes
- [binding](binding.md)
  Associates information in a data item with an element.
- [keyboardType](keyboardtype.md)
  Specifies the keyboard to display.
- [prototype](prototype.md)
  Associates a data item type with an element.
- [showSpinner](showspinner.md)
  Displays a rotating spinner icon inside of a search field.
- [theme](theme.md)
  Sets the color scheme for an element.

## See Also

- [asset](asset.md)
  Contains information about where a media item is stored.
- [relatedContentURL](relatedcontenturl.md)
  Contains the URL for the displayed content.
- [textField](textfield.md)
  Displays a text field the user can interact with.
- [mediaContent](mediacontent.md)
  Contains information used to play inline audio or video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/searchfield)*