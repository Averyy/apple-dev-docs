# Adding Components

**Framework**: Apple News

Learn the basics for adding components to your article.

#### Overview

An article can have many types of components, including text, images, social media posts, data tables, and so on. Each component is associated with both a `ComponentLayout` object that determines its placement in an article and a `ComponentStyle` object that determines its appearance.

If you like to treat a set of components as a group, add them to a [`Container`](https://developer.apple.com/documentation/applenewsformat/container) component. See [`Nesting Components in an Article`](nesting-components-in-an-article.md). Otherwise, place individual components directly into the component’s array in [`ArticleDocument`](https://developer.apple.com/documentation/applenewsformat/articledocument).

The following sample shows three components (a `title` component, an `author` component, and an `intro` component) in a `components` array.

```json
"components": [
    {
      "role": "title",
      "layout": "titleLayout",
      "text": "New Title",
      "textStyle": "titleStyle"
    },
    {
      "role": "author",
      "layout": "authorLayout",
      "text": "Angie Anders | Anders & Meyerson | March 20, 2018",
      "textStyle": "authorStyle"
    },
    {
       "role": "intro",
       "text": "The beginning was not nearly close enough and the ending had yet to be written."
    }
]
```

## See Also

- [Creating Your First Article](creating-your-first-article.md)
  Create an article with text components and component text styles.
- [object Component](../applenewsformat/component.md)
  Properties shared by all component types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/adding-components)*