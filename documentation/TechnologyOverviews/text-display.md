# Text display

**Framework**: Technology Overviews

Display localized text from your app’s interface, and discover how to lay out and render text yourself.

Words are a powerful communication tool and have multiple roles within apps. Whether you display words in your interface, or capture someone else’s words as data or input, the presentation of text involves the collaboration of several different types:

- Strings are data objects that store the characters you want to display. Some string types also store data about how to format individual characters.
- Fonts provide the visual appearance of text. The font family defines the shape of characters, while size and style values change the dimensions or appearance of those shapes.
- Views display strings using the font information you provide. Views use layout objects to help calculate the position of individual characters based on their font and the available space.

## Manage text as string data

Store text in your app using the provided [`String`](../Swift/string.md) type, which is Unicode-correct, efficient, and suitable for managing text of any length or in any language. The type is also interchangeable with the `NSString` type common in Objective-C interfaces, so you can use it in both Swift and Objective-C code.

When you need to manage text and style information together, store that text in an [`AttributedString`](../Foundation/attributedstring.md) type instead of a regular string. Attributed strings are also strings, but they allow you to apply font, style, and other visual and nonvisual characteristics to the characters of that string. For example, you can store a URL with a range of characters and use it to create a link during rendering. You can apply attributes to the entire string, to a subset of characters, or to a single character.

> **Note**: If you build a custom text view using TextKit for [UIKit](../UIKit/textkit.md) or [AppKit](../AppKit/textkit.md), you also use the [`NSAttributedString`](../Foundation/nsattributedstring.md) and [`NSMutableAttributedString`](../Foundation/nsmutableattributedstring.md) types to manage text.

## Choose the fonts for your text

