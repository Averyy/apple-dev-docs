# style

**Framework**: Foundation  
**Kind**: property

Specifies the style of the formatted result.

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
var style: PersonNameComponents.FormatStyle.Style
```

#### Discussion

The style property controls length of the string representation of the name.

For example:

```swift
var tlc = PersonNameComponents()
tlc.familyName = "Clark"
tlc.givenName = "Thomas"
tlc.middleName = "Louis"
tlc.namePrefix = "Dr."
tlc.nickname = "Tom"
tlc.nameSuffix = "Esq."

let longFormatStyle = PersonNameComponents.FormatStyle(style: .long, locale: Locale(identifier: "us_EN"))
print(tlc.formatted(longFormatStyle)) // Dr. Thomas Louis Clark Esq.
        
let mediumFormatStyle = PersonNameComponents.FormatStyle(style: .medium, locale: Locale(identifier: "us_EN"))
print(tlc.formatted(mediumFormatStyle)) // Thomas Clark
        
let shortFormatStyle = PersonNameComponents.FormatStyle(style: .short, locale: Locale(identifier: "us_EN"))
print(tlc.formatted(shortFormatStyle)) // Tom
        
let abbrevFormatStyle = PersonNameComponents.FormatStyle(style: .abbreviated, locale: Locale(identifier: "us_EN"))
print(tlc.formatted(abbrevFormatStyle)) // TC

let defaultFormatStyle = PersonNameComponents.FormatStyle(locale: Locale(identifier: "us_EN"))
print(tlc.formatted(defaultFormatStyle)) // Thomas Clark
```

The default value is `medium`.

##### Styles

You can configure `PersonNameComponents.FormatStyle` to format names in the following styles:

The following table demonstrates the style for various names and locales.

| Locale | Name prefix | Given name | Middle name | Family name | Name suffix | Nickname |
| --- | --- | --- | --- | --- | --- | --- |
| Arabic ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(ar-SA)` | .د | أحمد |  | محمدالمصري |  |  |
| Chinese ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(zh-Hans)` | 物理学博士 | 振宁 |  | 杨 | 先生 |  |
| English ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(en-US)` | Dr. | Thomas | Louis | Clark | Esq. | Tom |
| French ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(fr-FR)` | Père | Jean-Philippe |  | de Zélicourt |  | JP |
| German ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(de-DE)` | Dr. med. | Max |  | Mustermann | junior, M.A. |  |
| Hindi ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(hi-IN)` | डॉ. | रिय |  | साहिल |  |  |
| Japanese ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(ja-JP)` |  | 泰夫 |  | 木田 | 先生 |  |
| Spanish ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(es-ES)` | Dr. | José Ramiro |  | Martín González de Rivera | júnior, PhD | Ramiro |
| Thai ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(th-TH)` | ฯพณฯ | สมชาย | ปีเตอร์ | รัตนเรืองรองบวรทิพย์ |  |  |

###### Long

The Long style provides the most explicit representation of names. It uses all available name components, with the exception of nickname.

| Locale | Long style |
| --- | --- |
| Arabic (ar-SA) | ﺩ. أحمد محمﺩﺍلمصﺭﻱ |
| Chinese (zh-Hans) | 物理学博士杨振宁先生 |
| English (en-US) | Dr. Thomas Louis Clark Esq. |
| French (fr-FR) | Père Jean-Philippe de Zélicourt |
| German (de-DE) | Dr. med. Max Mustermann junior, M.A. |
| Hindi (hi-IN) | डॉ. रिय साहिल |
| Japanese (ja-JP) | 木田泰夫先生 |
| Spanish (es-ES) | Dr. José Ramiro Martín González de Rivera júnior, PhD |
| Thai (th-TH) | ฯพณฯ สมชาย ปีเตอร์ รัตนเรืองรอง บวรทิพย์ |

###### Medium

The Medium, or default, style presents names in a way that is suitable for most contexts. It uses the given and family names, as well as a nickname, if provided, and enabled by the user.

| Locale | Default style |
| --- | --- |
| Arabic (ar-SA) | أحمد محمﺩﺍلمصﺭﻱ |
| Chinese (zh-Hans) | 杨振宁 |
| English (en-US) | Thomas Clark |
| French (fr-FR) | Jean-Philippe de Zélicourt |
| German (de-DE) | Max Mustermann |
| Hindi (hi-IN) | रिय साहिल |
| Japanese (ja-JP) | 木田泰夫 |
| Spanish (es-ES) | José Ramiro Martín González de Rivera |
| Thai (th-TH) | สมชาย รัตนเรืองรอง บวรทิพย์ |

