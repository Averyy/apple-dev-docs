# Scanner

**Framework**: Foundation  
**Kind**: class

A string parser that scans for substrings or characters in a character set, and for numeric values from decimal, hexadecimal, and floating-point representations.

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
class Scanner
```

#### Overview

A [`Scanner`](scanner.md) object interprets and converts the characters of a [`String`](https://developer.apple.com/documentation/Swift/String) into number and string values. You assign the scanner’s string when you create the scanner, and the scanner progresses through the characters of that string from beginning to end as you request items.

Because of the nature of class clusters, a scanner object isn’t an actual instance of the [`Scanner`](scanner.md) class, but is one of its private subclasses. Although a scanner object’s class is private, its interface is public, as declared by this abstract superclass, [`Scanner`](scanner.md). The objects you create using this class are referred to as scanner objects (and when no confusion will result, merely as scanners).

To set a [`Scanner`](scanner.md) object to ignore a set of characters as it scans the string, use the [`charactersToBeSkipped`](scanner/characterstobeskipped.md) property. Characters in the skip set are skipped over before the target is scanned. The default set of characters to skip is the whitespace and newline character set.

To retrieve the unscanned remainder of the string, use `scanner.string.substring(from: scanner.scanLocation)`.

## Topics

### Creating a Scanner
- [class func localizedScanner(with: String) -> Any](scanner/localizedscanner(with:).md)
  Returns an `NSScanner` object that scans a given string according to the user’s default locale.
- [init(string: String)](scanner/init(string:).md)
  Returns an `NSScanner` object initialized to scan a given string.
### Getting a Scanner’s String
- [var string: String](scanner/string.md)
  The string the scanner will scan.
### Configuring a Scanner
- [var scanLocation: Int](scanner/scanlocation.md)
  The character position at which the receiver will begin its next scanning operation.
- [var caseSensitive: Bool](scanner/casesensitive.md)
  Flag that indicates whether the receiver distinguishes case in the characters it scans.
- [var charactersToBeSkipped: CharacterSet?](scanner/characterstobeskipped.md)
  Character set containing the characters the scanner ignores when looking for a scannable element.
- [var locale: Any?](scanner/locale.md)
  The locale to use when scanning.
### Scanning Characters and Strings
- [func scanCharacters(from: CharacterSet, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](scanner/scancharacters(from:into:).md)
  Scans the string as long as characters from a given character set are encountered, accumulating characters into a string that’s returned by reference.
- [func scanUpToCharacters(from: CharacterSet, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](scanner/scanuptocharacters(from:into:).md)
  Scans the string until a character from a given character set is encountered, accumulating characters into a string that’s returned by reference.
- [func scanString(String, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](scanner/scanstring(_:into:).md)
  Scans a given string, returning an equivalent string object by reference if a match is found.
- [func scanUpTo(String, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](scanner/scanupto(_:into:).md)
  Scans the string until a given string is encountered, accumulating characters into a string that’s returned by reference.
### Scanning Numeric Values
- [func scanDecimal(UnsafeMutablePointer<Decimal>?) -> Bool](scanner/scandecimal(_:).md)
  Scans for an `NSDecimal` value, returning a found value by reference.
- [func scanDouble(UnsafeMutablePointer<Double>?) -> Bool](scanner/scandouble(_:).md)
  Scans for a double value, returning a found value by reference.
- [func scanFloat(UnsafeMutablePointer<Float>?) -> Bool](scanner/scanfloat(_:).md)
  Scans for a float value, returning a found value by reference.
- [func scanHexDouble(UnsafeMutablePointer<Double>?) -> Bool](scanner/scanhexdouble(_:).md)
  Scans for a double value from a hexadecimal representation, returning a found value by reference.
- [func scanHexFloat(UnsafeMutablePointer<Float>?) -> Bool](scanner/scanhexfloat(_:).md)
  Scans for a double value from a hexadecimal representation, returning a found value by reference.
- [func scanHexInt32(UnsafeMutablePointer<UInt32>?) -> Bool](scanner/scanhexint32(_:).md)
  Scans for an unsigned value from a hexadecimal representation, returning a found value by reference.
- [func scanHexInt64(UnsafeMutablePointer<UInt64>?) -> Bool](scanner/scanhexint64(_:).md)
  Scans for a long long value from a hexadecimal representation, returning a found value by reference.
- [func scanInt(UnsafeMutablePointer<Int>?) -> Bool](scanner/scanint(_:).md)
  Scans for an NSInteger value from a decimal representation, returning a found value by reference
- [func scanInt32(UnsafeMutablePointer<Int32>?) -> Bool](scanner/scanint32(_:).md)
  Scans for an int value from a decimal representation, returning a found value by reference.
- [func scanInt64(UnsafeMutablePointer<Int64>?) -> Bool](scanner/scanint64(_:).md)
  Scans for a long long value from a decimal representation, returning a found value by reference.
- [func scanUnsignedLongLong(UnsafeMutablePointer<UInt64>?) -> Bool](scanner/scanunsignedlonglong(_:).md)
  Scans for an unsigned long long value from a decimal representation, returning a found value by reference.
### Monitoring Scanner Progress
- [var isAtEnd: Bool](scanner/isatend.md)
  Flag that indicates whether the receiver has exhausted all significant characters.
### Instance Properties
- [var currentIndex: String.Index](scanner/currentindex.md)
### Instance Methods
- [func scanCharacter() -> Character?](scanner/scancharacter.md)
- [func scanCharacters(from: CharacterSet) -> String?](scanner/scancharacters(from:).md)
- [func scanDecimal() -> Decimal?](scanner/scandecimal.md)
- [func scanDouble(representation: Scanner.NumberRepresentation) -> Double?](scanner/scandouble(representation:).md)
- [func scanFloat(representation: Scanner.NumberRepresentation) -> Float?](scanner/scanfloat(representation:).md)
- [func scanInt(representation: Scanner.NumberRepresentation) -> Int?](scanner/scanint(representation:).md)
- [func scanInt32(representation: Scanner.NumberRepresentation) -> Int32?](scanner/scanint32(representation:).md)
- [func scanInt64(representation: Scanner.NumberRepresentation) -> Int64?](scanner/scanint64(representation:).md)
- [func scanString(String) -> String?](scanner/scanstring(_:).md)
- [func scanUInt64(representation: Scanner.NumberRepresentation) -> UInt64?](scanner/scanuint64(representation:).md)
- [func scanUpToCharacters(from: CharacterSet) -> String?](scanner/scanuptocharacters(from:).md)
- [func scanUpToString(String) -> String?](scanner/scanuptostring(_:).md)
### Enumerations
- [Scanner.NumberRepresentation](scanner/numberrepresentation.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSRegularExpression](nsregularexpression.md)
  An immutable representation of a compiled regular expression that you apply to Unicode strings.
- [class NSDataDetector](nsdatadetector.md)
  A specialized regular expression object that matches natural language text for predefined data patterns.
- [class NSTextCheckingResult](nstextcheckingresult.md)
  An occurrence of textual content found during the analysis of a block of text, such as when matching a regular expression.
- [let NSNotFound: Int](nsnotfound-4qp9h.md)
  A value indicating that a requested item couldn’t be found or doesn’t exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner)*