The [system font](https://developer.apple.com/design/human-interface-guidelines/typography) on Apple platforms is always present, adapts readily to support [Dynamic Type](https://developer.apple.com/design/human-interface-guidelines/typography) and [accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) features, and supports an extensive range of weights, styles, and languages. The system font is the best choice for labels and text you display from the views of your app’s interface. Configure the font with custom parameters or retrieve one of the standard fonts that defines the weight and style information for you. The standard fonts allow you to choose a font based on the meaning of your content. For example, apply the [title](../SwiftUI/font/title.md) font to section headers to make them stand out visually from paragraphs of [body](../SwiftUI/font/body.md) text. Access the system fonts using the APIs for [SwiftUI](../SwiftUI/font.md), [UIKit](../UIKit/uifont/textstyle.md), and [AppKit](../AppKit/nsfont/textstyle.md).

![A screenshot showing text on an iPhone in several different styles, including a large title, a title, body text, and a subtitle.](https://developer.apple.com/tutorials/images/com.apple.TechnologyOverviews/typography-text-hierarchy-levels@2x.png)

For text that requires a more personalized appearance, choose from the system’s other [built-in fonts](https://developer.apple.com/fonts/system-fonts/) or use your own [custom fonts](./fonts.md#Bundle-a-custom-font-with-your-app). Apple platforms ship with a large collection of fonts you can apply to document-based text or other personal content. Create these fonts directly in your code or display the [UIKit](../UIKit/uifontpickerviewcontroller.md) or [AppKit](../AppKit/nsfontpanel.md) font picker interface. For example, a word processor or text-creation app might apply these fonts to the selected text or any new text someone creates. [Ship custom fonts with your app](./fonts.md#Bundle-a-custom-font-with-your-app) and access them from your code, or [share them](./fonts.md#Install-fonts-for-systemwide-use) with the rest of the system.

## Display text in your interface

Display text in your interface using the standard text views that [SwiftUI](../SwiftUI/text-input-and-output.md), [UIKit](../UIKit/text-display-and-fonts.md), and [AppKit](../AppKit/text-display.md) provide. Standard text views render your text in a consistent and efficient way. They also adapt automatically to [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode), [Dynamic Type](https://developer.apple.com/design/human-interface-guidelines/typography), [accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility), and other system settings so you don’t have to handle those changes yourself.

When you add text to one of the standard text views, the view displays that text using the [system font](https://developer.apple.com/design/human-interface-guidelines/typography) by default. For labels and text fields, you typically use the same font for the entire string. For text views, you you can specify multiple fonts using an attributed string or continue to use a single font for all of the text.

Each app-builder framework defines the approach for applying fonts to your text:

- In SwiftUI, [apply fonts](../SwiftUI/applying-custom-fonts-to-text.md) to standard text views using a [modifier](../SwiftUI/text-input-and-output.md). Choose a predefined [`Font`](../SwiftUI/font.md) type for the text style you want, or create a custom instance with your preferred font information.
- In UIKit, apply fonts to the standard text views using the methods and properties of those views. Retrieve predefined instances of the [system font](../UIKit/uifont.md) or [standard text styles](../UIKit/uifont/textstyle.md) from the [`UIFont`](../UIKit/uifont.md) type, or create custom fonts using the initializers of that type. You can also collect the font attributes you want in a [`UIFontDescriptor`](../UIKit/uifontdescriptor.md), and use that type to create a font object.
- In AppKit, apply fonts to the standard text views using the methods and properties of those views. Retrieve predefined instances of the [system font or standard text styles](../AppKit/nsfont.md) from the [`NSFont`](../AppKit/nsfont.md) type. You can also retrieve fonts meant for specific types of [UI elements](../AppKit/nsfont.md), or create custom font objects from [attributes you supply](../AppKit/nsfont.md).

When you need more control over the placement of text in your view, [create a custom view](./text-display.md#Build-a-custom-text-view) using TextKit for [UIKit](../UIKit/textkit.md) or [AppKit](../AppKit/textkit.md). TextKit provides the types you need to lay out and render text efficiently, and in a way that’s compatible with the [app-builder technologies](./app-design-and-ui.md).

## Prepare your text for translation

If you’re planning to support multiple languages, [internationalize](../Xcode/supporting-multiple-languages-in-your-app.md) your code to make it ready to handle different languages. During this process, identify the [strings](../Xcode/preparing-your-apps-text-for-translation.md) and other content that require translation and look for places where you use [numbers, currencies, dates](../Xcode/preparing-dates-numbers-with-formatters.md), images, and other content that might change after translation. Update your code to create this information in a localization-friendly way.

[String catalogs](../Xcode/localizing-and-varying-text-with-a-string-catalog.md) offer a modern way to manage localizable string resources in your app. A string catalog keeps all of your translations in one place, and gives you ways to customize translations based on grammatical differences. For example, a string that contains a number can have different translations when the number indicates zero, one, or more than one item. You can also specify per-device translations to adjust text for different device sizes.

Xcode automatically collects properly marked strings in your code and places them in string catalogs. In SwiftUI, the view initializers always mark text as localizable and add them to your string catalogs. To add other strings, use a [`String`](../Swift/string.md) initializer that takes a localized value, as shown in the following example:

```swift
myLabel.string = String(localized: "There are \(peopleInChat) people in this chat.",
              comment: "Label indicating number of chat participants.")
```

All string types store text as Unicode characters and support both left-to-right and right-to-left languages. If you support bidirectional text, make sure the rest of your text [supports both language directions](https://developer.apple.com/videos/play/wwdc2022/10107) correctly. For example, use [range sets](../Swift/rangeset.md) to correctly manage text selections with bidirectional text.

> **Note**: Translate only the strings and data that appear in your interface. Don’t translate strings you use internally to manage your data. For example, don’t translate key names you use to identify data in a custom file format.

## Build a custom text view

If you need more control over the placement and display of text than the standard text views offer, create a custom view with [TextKit](https://developer.apple.com/videos/play/wwdc2021/10061) for [UIKit](../UIKit/textkit.md) or [AppKit](../AppKit/textkit.md). Use this approach if you’re building a word processor or similarly advanced app that requires sophisticated text handling. TextKit gives you the types you need to manage and lay out text precisely in your custom view. It also integrates with other system features, like [Writing Tools](https://developer.apple.com/videos/play/wwdc2025/265), so you can incorporate those features into your own text-based code.

## Topics

### Fonts
- [Fonts](./fonts.md)
  Choose the right fonts for your app’s interface and content, and make custom fonts available across your app, its extensions, and other apps.

## See Also

### Related Documentation
- [Fonts](./fonts.md)
  Choose the right fonts for your app’s interface and content, and make custom fonts available across your app, its extensions, and other apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/text-display)*