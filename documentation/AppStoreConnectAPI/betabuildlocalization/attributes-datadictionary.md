# BetaBuildLocalization.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe a Beta Build Localizations resource.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaBuildLocalization.Attributes
```

#### Discussion

Table 1 lists allowed locale values.

| `da` | Danish |
| --- | --- |
| `de-DE` | German |
| `el` | Greek |
| `en-AU` | English (Australia) |
| `en-CA` | English (Canada) |
| `en-GB` | English (U.K.) |
| `en-US` | English (U.S.) |
| `es-ES` | Spanish (Spain) |
| `es-MX` | Spanish (Mexico) |
| `fi` | Finnish |
| `fr-CA` | French (Canada) |
| `fr-FR` | French |
| `id` | Indonesian |
| `it` | Italian |
| `ja` | Japanese |
| `ko` | Korean |
| `ms` | Malay |
| `nl-NL` | Dutch |
| `no` | Norwegian |
| `pt-BR` | Portuguese (Brazil) |
| `pt-PT` | Portuguese (Portugal) |
| `ru` | Russian |
| `sv` | Swedish |
| `th` | Thai |
| `tr` | Turkish |
| `vi` | Vietnamese |
| `zh-Hans` | Chinese (Simplified) |
| `zh-Hant` | Chinese (Traditional) |

## Properties

- `locale` (string): The specified locale. To learn more, see [`Managing metadata in your app by using locale shortcodes`](managing-metadata-in-your-app-by-using-locale-shortcodes.md).
- `whatsNew` (string): A field that describes changes and additions to a build and indicates features you would like your users to test.

## See Also

- [Beta Build Localizations](beta-build-localizations.md)
  Beta test information about builds, specific to a locale.
- [object BetaBuildLocalization.Relationships](betabuildlocalization/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betabuildlocalization/attributes-data.dictionary)*