###### Short

The Short style offers an alternative display method for names whose default representation may exceed a certain length constraint. Users customize how the system displays short names in the preferences for the Contacts app. For scripts that don’t support Short name, or cases where the specified Short style is unavailable, the format uses Medium style.

The table below shows the formatted string output for each Short Name configuration and for a variety of locales:

| Locale | Given name - family initial | Given initial - family name | Given name only | Family name only |
| --- | --- | --- | --- | --- |
| Arabic (ar-SA) |  |  | أحمد | محمﺩﺍلمصﺭﻱ |
| Chinese (zh-Hans) |  |  |  |  |
| English (en-US) | Thomas C | T Clark | Thomas | Clark |
| French (fr-FR) | Jean-Philippe d | J de Zélicourt | Jean-Philippe | de Zélicourt |
| German (de-DE) | Max M | M Mustermann | Max | Mustermann |
| Hindi (hi-IN) |  |  | रिय | साहिल |
| Japanese (ja-JP) |  |  |  |  |
| Spanish (es-ES) | José Ramiro M | J Martín González de Rivera | José Ramiro | Martín González de Rivera |
| Thai (th-TH) | สมชาย ร | ส รัตนเรืองรองบวรทิพย์ | สมชาย | รัตนเรืองรองบวรทิพย์ |

> ❗ **Important**:  `PersonNameComponents.FormatStyle` doesn’t account for prepositional particles. Representations using the Short style that specify a family name initial naively use the first letter unit of the particle as the initial.

 `PersonNameComponents.FormatStyle` doesn’t account for prepositional particles. Representations using the Short style that specify a family name initial naively use the first letter unit of the particle as the initial.

###### Abbreviated

The Abbreviated style offers the most compact representation of names, similar to a monogram.

Abbreviated style is supported for names in several scripts, with the following general characteristics:

- For names in Cyrillic, Greek, or Latin script, the first characters of `givenName`, `middleName`, and `familyName` may be used.
- For names in Chinese or Japanese script, `familyName` may be used. If `familyName` is too long, or if the family name is `nil`, the Short or Medium style may be used instead.
- For names in Korean script, `givenName` may be used. If `givenName` is too long, the first character of `givenName` may be used. If `givenName` is `nil`, the `familyName` may be used instead.
- For names in Bengali, Devanagari, Gujarati, Gurmukhi, Kannada, Malayalam, Oriya, Sinhala, Tamil, Telugu, Tibetan, or Thai script, the first character of `givenName` may be used. If `givenName` is `nil`, the first character of `familyName` may be used instead.
- For names that contain more than one script, the abbreviated style may use the `familyName`, `givenName`, or the first characters of `givenName` and/or `familyName`.

If the Abbreviated style is unavailable, the Short style is used instead—unless that too is unsupported, in which case the Medium style is used instead.

| Locale | Abbreviated style |
| --- | --- |
| Arabic (ar-SA) | N/A |
| Chinese (zh-Hans) | 杨 |
| English (en-US) | TLC |
| French (fr-FR) | Jd |
| German (de-DE) | MM |
| Hindi (hi-IN) | मि |
| Japanese (ja-JP) | 木田 |
| Spanish (es-ES) | JM |
| Thai (th-TH) | ส |

> ❗ **Important**:  `PersonNameComponents.FormatStyle` doesn’t account for prepositional particles or compound names. Representations using the Abbreviated style uses the first letter unit of each name component, regardless.

 `PersonNameComponents.FormatStyle` doesn’t account for prepositional particles or compound names. Representations using the Abbreviated style uses the first letter unit of each name component, regardless.

## See Also

- [PersonNameComponents.FormatStyle.Style](personnamecomponents/formatstyle/style-swift.enum.md)
  The type that represents the style of the formatted result.
- [var locale: Locale](personnamecomponents/formatstyle/locale.md)
  The locale to use when formatting the person name components.
- [var attributed: PersonNameComponents.AttributedStyle](personnamecomponents/formatstyle/attributed.md)
  The style used to create a locale-aware attributed string representation of an instance of person name components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/personnamecomponents/formatstyle/style-swift.property)*