# localizesFormat

**Framework**: Foundation  
**Kind**: property

Determines whether the dollar sign character (`$`), decimal separator character (`.`), and thousand separator character (`,`) are converted to appropriately localized characters as specified by the user’s localization preference.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var localizesFormat: Bool { get set }
```

#### Discussion

While the currency-symbol part of this feature may be useful in certain types of applications, it’s probably more likely that you would tie a particular application to a particular currency (that is, that you would “hard-code” the currency symbol and separators instead of having them dynamically change based on the user’s configuration). The reason for this, of course, is that `NSNumberFormatter` doesn’t perform currency conversions, it just formats numeric data. You wouldn’t want one user interpreting the value `"56324"` as US currency and another user who’s accessing the same data interpreting it as Japanese currency, simply based on each user’s localization preferences.

## See Also

- [var locale: Locale!](numberformatter/locale.md)
  The locale of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/localizesformat)*