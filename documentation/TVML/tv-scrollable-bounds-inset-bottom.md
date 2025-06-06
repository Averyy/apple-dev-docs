# tv-scrollable-bounds-inset-bottom

**Framework**: TVML

Specifies the size of an unscrollable region only at the bottom of the stack template.

#### Overview

The `tv-scrollable-bounds-inset-bottom` style creates an unscrollable region of a specified number of points up from the bottom of the `stackTemplate.`

Use the `tv-scrollable-bounds-inset-bottom` style to create an inset only at the bottom, without creating an inset at the top.

Here’s an example that sets the inset at the bottom to 100 points.

```xml
<stackTemplate style="tv-scrollable-bounds-inset-bottom: 100.0">
    <banner>
        …
    </banner>
    <collectionList>
        <shelf>
            <section>
                <lockup>…</lockup>
            </section>
        </shelf>
    </collectionList>
</stackTemplate>
```

##### Elements That Use Tv Scrollable Bounds Inset Bottom

- [`stackTemplate`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/ATV_Template_Guide/StackTemplate.html#//apple_ref/doc/uid/TP40015064-CH21)

## See Also

- [tv-scrollable-bounds-inset-top](tv-scrollable-bounds-inset-top.md)
  Specifies the size of an unscrollable region only at the top of the stack template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvml/tv-scrollable-bounds-inset-bottom)*