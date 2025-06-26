# LocalizedStringKey

**Framework**: SwiftUI  
**Kind**: struct

The key used to look up an entry in a strings file or strings dictionary file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct LocalizedStringKey
```

## Mentions

- [Preparing views for localization](preparing-views-for-localization.md)
- [Adding a search interface to your app](adding-a-search-interface-to-your-app.md)

#### Overview

Initializers for several SwiftUI types – such as [`Text`](text.md), [`Toggle`](toggle.md), [`Picker`](picker.md) and others –  implicitly look up a localized string when you provide a string literal. When you use the initializer `Text("Hello")`, SwiftUI creates a `LocalizedStringKey` for you and uses that to look up a localization of the `Hello` string. This works because `LocalizedStringKey` conforms to [`ExpressibleByStringLiteral`](https://developer.apple.com/documentation/Swift/ExpressibleByStringLiteral).

Types whose initializers take a `LocalizedStringKey` usually have a corresponding initializer that accepts a parameter that conforms to [`StringProtocol`](https://developer.apple.com/documentation/Swift/StringProtocol). Passing a `String` variable to these initializers avoids localization, which is usually appropriate when the variable contains a user-provided value.

As a general rule, use a string literal argument when you want localization, and a string variable argument when you don’t. In the case where you want to localize the value of a string variable, use the string to create a new `LocalizedStringKey` instance.

The following example shows how to create [`Text`](text.md) instances both with and without localization. The title parameter provided to the [`Section`](section.md) is a literal string, so SwiftUI creates a `LocalizedStringKey` for it. However, the string entries in the `messageStore.today` array are `String` variables, so the [`Text`](text.md) views in the list use the string values verbatim.

```swift
List {
    Section(header: Text("Today")) {
        ForEach(messageStore.today) { message in
            Text(message.title)
        }
    }
}
```

If the app is localized into Japanese with the following translation of its `Localizable.strings` file:

```other
"Today" = "今日";
```

When run in Japanese, the example produces a list like the following, localizing “Today” for the section header, but not the list items.

![A list with a single section header displayed in Japanese.](https://docs-assets.developer.apple.com/published/d90163e00915e5a2cb0b2b6a7628c942/SwiftUI-LocalizedStringKey-Today-List-Japanese%402x.png)

## Topics

### Creating a key from a literal value
- [init(String)](localizedstringkey/init(_:).md)
  Creates a localized string key from the given string value.
- [init(stringLiteral: String)](localizedstringkey/init(stringliteral:).md)
  Creates a localized string key from the given string literal.
### Creating a key from an interpolation
- [init(stringInterpolation: LocalizedStringKey.StringInterpolation)](localizedstringkey/init(stringinterpolation:).md)
  Creates a localized string key from the given string interpolation.
- [LocalizedStringKey.StringInterpolation](localizedstringkey/stringinterpolation.md)
  Represents the contents of a string literal with interpolations while it’s being built, for use in creating a localized string key.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringInterpolation](../Swift/ExpressibleByStringInterpolation.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)

## See Also

- [Preparing views for localization](preparing-views-for-localization.md)
  Specify hints and add strings to localize your SwiftUI views.
- [var locale: Locale](environmentvalues/locale.md)
  The current locale that views should use.
- [func typesettingLanguage(_:isEnabled:)](view/typesettinglanguage(_:isenabled:).md)
  Specifies the language for typesetting.
- [struct TypesettingLanguage](typesettinglanguage.md)
  Defines how typesetting language is determined for text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey)*