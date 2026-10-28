# Enhancing Your Articles with Styles

**Framework**: Apple News  
**Role**: Article

Improve the appearance of the text and components in your article by using Apple News Format styles.

## Overview

In Apple News Format, you can use your own custom styles throughout an article to get precisely the look you want for your content and give your users a better experience.

You can create custom styles that a single component uses (for example, a stylish drop cap used only at the beginning of your article) or that all components of a specific type use (for example, a font that all `body` components use). You can apply a style to a single word in a title or define a style for the entire document. The following table summarizes the styles in Apple News Format.

| Apply style to | Using | Includes |
| --- | --- | --- |
| Text or a range of text in your content | [`TextStyle`](../AppleNewsFormat/textstyle.md) and [`InlineTextStyle`](../AppleNewsFormat/inlinetextstyle.md) | Fonts (family, weight, style, width, name, and size), background color, ordered and unordered list items, strikethrough, text color, text shadow, tracking (spacing between letters), underline, and vertical alignment. |
| Text component (such as `body`, `title`, and `caption`) | [`ComponentTextStyle`](../AppleNewsFormat/componenttextstyle.md) | Text style, drop caps, first-line indents, hanging punctuation, hyphenation, line height, link style, paragraph spacing, and text alignment. |
| Table (both JSON and HTML tables) | [`TableStyle`](../AppleNewsFormat/tablestyle.md) | Styles for table rows, columns, and cells. |
| Component (such as `photo` or `body`) | [`ComponentStyle`](../AppleNewsFormat/componentstyle.md) | Background color, background fill, background image, background video, opacity, borders, and table styles. |
| Document (the whole article) | [`ArticleDocument`](../AppleNewsFormat/articledocument.md) | Background color. |

### Define Custom Styles

In Apple News Format, you can create custom styles and custom text styles for a specific component or range of text. Or, if you want all components or text in your article to be able to use them, you can include them in one of the following objects:

- [`ArticleDocument.textStyles`](../AppleNewsFormat/articledocument/textstyles-data.dictionary.md)
- [`ArticleDocument.componentTextStyles`](../AppleNewsFormat/articledocument/componenttextstyles-data.dictionary.md)
- [`ArticleDocument.componentStyles`](../AppleNewsFormat/articledocument/componentstyles-data.dictionary.md)

Creating custom styles in one of these objects makes it easier to ensure a consistent look and feel for your article. For example, to add a line to the top and bottom of a pull quote, you might create a [`ComponentStyle`](../AppleNewsFormat/componentstyle.md) object with top and bottom borders and use that object as the value of the `style` property in the [`PullQuote`](../AppleNewsFormat/pullquote.md) component.

However, if you plan to have pull quotes throughout your article — all with a top and bottom border — then you can define a style named `PullQuoteBorder` in the [`ArticleDocument.componentStyles`](../AppleNewsFormat/articledocument/componentstyles-data.dictionary.md) object, so that it’s available to all other components in your document. When you want to use that same border style, you simply use the style name you created (`PullQuoteBorder`) as the value of a component’s `style` property instead of redefining the style every time.

#### Define a Custom Style for a Component

Include a [`ComponentStyle`](../AppleNewsFormat/componentstyle.md) object as the value of the individual component’s style property. To define a custom style that’s available to *any* component, include a property, with a name that you define, in the [`ArticleDocument.componentStyles`](../AppleNewsFormat/articledocument/componentstyles-data.dictionary.md) object. Include a [`ComponentStyle`](../AppleNewsFormat/componentstyle.md) object as the value of that property, and use that property’s name string as the value of the individual component’s style property.

#### Define a Custom Text Style for the Content of a Text Component

Include a [`ComponentTextStyle`](../AppleNewsFormat/componenttextstyle.md) object as the value of the individual component’s `textStyle` property. To define a custom text style that’s available to *any* text components, include a property, with a name that you define, in the [`ArticleDocument.componentTextStyles`](../AppleNewsFormat/articledocument/componenttextstyles-data.dictionary.md) object. Include a [`ComponentTextStyle`](../AppleNewsFormat/componenttextstyle.md) object as the value of that property, and use the property’s name string as the value of the individual component’s `textStyle` property.

#### Define a Custom Text Style for a Range of Text in a Component

Include a property, with a name that you define, in the [`ArticleDocument.textStyles`](../AppleNewsFormat/articledocument/textstyles-data.dictionary.md) object, and include a [`TextStyle`](../AppleNewsFormat/textstyle.md) object as the value of that property. Use either HTML or Markdown to refer to the TextStyles objects, or use an [`InlineTextStyle`](../AppleNewsFormat/inlinetextstyle.md) object.

## See Also

### Related Documentation
- [Apple News Format Tutorials](./apple-news-format-tutorials.md)
  Create a basic article and then add advanced design features.
### Styles
- [Supporting Dark Mode for Your Article](./supporting-dark-mode-for-your-article.md)
  Update your article template so that your article adapts when Dark Mode is active.
- [object DocumentStyle](../AppleNewsFormat/documentstyle.md)
  The object for setting the background color for your article.
- [Text Styles](./text-styles.md)
  Learn about text styles and how to apply them to your text and text components.
- [Component Styles](./component-styles.md)
  Learn to use component styles to add borders, set background colors, and apply background images to components and to set the styling for tables.
- [Supported Color Names](./supported-color-names.md)
  Learn the color names supported in Apple News Format.
- [type Color](../AppleNewsFormat/color.md)
  The strings for defining colors in Apple News Format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/enhancing-your-articles-with-styles)*