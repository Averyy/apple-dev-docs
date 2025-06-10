# Defining and Applying Text Styles

**Framework**: Apple News

Define and apply custom, default, and inline text styles, or use HTML tags or Markdown syntax to style your text.

#### Overview

Text styles determine the look of text in your article. For example, text styles let you create drop caps and shadowing.

![Screenshot of an article with a drop cap.](https://docs-assets.developer.apple.com/published/102b076a3c5b604470c3e93a4e533e39/media-4085702%402x.png)

In Apple News Format, you can define:

- Custom default text style for your article.
- Custom role-based default text styles for components with a specific role. You can use this option for all components with the same role in an article.
- Custom text styles that can apply to ranges of text. You use this option if you have only a portion of text that needs a specific style in a single component or in multiple components.
- Custom component text style to use with multiple components.

The recommended type sizes are as follows:

- For [`Body`](https://developer.apple.com/documentation/applenewsformat/body) `text`, choose a size between 16–19 points.
- For line spacing, choose a size between 24–32 points. See `lineHeight`, in [`ComponentTextStyle`](https://developer.apple.com/documentation/applenewsformat/componenttextstyle).
- For [`Title`](https://developer.apple.com/documentation/applenewsformat/title) `text`, [`Heading`](https://developer.apple.com/documentation/applenewsformat/heading) (heading1, heading2, heading3, heading4, heading5, heading6), [`DropCapStyle`](https://developer.apple.com/documentation/applenewsformat/dropcapstyle), [`PullQuote`](https://developer.apple.com/documentation/applenewsformat/pullquote), and [`Intro`](https://developer.apple.com/documentation/applenewsformat/intro) `text`, choose a size larger than 19 points.
- For [`Caption`](https://developer.apple.com/documentation/applenewsformat/caption) `text`, choose a size that’s smaller than 16 points.

> **Note**:  You must use only lowercase characters for custom tags. For example, if you have a default text style called `default-tag-blueBackgroundColor`, Apple News Format won’t apply the default text style. You must name it `default-tag-bluebackgroundcolor`.

##### Define a Custom Default Text Style

To create a custom default text style for your article, add a text style called `default` in the [`ArticleDocument.componentTextStyles`](https://developer.apple.com/documentation/applenewsformat/articledocument/componenttextstyles-data.dictionary), as shown in this example.

```json
"componentTextStyles": {
  "default": {
    "fontName": "DINAlternate-Bold",
    "textColor": "#222222",
    "fontSize": 16,
    "lineHeight": 22,
    "linkStyle": {
      "textColor": "#D5B327"
    }
  }
}
```

##### Define a Custom Role Based Default Text Style

To create a custom, role-based, default text style for all components, add a text style to the [`ArticleDocument.componentTextStyles`](https://developer.apple.com/documentation/applenewsformat/articledocument/componenttextstyles-data.dictionary) object, and name it `default-<role>` (where `<role>` is a valid component `role` name). For an explanation of `role`, see [`Components`](components.md).

Role-based, default text styles take precedence over default text styles, but any properties not specified in the role-based default continue to use the values from the article default.  When you create a component that has the same role, Apple News Format automatically applies the role-based default style to the new component. If you make changes to the style, those changes are propagated throughout your article.

The following example shows a default text style and two role-based default text styles — one for a [`Body`](https://developer.apple.com/documentation/applenewsformat/body) component and one for a [`Caption`](https://developer.apple.com/documentation/applenewsformat/caption) component.

```json
"componentTextStyles": {
  "default": {
    "fontName": "DINAlternate-Bold",
    "textColor": "#222222",
    "fontSize": 16,
    "lineHeight": 22,
    "linkStyle": {
      "textColor": "#D5B327"
    }    
  },	    
  "default-body": {
    "fontName": "IowanOldStyle-Italic",
    "paragraphSpacingBefore": 12,
    "paragraphSpacingAfter": 12
  },
  "default-caption": {
    "fontName": "IowanOldStyle-Italic",
    "fontSize": 12,
    "lineHeight": 16,
    "paragraphSpacingBefore": 12,
    "paragraphSpacingAfter": 12,
    "textColor": "#53585F"
  }
}
```

##### Define Custom Text Styles for a Range of Text

To define a custom text style for a range of text to use with a single component, use HTML, Markdown, or the [`InlineTextStyle`](https://developer.apple.com/documentation/applenewsformat/inlinetextstyle) object. See [`Using HTML with Apple News Format`](using-html-with-apple-news-format.md) and [`Using Markdown with Apple News Format`](using-markdown-with-apple-news-format.md).

You can also create a custom text style for a range of text that multiple components can use throughout your document by including a [`TextStyle`](https://developer.apple.com/documentation/applenewsformat/textstyle) object in the [`ArticleDocument.textStyles`](https://developer.apple.com/documentation/applenewsformat/articledocument/textstyles-data.dictionary) object to specify the properties of the text styles you want to apply, and name the text style. In the component’s text, if you are using HTML, use `<span data-anf-textstyle='styleName'>` with the name of the style you created to apply the text style to a range.

You can also apply a style to a range using Markdown or an `inlineTextStyle` object. Inline text styles are ignored if the component’s `format` property is set to `html` or `markdown`. Only those text style properties that have a value that you’ve specified override the component text style and default styles.

```json
{
  "components": [
    {
      "role": "body",
      "text": "<custom>Not only</custom> on Mars",
      "format": "html"
    },
    {
      "role": "body",
      "text": "<span data-anf-textstyle='sampleTextStyle'>Not only</span> on Mars",
      "format": "html"
    },
    {
      "role": "body",
      "text": "[Not only]{sampleTextStyle} on Mars",
      "format": "markdown"
    },
    {
      "role": "body",
      "text": "Not only on Mars",
      "inlineTextStyles": [
        {
          "rangeStart": 0,
          "rangeLength": 8,
          "textStyle": "sampleTextStyle"
        }
      ]
    }
  ],
  "textStyles": {
    "default-tag-custom": {
      "textColor": "#34af15"
    },
    "sampleTextStyle": {
      "textColor": "#34af15"
    }
  }
}
```

##### Define Custom Component Text Style to Use with Multiple Components

To create a custom component text style to use with multiple components, create and name a text style in the [`ArticleDocument.componentTextStyles`](https://developer.apple.com/documentation/applenewsformat/articledocument/componenttextstyles-data.dictionary) object, and specify the properties you want for that style.

To apply this custom text style, put its name as the value for the [`TextStyle`](https://developer.apple.com/documentation/applenewsformat/textstyle) object in the properties of the component. Any properties that you don’t specify in your custom text style will use the settings from the article’s default text styles. Now, whenever you add another text component that you want displayed in that style, you can simply reference the style name in the `textStyle` property for that component as shown in this example.

```json
{
  "components": [
    {
      "role": "body",
      "text": "Apple News Format allows publishers to craft beautiful editorial layouts. Galleries, audio, video, and fun interactions like animation make stories spring to life.",
      "textStyle": "light-gray-italic"
    }
  ],
  "componentTextStyles": {
    "light-gray-italic": {
      "textColor": "#DDD",
      "fontFamily": "Arial",
      "fontStyle": "italic"
    }
  }
}
```

##### Use Html and Markdown with Text

You can use HTML tags and Markdown syntax to style text in your article and to apply Apple News Format text styles.

- Use HTML tags with default styles for tags, references to `textStyles`, or a mix of both. To use HTML tags to style text in a component, set the component’s `format` property to `html`. See [`Using HTML with Apple News Format`](using-html-with-apple-news-format.md).
- Use a subset of Markdown syntax to style text within paragraphs and to use a custom text style. To use Markdown to style text in a component, set the component’s `format` property to `markdown`. See [`Using Markdown with Apple News Format`](using-markdown-with-apple-news-format.md).

## See Also

- [Applying Apple News Format Fonts](applying-apple-news-format-fonts.md)
  Choose a font family for Apple News Format that’s supported in iOS, iPadOS, and macOS.
- [object TextStyle](../applenewsformat/textstyle.md)
  The object for defining the text style, such as font family, size, and color, that you can apply to ranges of text.
- [object ComponentTextStyle](../applenewsformat/componenttextstyle.md)
  The object for defining the style for a text component, including spacing, alignment, and drop caps.
- [object DropCapStyle](../applenewsformat/dropcapstyle.md)
  The object for defining the drop cap text style to use in the first paragraph in a text component.
- [object ListItemStyle](../applenewsformat/listitemstyle.md)
  The object for defining the style for bulleted or numbered lists in an article.
- [object InlineTextStyle](../applenewsformat/inlinetextstyle.md)
  The object for applying text styling when not using HTML or Markdown formatting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/defining-and-applying-text-styles)*