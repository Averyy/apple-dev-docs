# localizedString(forCollationIdentifier:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the localized string for the specified collation identifier.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func localizedString(forCollationIdentifier collationIdentifier: String) -> String?
```

```objc
- (NSString *) localizedStringForCollationIdentifier:(NSString *) collationIdentifier;
```

## Return Value

The localized name for the collation.

## Discussion

For example, calling this method on an American English (`en_US`) locale, passing `"phonebook"` for `collationIdentifier`, produces the string `"Phonebook Sort Order"`.

This method is equivalent to calling the [`displayName(forKey:value:)`](./displayname%28forkey,value%29.md) method passing the [`collationIdentifier`](./key/collationidentifier.md) key and `collationIdentifier` value.

## Parameters

- `collationIdentifier`: The identifier for the collation whose name you want.

## See Also

### Getting Display Information About a Locale
- [func localizedString(forLocaleIdentifier: String) -> String](./localizedstring%28forlocaleidentifier%29.md)
  Returns the localized string for the specified locale identifier.
- [func localizedString(forCountryCode: String) -> String?](./localizedstring%28forcountrycode%29.md)
  Returns the localized string for a country or region code.
- [func localizedString(forLanguageCode: String) -> String?](./localizedstring%28forlanguagecode%29.md)
  Returns the localized string for the specified language code.
- [func localizedString(forScriptCode: String) -> String?](./localizedstring%28forscriptcode%29.md)
  Returns the localized string for the specified script code.
- [func localizedString(forVariantCode: String) -> String?](./localizedstring%28forvariantcode%29.md)
  Returns the localized string for the specified variant code.
- [func localizedString(forCollatorIdentifier: String) -> String?](./localizedstring%28forcollatoridentifier%29.md)
  Returns the localized string for the specified collator identifier.
- [func localizedString(forCurrencyCode: String) -> String?](./localizedstring%28forcurrencycode%29.md)
  Returns the localized string for the specified currency code.
- [func localizedString(forCalendarIdentifier: String) -> String?](./localizedstring%28forcalendaridentifier%29.md)
  Returns the localized string for the specified calendar identifier.
- [Locale Calendar Identifiers](../locale-calendar-identifiers.md)
  The types of calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/localizedstring(forcollationidentifier:))*