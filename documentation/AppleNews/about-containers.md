# About Containers

**Framework**: Apple News

Learn the basic Apple News Format container concepts required for the three advanced tutorials.

#### Overview

Most of the design and layout effects in this tutorial require you to create hierarchies of nested components. In Apple News Format JSON, a container is a component that can hold other components. Container components include four types: `chapter`, `header`, `section`, and `container`.

This is an example of a simple container.

```json
{
  "role": "container",
  "components": [
    {
      "role": "title",
      "text": "A Photo",
    },
    {
      "role": "photo",
      "URL": "bundle://<filename>.<extension>",
    }
  ]
}
```

In the example above, the `container` component has two child components. Notice that a container has a property named `components` whose value is an array. Any components inside the container’s `components` array are children of the container.

## See Also

- [Nesting Components in an Article](nesting-components-in-an-article.md)
  Use container components to create the component hierarchies you need for special article designs.
- [object Container](../applenewsformat/container.md)
  Properties shared by all container types.
- [Setting Up the Advanced Tutorials](setting-up-the-advanced-tutorials.md)
  Download the tutorial files, and learn about what you’ll create in the three advanced tutorials.
- [Creating a Layered Header](creating-a-layered-header.md)
  Create a header with a caption that’s layered in front of an image.
- [Adding Parallax Behavior](adding-parallax-behavior.md)
  Create an illusion of multiple flat layers by causing the article body to overlap the header as the user scrolls.
- [Viewing the Finished Article for Advanced Design Tutorial 1](viewing-the-finished-article-for-advanced-design-tutorial-1.md)
  See the full JSON code from this tutorial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/about-containers)*