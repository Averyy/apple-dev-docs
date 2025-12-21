# NumberFormatter

**Framework**: Foundation  
**Kind**: class

A formatter that converts between numeric values and their textual representations.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NumberFormatter
```

#### Overview

Instances of [`NumberFormatter`](numberformatter.md) format the textual representation of cells that contain [`NSNumber`](nsnumber.md) objects and convert textual representations of numeric values into [`NSNumber`](nsnumber.md) objects. The representation encompasses integers, floats, and doubles; floats and doubles can be formatted to a specified decimal position. [`NumberFormatter`](numberformatter.md) objects can also impose ranges on the numeric values cells can accept.

> 💡 **Tip**:  In Swift, you can use [`IntegerFormatStyle`](integerformatstyle.md), [`FloatingPointFormatStyle`](floatingpointformatstyle.md), or [`Decimal.FormatStyle`](decimal/formatstyle.md) rather than [`NumberFormatter`](numberformatter.md). The [`FormatStyle`](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [`FormatStyle`](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

##### Significant Digits and Fraction Digits

The [`NumberFormatter`](numberformatter.md) class provides flexible options for displaying non-zero fractional parts of numbers.

If you set the [`usesSignificantDigits`](numberformatter/usessignificantdigits.md) property to [`true`](https://developer.apple.com/documentation/Swift/true), you can configure [`NumberFormatter`](numberformatter.md) to display significant digits using the [`minimumSignificantDigits`](numberformatter/minimumsignificantdigits.md) and [`maximumSignificantDigits`](numberformatter/maximumsignificantdigits.md) properties. If [`usesSignificantDigits`](numberformatter/usessignificantdigits.md) is [`false`](https://developer.apple.com/documentation/Swift/false), these properties are ignored. See Configuring Significant Digits.

Otherwise, you can configure the minimum and maximum number of integer and fraction digits, or the numbers before and after the decimal separator, respectively, using the [`minimumIntegerDigits`](numberformatter/minimumintegerdigits.md), [`maximumIntegerDigits`](numberformatter/maximumintegerdigits.md), [`minimumFractionDigits`](numberformatter/minimumfractiondigits.md), and [`maximumFractionDigits`](numberformatter/maximumfractiondigits.md) properties. See Configuring Integer and Fraction Digits.

##### Thread Safety

On iOS 7 and later [`NumberFormatter`](numberformatter.md) is thread-safe.

In macOS 10.9 and later [`NumberFormatter`](numberformatter.md) is thread-safe so long as you are using the modern behavior in a 64-bit app.

On earlier versions of the operating system, or when using the legacy formatter behavior or running in 32-bit in macOS, [`NumberFormatter`](numberformatter.md) is not thread-safe, and you therefore must not mutate a number formatter simultaneously from multiple threads.

## Topics

### Configuring Formatter Behavior and Style
- [var formatterBehavior: NumberFormatter.Behavior](numberformatter/formatterbehavior.md)
  The formatter behavior of the receiver.
- [class func setDefaultFormatterBehavior(NumberFormatter.Behavior)](numberformatter/setdefaultformatterbehavior(_:).md)
  Sets the default formatter behavior for new instances of `NSNumberFormatter` .
- [class func defaultFormatterBehavior() -> NumberFormatter.Behavior](numberformatter/defaultformatterbehavior.md)
  Returns an `NSNumberFormatterBehavior` constant that indicates default formatter behavior for new instances of `NSNumberFormatter`.
- [var numberStyle: NumberFormatter.Style](numberformatter/numberstyle.md)
  The number style used by the receiver.
- [var generatesDecimalNumbers: Bool](numberformatter/generatesdecimalnumbers.md)
  Determines whether the receiver creates instances of [`NSDecimalNumber`](nsdecimalnumber.md) when it converts strings to number objects.
### Converting Between Numbers and Strings
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, range: UnsafeMutablePointer<NSRange>?) throws](numberformatter/getobjectvalue(_:for:range:).md)
  Returns by reference a cell-content object after creating it from a range of characters in a given string.
- [func number(from: String) -> NSNumber?](numberformatter/number(from:).md)
  Returns an [`NSNumber`](nsnumber.md) object created by parsing a given string.
- [func string(from: NSNumber) -> String?](numberformatter/string(from:).md)
  Returns a string containing the formatted value of the provided number object.
- [class func localizedString(from: NSNumber, number: NumberFormatter.Style) -> String](numberformatter/localizedstring(from:number:).md)
  Returns a localized number string with the specified style.
### Managing Localization of Numbers
- [var localizesFormat: Bool](numberformatter/localizesformat.md)
  Determines whether the dollar sign character (`$`), decimal separator character (`.`), and thousand separator character (`,`) are converted to appropriately localized characters as specified by the user’s localization preference.
- [var locale: Locale!](numberformatter/locale.md)
  The locale of the receiver.
### Configuring Rounding Behavior
- [var roundingBehavior: NSDecimalNumberHandler](numberformatter/roundingbehavior.md)
  The rounding behavior used by the receiver.
- [class NSDecimalNumberHandler](nsdecimalnumberhandler.md)
  A class that adopts the decimal number behaviors protocol.
- [var roundingIncrement: NSNumber!](numberformatter/roundingincrement.md)
  The rounding increment used by the receiver.
- [var roundingMode: NumberFormatter.RoundingMode](numberformatter/roundingmode-swift.property.md)
  The rounding mode used by the receiver.
### Configuring Integer and Fraction Digits
- [var minimumIntegerDigits: Int](numberformatter/minimumintegerdigits.md)
  The minimum number of digits before the decimal separator.
- [var maximumIntegerDigits: Int](numberformatter/maximumintegerdigits.md)
  The maximum number of digits before the decimal separator.
- [var minimumFractionDigits: Int](numberformatter/minimumfractiondigits.md)
  The minimum number of digits after the decimal separator.
- [var maximumFractionDigits: Int](numberformatter/maximumfractiondigits.md)
  The maximum number of digits after the decimal separator.
### Configuring Significant Digits
- [var usesSignificantDigits: Bool](numberformatter/usessignificantdigits.md)
  A Boolean value indicating whether the formatter uses minimum and maximum significant digits when formatting numbers.
- [var minimumSignificantDigits: Int](numberformatter/minimumsignificantdigits.md)
  The minimum number of significant digits for the number formatter.
- [var maximumSignificantDigits: Int](numberformatter/maximumsignificantdigits.md)
  The maximum number of significant digits for the number formatter.
### Configuring Numeric Formats
- [var format: String](numberformatter/format.md)
  The receiver’s format.
- [var formattingContext: Formatter.Context](numberformatter/formattingcontext.md)
  The capitalization formatting context used when formatting a number.
- [var formatWidth: Int](numberformatter/formatwidth.md)
  The format width used by the receiver.
- [var negativeFormat: String!](numberformatter/negativeformat.md)
  The format the receiver uses to display negative values.
- [var positiveFormat: String!](numberformatter/positiveformat.md)
  The format the receiver uses to display positive values.
- [var multiplier: NSNumber?](numberformatter/multiplier.md)
  The multiplier of the receiver.
### Configuring Numeric Symbols
- [var percentSymbol: String!](numberformatter/percentsymbol.md)
  The string used to represent a percent symbol.
- [var perMillSymbol: String!](numberformatter/permillsymbol.md)
  The string used to represent a per-mill (per-thousand) symbol.
- [var minusSign: String!](numberformatter/minussign.md)
  The string used to represent a minus sign.
- [var plusSign: String!](numberformatter/plussign.md)
  The string used to represent a plus sign.
- [var exponentSymbol: String!](numberformatter/exponentsymbol.md)
  The string used to represent an exponent symbol.
- [var zeroSymbol: String?](numberformatter/zerosymbol.md)
  The string used to represent a zero value.
- [var nilSymbol: String](numberformatter/nilsymbol.md)
  The string used to represent a `nil` value.
- [var notANumberSymbol: String!](numberformatter/notanumbersymbol.md)
  The string used to represent a NaN (“not a number”) value.
- [var negativeInfinitySymbol: String](numberformatter/negativeinfinitysymbol.md)
  The string used to represent a negative infinity symbol.
- [var positiveInfinitySymbol: String](numberformatter/positiveinfinitysymbol.md)
  The string used to represent a positive infinity symbol.
### Configuring the Format of Currency
- [var currencySymbol: String!](numberformatter/currencysymbol.md)
  The string used by the receiver as a local currency symbol.
- [var currencyCode: String!](numberformatter/currencycode.md)
  The receiver’s currency code.
- [var internationalCurrencySymbol: String!](numberformatter/internationalcurrencysymbol.md)
  The international currency symbol used by the receiver.
- [var currencyGroupingSeparator: String!](numberformatter/currencygroupingseparator.md)
  The currency grouping separator for the receiver.
### Configuring Numeric Prefixes and Suffixes
- [var positivePrefix: String!](numberformatter/positiveprefix.md)
  The string the receiver uses as the prefix for positive values.
- [var positiveSuffix: String!](numberformatter/positivesuffix.md)
  The string the receiver uses as the suffix for positive values.
- [var negativePrefix: String!](numberformatter/negativeprefix.md)
  The string the receiver uses as a prefix for negative values.
- [var negativeSuffix: String!](numberformatter/negativesuffix.md)
  The string the receiver uses as a suffix for negative values.
### Configuring the Display of Numeric Values
- [var textAttributesForNegativeValues: [String : Any]?](numberformatter/textattributesfornegativevalues.md)
  The text attributes to be used in displaying negative values.
- [var textAttributesForPositiveValues: [String : Any]?](numberformatter/textattributesforpositivevalues.md)
  The text attributes to be used in displaying positive values.
- [var attributedStringForZero: NSAttributedString](numberformatter/attributedstringforzero.md)
  The attributed string that the receiver uses to display zero values.
- [var textAttributesForZero: [String : Any]?](numberformatter/textattributesforzero.md)
  The text attributes used to display a zero value.
- [var attributedStringForNil: NSAttributedString](numberformatter/attributedstringfornil.md)
  The attributed string the receiver uses to display `nil` values.
- [var textAttributesForNil: [String : Any]?](numberformatter/textattributesfornil.md)
  The text attributes used to display the `nil` symbol.
- [var attributedStringForNotANumber: NSAttributedString](numberformatter/attributedstringfornotanumber.md)
  The attributed string the receiver uses to display “not a number” values.
- [var textAttributesForNotANumber: [String : Any]?](numberformatter/textattributesfornotanumber.md)
  The text attributes used to display the NaN (“not a number”) string.
- [var textAttributesForPositiveInfinity: [String : Any]?](numberformatter/textattributesforpositiveinfinity.md)
  The text attributes used to display the positive infinity symbol.
- [var textAttributesForNegativeInfinity: [String : Any]?](numberformatter/textattributesfornegativeinfinity.md)
  The text attributes used to display the negative infinity symbol.
### Configuring Separators and Grouping Size
- [var groupingSeparator: String!](numberformatter/groupingseparator.md)
  The string used by the receiver for a grouping separator.
- [var usesGroupingSeparator: Bool](numberformatter/usesgroupingseparator.md)
  Determines whether the receiver displays the group separator.
- [var thousandSeparator: String!](numberformatter/thousandseparator.md)
  The character the receiver uses as a thousand separator.
- [var hasThousandSeparators: Bool](numberformatter/hasthousandseparators.md)
  Determines whether the receiver uses thousand separators.
- [var decimalSeparator: String!](numberformatter/decimalseparator.md)
  The character the receiver uses as a decimal separator.
- [var alwaysShowsDecimalSeparator: Bool](numberformatter/alwaysshowsdecimalseparator.md)
  Determines whether the receiver always shows the decimal separator, even for integer numbers.
- [var currencyDecimalSeparator: String!](numberformatter/currencydecimalseparator.md)
  The string used by the receiver as a currency decimal separator.
- [var groupingSize: Int](numberformatter/groupingsize.md)
  The grouping size of the receiver.
- [var secondaryGroupingSize: Int](numberformatter/secondarygroupingsize.md)
  The secondary grouping size of the receiver.
### Managing the Padding of Numbers
- [var paddingCharacter: String!](numberformatter/paddingcharacter.md)
  The string that the receiver uses to pad numbers in the formatted string representation.
- [var paddingPosition: NumberFormatter.PadPosition](numberformatter/paddingposition.md)
  The padding position used by the receiver.
### Managing Input and Output Attributes
- [var allowsFloats: Bool](numberformatter/allowsfloats.md)
  Determines whether the receiver allows as input floating-point values (that is, values that include the period character [`.`]).
- [var minimum: NSNumber?](numberformatter/minimum.md)
  The lowest number allowed as input by the receiver.
- [var maximum: NSNumber?](numberformatter/maximum.md)
  The highest number allowed as input by the receiver.
### Managing Leniency Behavior
- [var isLenient: Bool](numberformatter/islenient.md)
  Determines whether the receiver will use heuristics to guess at the number which is intended by a string.
### Managing the Validation of Partial Numeric Strings
- [var isPartialStringValidationEnabled: Bool](numberformatter/ispartialstringvalidationenabled.md)
  Determines whether partial string validation is enabled for the receiver.
### Constants
- [NumberFormatter.Style](numberformatter/style.md)
  The predefined number format styles used by the [`numberStyle`](numberformatter/numberstyle.md) property.
- [NumberFormatter.Behavior](numberformatter/behavior.md)
  These constants specify the behavior of a number formatter. These constants are returned by the [`defaultFormatterBehavior()`](numberformatter/defaultformatterbehavior().md) class method and the [`formatterBehavior`](numberformatter/formatterbehavior.md) property.
- [NumberFormatter.PadPosition](numberformatter/padposition.md)
  These constants are used to specify how numbers should be padded. These constants are used by the [`paddingPosition`](numberformatter/paddingposition.md) property.
- [NumberFormatter.RoundingMode](numberformatter/roundingmode-swift.enum.md)
  These constants are used to specify how numbers should be rounded. These constants are used by the [`roundingMode`](numberformatter/roundingmode-swift.property.md) property.
### Instance Properties
- [var minimumGroupingDigits: Int](numberformatter/minimumgroupingdigits.md)

## Relationships

### Inherits From
- [Formatter](formatter.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter)*