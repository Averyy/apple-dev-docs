# NSTextCheckingResult

**Framework**: Foundation  
**Kind**: class

An occurrence of textual content found during the analysis of a block of text, such as when matching a regular expression.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSTextCheckingResult
```

#### Overview

On both iOS and macOS, instances of [`NSTextCheckingResult`](nstextcheckingresult.md) are returned by the [`NSRegularExpression`](nsregularexpression.md) class and the [`NSDataDetector`](nsdatadetector.md) class to indicate the discovery of content. In those cases, what is found may be a match for a regular expression or a date, address, phone number, and so on. In macOS, instances of `NSTextCheckingResult` are returned by the [`NSSpellChecker`](https://developer.apple.com/documentation/AppKit/NSSpellChecker) object to describe the results of spelling, grammar, or text-substitution actions.

## Topics

### Text Checking Type Range and Type
- [var range: NSRange](nstextcheckingresult/range.md)
  Returns the range of the result that the receiver represents.
- [var resultType: NSTextCheckingResult.CheckingType](nstextcheckingresult/resulttype.md)
  Returns the text checking result type that the receiver represents.
- [var numberOfRanges: Int](nstextcheckingresult/numberofranges.md)
  Returns the number of ranges.
- [func range(at: Int) -> NSRange](nstextcheckingresult/range(at:).md)
  Returns the result type that the range represents.
### Text Checking Results for Text Replacement
- [class func replacementCheckingResult(range: NSRange, replacementString: String) -> NSTextCheckingResult](nstextcheckingresult/replacementcheckingresult(range:replacementstring:).md)
  Creates and returns a text checking result with the specified replacement string.
- [var replacementString: String?](nstextcheckingresult/replacementstring.md)
  A replacement string from one of a number of replacement checking results.
### Text Checking Results for Regular Expressions
- [class func regularExpressionCheckingResult(ranges: NSRangePointer, count: Int, regularExpression: NSRegularExpression) -> NSTextCheckingResult](nstextcheckingresult/regularexpressioncheckingresult(ranges:count:regularexpression:).md)
  Creates and returns a type checking result with the specified regular expression data.
- [var regularExpression: NSRegularExpression?](nstextcheckingresult/regularexpression.md)
  The regular expression of a type checking result.
### Text Checking Result Components
- [var components: [NSTextCheckingKey : String]?](nstextcheckingresult/components.md)
  A dictionary containing the components of a type checking result.
### Text Checking Results for URLs
- [class func linkCheckingResult(range: NSRange, url: URL) -> NSTextCheckingResult](nstextcheckingresult/linkcheckingresult(range:url:).md)
  Creates and returns a text checking result with the specified URL.
- [var url: URL?](nstextcheckingresult/url.md)
  The URL of a type checking result.
### Text Checking Results for Addresses
- [class func addressCheckingResult(range: NSRange, components: [NSTextCheckingKey : String]) -> NSTextCheckingResult](nstextcheckingresult/addresscheckingresult(range:components:).md)
  Creates and returns a text checking result with the specified address components.
- [var addressComponents: [NSTextCheckingKey : String]?](nstextcheckingresult/addresscomponents.md)
  The address dictionary of a type checking result.
### Text Checking Results for Transit Information
- [class func transitInformationCheckingResult(range: NSRange, components: [NSTextCheckingKey : String]) -> NSTextCheckingResult](nstextcheckingresult/transitinformationcheckingresult(range:components:).md)
  Creates and returns a text checking result with the specified transit information.
### Text Checking Results for Phone Numbers
- [class func phoneNumberCheckingResult(range: NSRange, phoneNumber: String) -> NSTextCheckingResult](nstextcheckingresult/phonenumbercheckingresult(range:phonenumber:).md)
  Creates and returns a text checking result with the specified phone number.
- [var phoneNumber: String?](nstextcheckingresult/phonenumber.md)
  The phone number of a type checking result.
### Text Checking Results for Dates and Times
- [class func dateCheckingResult(range: NSRange, date: Date) -> NSTextCheckingResult](nstextcheckingresult/datecheckingresult(range:date:).md)
  Creates and returns a text checking result with the specified date.
- [class func dateCheckingResult(range: NSRange, date: Date, timeZone: TimeZone, duration: TimeInterval) -> NSTextCheckingResult](nstextcheckingresult/datecheckingresult(range:date:timezone:duration:).md)
  Creates and returns a text checking result with the specified date, time zone, and duration.
- [var date: Date?](nstextcheckingresult/date.md)
  The date component of a type checking result.
- [var duration: TimeInterval](nstextcheckingresult/duration.md)
  The duration component of a type checking result.
- [var timeZone: TimeZone?](nstextcheckingresult/timezone.md)
  The time zone component of a type checking result.
### Text Checking Results for Typography
- [class func dashCheckingResult(range: NSRange, replacementString: String) -> NSTextCheckingResult](nstextcheckingresult/dashcheckingresult(range:replacementstring:).md)
  Creates and returns a text checking result with the specified dash corrected replacement string.
- [class func quoteCheckingResult(range: NSRange, replacementString: String) -> NSTextCheckingResult](nstextcheckingresult/quotecheckingresult(range:replacementstring:).md)
  Creates and returns a text checking result with the specified quote-balanced replacement string.
### Text Checking Results for Spelling
- [class func spellCheckingResult(range: NSRange) -> NSTextCheckingResult](nstextcheckingresult/spellcheckingresult(range:).md)
  Creates and returns a text checking result with the range of a misspelled word.
- [class func correctionCheckingResult(range: NSRange, replacementString: String) -> NSTextCheckingResult](nstextcheckingresult/correctioncheckingresult(range:replacementstring:).md)
  Creates and returns a text checking result after detecting a possible correction.
### Text Checking Results for Orthography
- [class func orthographyCheckingResult(range: NSRange, orthography: NSOrthography) -> NSTextCheckingResult](nstextcheckingresult/orthographycheckingresult(range:orthography:).md)
  Creates and returns a text checking result with the specified orthography.
- [var orthography: NSOrthography?](nstextcheckingresult/orthography.md)
  The detected orthography of a type checking result.
### Text Checking Results for Grammar
- [class func grammarCheckingResult(range: NSRange, details: [[String : Any]]) -> NSTextCheckingResult](nstextcheckingresult/grammarcheckingresult(range:details:).md)
  Creates and returns a text checking result with the specified array of grammatical errors.
- [var grammarDetails: [[String : Any]]?](nstextcheckingresult/grammardetails.md)
  The details of a located grammatical type checking result.
### Adjusting the Ranges of a Text Checking Result
- [func adjustingRanges(offset: Int) -> NSTextCheckingResult](nstextcheckingresult/adjustingranges(offset:).md)
  Returns a new text checking result after adjusting the ranges as specified by the offset.
### Constants
- [Keys for Transit Components](keys-for-transit-components.md)
  The following constants identify the possible keys returned in the components dictionary.
- [Keys for Address Components](keys-for-address-components.md)
  The following constants identify the possible keys returned in the [`addressComponents`](nstextcheckingresult/addresscomponents.md) dictionary.
- [NSTextCheckingResult.CheckingType](nstextcheckingresult/checkingtype.md)
  These constants specify the type of checking the methods should do. They are returned by [`resultType`](nstextcheckingresult/resulttype.md).
- [typealias NSTextCheckingTypes](nstextcheckingtypes.md)
  Defines the types of checking that are available. These values can be combined using the C-bitwise OR operator. The system supports its own internal types, and the user can extend those types by subclassing `NSTextCheckingResult` and adding their own custom types.
- [struct NSTextCheckingKey](nstextcheckingkey.md)
- [Anonymous](1476845-anonymous.md)
### Instance Properties
- [var alternativeStrings: [String]?](nstextcheckingresult/alternativestrings.md)
### Instance Methods
- [func range(withName: String) -> NSRange](nstextcheckingresult/range(withname:).md)
### Type Methods
- [class func correctionCheckingResult(range: NSRange, replacementString: String, alternativeStrings: [String]) -> NSTextCheckingResult](nstextcheckingresult/correctioncheckingresult(range:replacementstring:alternativestrings:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)

## See Also

- [class Scanner](scanner.md)
  A string parser that scans for substrings or characters in a character set, and for numeric values from decimal, hexadecimal, and floating-point representations.
- [class NSRegularExpression](nsregularexpression.md)
  An immutable representation of a compiled regular expression that you apply to Unicode strings.
- [class NSDataDetector](nsdatadetector.md)
  A specialized regular expression object that matches natural language text for predefined data patterns.
- [let NSNotFound: Int](nsnotfound-4qp9h.md)
  A value indicating that a requested item couldn’t be found or doesn’t exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult)*