# assumesTopLevelDictionary

**Framework**: Foundation  
**Kind**: property

Specifies that decoding assumes the top level of the JSON data is a dictionary, even if it doesn’t begin and end with braces.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var assumesTopLevelDictionary: Bool { get set }
```

#### Discussion

This is an extension to JSON5 that’s not part of the specification. [`AttributedString`](attributedstring.md) uses this option, along with [`allowsJSON5`](jsondecoder/allowsjson5.md), to support the use of JSON5 inside Markdown strings that use multiple custom attributes. Using [`assumesTopLevelDictionary`](jsondecoder/assumestopleveldictionary.md) allows for the following syntax inside the parentheses of the custom attribute markup:

```swift
This is a [Markdown](https://commonmark.org) string with a ^[custom attribute](factor: 10, other: true).
```

Without [`assumesTopLevelDictionary`](jsondecoder/assumestopleveldictionary.md), the markup would have to use explicit enclosing braces to declare the contents of the parentheses to be a dictionary:

```swift
This is a [Markdown](https://commonmark.org) string with a ^[custom attribute]({factor: 10, other: true}).
```

When you use braces, you must use matched pairs. This means that with [`assumesTopLevelDictionary`](jsondecoder/assumestopleveldictionary.md) set, the syntax `({…})` and `(…)` are both legal, but `({…)` and `(…})` are not.

## See Also

- [var keyDecodingStrategy: JSONDecoder.KeyDecodingStrategy](jsondecoder/keydecodingstrategy-swift.property.md)
  A value that determines how to decode a type’s coding keys from JSON keys.
- [JSONDecoder.KeyDecodingStrategy](jsondecoder/keydecodingstrategy-swift.enum.md)
  The values that determine how to decode a type’s coding keys from JSON keys.
- [var userInfo: [CodingUserInfoKey : any Sendable]](jsondecoder/userinfo.md)
  A dictionary you use to customize the decoding process by providing contextual information.
- [var allowsJSON5: Bool](jsondecoder/allowsjson5.md)
  Specifies that decoding supports the JSON5 syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsondecoder/assumestopleveldictionary)*