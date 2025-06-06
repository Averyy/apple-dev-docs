# NSRegularExpression

**Framework**: Foundation  
**Kind**: class

An immutable representation of a compiled regular expression that you apply to Unicode strings.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSRegularExpression
```

#### Overview

The fundamental matching method for [`NSRegularExpression`](nsregularexpression.md) is a Block iterator method that allows clients to supply a Block object which will be invoked each time the regular expression matches a portion of the target string.  There are additional convenience methods for returning all the matches as an array, the total number of matches, the first match, and the range of the first match.

An individual match is represented by an instance of the [`NSTextCheckingResult`](nstextcheckingresult.md) class, which carries information about the overall matched range (via its [`range`](nstextcheckingresult/range.md) property), and the range of each individual capture group (via the [`range(at:)`](nstextcheckingresult/range(at:).md) method).  For basic [`NSRegularExpression`](nsregularexpression.md) objects, these match results will be of type [`regularExpression`](nstextcheckingresult/checkingtype/regularexpression.md), but subclasses may use other types.

> **Note**:  [`NSRegularExpression`](nsregularexpression.md) conforms to the International Components for Unicode ([`ICU`](https://developer.apple.comhttps://unicode-org.github.io/icu/)) specification for [`regular expressions`](https://developer.apple.comhttps://unicode-org.github.io/icu/userguide/strings/regexp.html).

##### Examples Using Nsregularexpression

What follows are a set of graduated examples for using the `NSRegularExpression` class. All these examples use the regular expression `\\b(a|b)(c|d)\\b` as their regular expression.

This snippet creates a regular expression to match two-letter words, in which the first letter is “a” or “b” and the second letter is “c” or “d”. Specifying [`caseInsensitive`](nsregularexpression/options-swift.struct/caseinsensitive.md) means that matches will be case-insensitive, so this will match “BC”, “aD”, and so forth, as well as their lower-case equivalents.

The [`numberOfMatches(in:options:range:)`](nsregularexpression/numberofmatches(in:options:range:).md) method provides a simple mechanism for counting the number of matches in a given range of a string.

If you are interested only in the overall range of the first match, the [`rangeOfFirstMatch(in:options:range:)`](nsregularexpression/rangeoffirstmatch(in:options:range:).md) method provides it for you.  Some regular expressions (though not the example pattern) can successfully match a zero-length range, so the comparison of the resulting range with `{NSNotFound, 0}` is the most reliable way to determine whether there was a match or not.

The example regular expression contains two capture groups, corresponding to the two sets of parentheses, one for the first letter, and one for the second.  If you are interested in more than just the overall matched range, you want to obtain an [`NSTextCheckingResult`](nstextcheckingresult.md) object corresponding to a given match.  This object provides information about the overall matched range, via its [`range`](nstextcheckingresult/range.md) property, and also supplies the capture group ranges, via the [`range(at:)`](nstextcheckingresult/range(at:).md) method.  The first capture group range is given by `[result rangeAtIndex:1]`, the second by `[result rangeAtIndex:2]`.  Sending a result the  [`range(at:)`](nstextcheckingresult/range(at:).md) message and passing `0` is equivalent to `[result range]`.

If the result returned is non-`nil`, then `[result range]` will always be a valid range, so it is not necessary to compare it against `{NSNotFound, 0}`.  However, for some regular expressions (though not the example pattern) some capture groups may or may not participate in a given match.  If a given capture group does not participate in a given match, then `[result rangeAtIndex:idx]` will return `{NSNotFound, 0}`.

The [`matches(in:options:range:)`](nsregularexpression/matches(in:options:range:).md) returns all the matching results.

The [`firstMatch(in:options:range:)`](nsregularexpression/firstmatch(in:options:range:).md) method is similar to [`matches(in:options:range:)`](nsregularexpression/matches(in:options:range:).md) but it returns only the first match.

The Block enumeration method [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md) is the most general and flexible of the matching methods of `NSRegularExpression`.  It allows you to iterate through matches in a string, performing arbitrary actions on each as specified by the code in the Block and to stop partway through if desired.  In the following example case, the iteration is stopped after a certain number of matches have been found.

If neither of the special options [`reportProgress`](nsregularexpression/matchingoptions/reportprogress.md) or [`reportCompletion`](nsregularexpression/matchingoptions/reportcompletion.md) is specified, then the result argument to the Block is guaranteed to be non-`nil`, and as mentioned before, it is guaranteed to have a valid overall range.  See [`NSRegularExpression.MatchingOptions`](nsregularexpression/matchingoptions.md) for the significance of [`reportProgress`](nsregularexpression/matchingoptions/reportprogress.md) or [`reportCompletion`](nsregularexpression/matchingoptions/reportcompletion.md).

`NSRegularExpression` also provides simple methods for performing find-and-replace operations on a string.  The following example returns a modified copy, but there is a corresponding method for modifying a mutable string in place.  The template specifies what is to be used to replace each match, with `$0` representing the contents of the overall matched range, `$1` representing the contents of the first capture group, and so on.  In this case, the template reverses the two letters of the word.

##### Concurrency and Thread Safety

`NSRegularExpression` is designed to be immutable and thread safe, so that a single instance can be used in matching operations on multiple threads at once.  However, the string on which it is operating should not be mutated during the course of a matching operation, whether from another thread or from within the Block used in the iteration.

##### Regular Expression Syntax

The following tables describe the character expressions used by the regular expression to match patterns within a string, the pattern operators that specify how many times a pattern is matched and additional matching restrictions, and the last table specifies flags that can be included in the regular expression pattern that specify search behavior over multiple lines (these flags can also be specified using the [`NSRegularExpression.Options`](nsregularexpression/options-swift.struct.md) option flags.

###### Regular Expression Metacharacters

Table 1: Character sequences used to match characters within a string.

| Character Expression | Description |
| --- | --- |
| `\a` | Match a BELL, `\u0007` |
| `\A` | Match at the beginning of the input. Differs from `^` in that `\A` will not match after a new line within the input. |
| `\b, outside of a [Set]` | Match if the current position is a word boundary. Boundaries occur at the transitions between word (`\w`) and non-word (`\W`) characters, with combining marks ignored. For better word boundaries, see [`useUnicodeWordBoundaries`](nsregularexpression/options-swift.struct/useunicodewordboundaries.md). |
| `\b, within a [Set]` | Match a BACKSPACE, `\u0008`. |
| `\B` | Match if the current position is not a word boundary. |
| `\cX` | Match a `control-X` character |
| `\d` | Match any character with the Unicode General Category of Nd (Number, Decimal Digit.) |
| `\D` | Match any character that is not a decimal digit. |
| `\e` | Match an `ESCAPE`, `\u001B`. |
| `\E` | Terminates a `\Q ... \E` quoted sequence. |
| `\f` | Match a FORM FEED, `\u000C`. |
| `\G` | Match if the current position is at the end of the previous match. |
| `\n` | Match a `LINE FEED`, `\u000A`. |
| `\N{``}` | Match the named character. |
| `\p{``}` | Match any character with the specified Unicode Property. |
| `\P{``}` | Match any character not having the specified Unicode Property. |
| `\Q` | Quotes all following characters until `\E`. |
| `\r` | Match a CARRIAGE RETURN, \u000D. |
| `\s` | Match a white space character. White space is defined as [\t\n\f\r\p{Z}]. |
| `\S` | Match a non-white space character. |
| `\t` | Match a HORIZONTAL TABULATION, `\u0009`. |
| `\u` | Match the character with the hex value . |
| `\U` | Match the character with the hex value . Exactly eight hex digits must be provided, even though the largest Unicode code point is `\U0010ffff`. |
| `\w` | Match a word character. Word characters are [\p{Ll}\p{Lu}\p{Lt}\p{Lo}\p{Nd}]. |
| `\W` | Match a non-word character. |
| `\x{``}` | Match the character with hex value . From one to six hex digits may be supplied. |
| `\x` | Match the character with two digit hex value . |
| `\X` | Match a Grapheme Cluster. |
| `\Z` | Match if the current position is at the end of input, but before the final line terminator, if one exists. |
| `\z` | Match if the current position is at the end of input. |
| `\` | Back Reference. Match whatever the _n_th capturing group matched.  must be a number `≥ 1` and `≤` total number of capture groups in the pattern. |
| `\0` | Match an Octal character.   is from one to three octal digits.  `0377` is the largest allowed Octal character.  The leading zero is required; it distinguishes Octal constants from back references. |
| `[``]` | Match any one character from the pattern. |
| `.` | Match any character. See [`dotMatchesLineSeparators`](nsregularexpression/options-swift.struct/dotmatcheslineseparators.md) and the `s` character expression in Table 4. |
| `^` | Match at the beginning of a line. See [`anchorsMatchLines`](nsregularexpression/options-swift.struct/anchorsmatchlines.md) and the `\m` character expression in Table 4. |
| `$` | Match at the end of a line. See [`anchorsMatchLines`](nsregularexpression/options-swift.struct/anchorsmatchlines.md) and the `m` character expression in Table 4. |
| `\` | Quotes the following character. Characters that must be quoted to be treated as literals are `* ? + [ ( ) { } ^ $ |

###### Regular Expression Operators

Table 2: Regular expression operators.

| Operator | Description |
| --- | --- |
| ` | ` |
| `*` | Match `0` or more times. Match as many times as possible. |
| `+` | Match `1` or more times. Match as many times as possible. |
| `?` | Match zero or one times. Prefer one. |
| `{``}` | Match exactly  times. |
| `{``,}` | Match at least  times. Match as many times as possible. |
| `{``,``}` | Match between  and  times. Match as many times as possible, but not more than . |
| `*?` | Match `0` or more times. Match as few times as possible. |
| `+?` | Match 1 or more times. Match as few times as possible. |
| `??` | Match zero or one times. Prefer zero. |
| `{``}?` | Match exactly n times. |
| `{``,}?` | Match at least n times, but no more than required for an overall pattern match. |
| `{``,``}?` | Match between n and m times. Match as few times as possible, but not less than n. |
| `*+` | Match 0 or more times. Match as many times as possible when first encountered. Do not retry with fewer, even if overall match fails (possessive match). |
| `++` | Match 1 or more times (possessive match). |
| `?+` | Match zero or one times (possessive match). |
| `{``}+` | Match exactly  times. |
| `{``,}+` | Match at least  times (possessive match). |
| `{``,``}+` | Match between  and  times (possessive match). |
| `(``)` | Capturing parentheses. Range of input that matched the parenthesized subexpression is available after the match. |
| `(?:``)` | Non-capturing parentheses. Groups the included pattern, but does not provide capturing of matching text. Somewhat more efficient than capturing parentheses. |
| `(?>``)` | Atomic-match parentheses. First match of the parenthesized subexpression is the only one tried; if it does not lead to an overall pattern match, back up the search for a match to a position before the “`(?>`” |
| `(?# ... )` | Free-format comment `(?# comment )`. |
| `(?= ... )` | Look-ahead assertion. True if the parenthesized pattern matches at the current input position, but does not advance the input position. |
| `(?! ... )` | Negative look-ahead assertion. True if the parenthesized pattern does not match at the current input position. Does not advance the input position. |
| `(?<= ... )` | Look-behind assertion. True if the parenthesized pattern matches text preceding the current input position, with the last character of the match being the input character just before the current position. Does not alter the input position. The length of possible strings matched by the look-behind pattern must not be unbounded (no * or + operators.) |
| `(?<! ... )` | Negative Look-behind assertion. True if the parenthesized pattern does not match text preceding the current input position, with the last character of the match being the input character just before the current position. Does not alter the input position. The length of possible strings matched by the look-behind pattern must not be unbounded (no * or + operators.) |
| `(?ismwx-ismwx:` `...` `)` | Flag settings. Evaluate the parenthesized expression with the specified flags enabled or -disabled. The flags are defined in [`Flag Options`](nsregularexpression#Flag-Options.md). |
| `(?ismwx-ismwx)` | Flag settings. Change the flag settings. Changes apply to the portion of the pattern following the setting. For example, (?i) changes to a case insensitive match.The flags are defined in [`Flag Options`](nsregularexpression#Flag-Options.md). |

###### Template Matching Format

The `NSRegularExpression` class provides find-and-replace methods for both immutable and mutable strings using the technique of template matching.

Table 3: Find-and-replace syntax.

| Character | Descriptions |
| --- | --- |
| `$` | The text of capture group n will be substituted for $.  must be `>= 0` and not greater than the number of capture groups. A `$` not followed by a digit has no special meaning, and will appear in the substitution text as itself, a `$`. |
| `\` | Treat the following character as a literal, suppressing any special meaning. Backslash escaping in substitution text is only required for ‘$’ and ’', but may be used on any other character without bad effects. |

The replacement string is treated as a template, with `$0` being replaced by the contents of the matched range, `$1` by the contents of the first capture group, and so on.  Additional digits beyond the maximum required to represent the number of capture groups will be treated as ordinary characters, as will a `$` not followed by digits.  Backslash will escape both `$` and `\`.

###### Flag Options

The following flags control various aspects of regular expression matching. These flag values may be specified within the pattern using the `(?ismx-ismx)` pattern options.  Equivalent behaviors can be specified for the entire pattern when an `NSRegularExpression` is initialized, using the [`NSRegularExpression.Options`](nsregularexpression/options-swift.struct.md) option flags.

Table 4: Regular expression matching flags.

| Flag (Pattern) | Description |
| --- | --- |
| i | If set, matching will take place in a case-insensitive manner. |
| x | If set, allow use of white space and #comments within patterns |
| s | If set, a “`.`” in a pattern will match a line terminator in the input text. By default, it will not. Note that a `carriage-return / line-feed pair` in text behave as a single line terminator, and will match a single “`.`” in a regular expression pattern |
| m | Control the behavior of “`^`” and “`$`” in a pattern. By default these will only match at the start and end, respectively, of the input text. If this flag is set, “`^`” and “`$`” will also match at the start and end of each line within the input text. |
| w | Controls the behavior of `\b` in a pattern. If set, word boundaries are found according to the definitions of word found in Unicode UAX 29, Text Boundaries. By default, word boundaries are identified by means of a simple classification of characters as either “word” or “non-word”, which approximates traditional regular expression behavior. The results obtained with the two options can be quite different in runs of spaces and other non-word characters. |

##### Performance

`NSRegularExpression` implements a nondeterministic finite automaton matching engine. As such, complex regular expression patterns containing multiple `*` or `+` operators may result in poor performance when attempting to perform matches — particularly failing to match a given input. For more information, see the [`“Performance Tips” section of the ICU User Guide`](https://developer.apple.comhttp://userguide.icu-project.org/strings/regexp#TOC-Performance-Tips).

##### Icu License

Tables 1, 2, 3, and 4 are reproduced from the ICU User Guide, Copyright (c) 2000 - 2009 IBM and Others, which are licensed under the following terms:

COPYRIGHT AND PERMISSION NOTICE

Copyright (c) 1995-2009 International Business Machines Corporation and others. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, provided that the above copyright notice(s) and this permission notice appear in all copies of the Software and that both the above copyright notice(s) and this permission notice appear in supporting documentation.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT OF THIRD PARTY RIGHTS. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR HOLDERS INCLUDED IN THIS NOTICE BE LIABLE FOR ANY CLAIM, OR ANY SPECIAL INDIRECT OR CONSEQUENTIAL DAMAGES, OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

Except as contained in this notice, the name of a copyright holder shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization of the copyright holder.

All trademarks and registered trademarks mentioned herein are the property of their respective owners.

## Topics

### Creating Regular Expressions
- [init(pattern: String, options: NSRegularExpression.Options) throws](nsregularexpression/init(pattern:options:).md)
  Returns an initialized NSRegularExpression instance with the specified regular expression pattern and options.
### Getting the Regular Expression and Options
- [var pattern: String](nsregularexpression/pattern.md)
  Returns the regular expression pattern.
- [var options: NSRegularExpression.Options](nsregularexpression/options-swift.property.md)
  Returns the options used when the regular expression option was created.
- [var numberOfCaptureGroups: Int](nsregularexpression/numberofcapturegroups.md)
  Returns the number of capture groups in the regular expression.
### Searching Strings Using Regular Expressions
- [func numberOfMatches(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange) -> Int](nsregularexpression/numberofmatches(in:options:range:).md)
  Returns the number of matches of the regular expression within the specified range of the string.
- [func enumerateMatches(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange, using: (NSTextCheckingResult?, NSRegularExpression.MatchingFlags, UnsafeMutablePointer<ObjCBool>) -> Void)](nsregularexpression/enumeratematches(in:options:range:using:).md)
  Enumerates the string allowing the Block to handle each regular expression match.
- [func matches(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange) -> [NSTextCheckingResult]](nsregularexpression/matches(in:options:range:).md)
  Returns an array containing all the matches of the regular expression in the string.
- [func firstMatch(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange) -> NSTextCheckingResult?](nsregularexpression/firstmatch(in:options:range:).md)
  Returns the first match of the regular expression within the specified range of the string.
- [func rangeOfFirstMatch(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange) -> NSRange](nsregularexpression/rangeoffirstmatch(in:options:range:).md)
  Returns the range of the first match of the regular expression within the specified range of the string.
### Replacing Strings Using Regular Expressions
- [func replaceMatches(in: NSMutableString, options: NSRegularExpression.MatchingOptions, range: NSRange, withTemplate: String) -> Int](nsregularexpression/replacematches(in:options:range:withtemplate:).md)
  Replaces regular expression matches within the mutable string using the template string.
- [func stringByReplacingMatches(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange, withTemplate: String) -> String](nsregularexpression/stringbyreplacingmatches(in:options:range:withtemplate:).md)
  Returns a new string containing matching regular expressions replaced with the template string.
### Escaping Characters in a String
- [class func escapedTemplate(for: String) -> String](nsregularexpression/escapedtemplate(for:).md)
  Returns a template string by adding backslash escapes as necessary to protect any characters that would match as pattern metacharacters
- [class func escapedPattern(for: String) -> String](nsregularexpression/escapedpattern(for:).md)
  Returns a string by adding backslash escapes as necessary to protect any characters that would match as pattern metacharacters.
### Custom Replace Functionality
- [func replacementString(for: NSTextCheckingResult, in: String, offset: Int, template: String) -> String](nsregularexpression/replacementstring(for:in:offset:template:).md)
  Used to perform template substitution for a single result for clients implementing their own replace functionality.
### Constants
- [NSRegularExpression.Options](nsregularexpression/options-swift.struct.md)
  These constants define the regular expression options. These constants are used by the property [`options`](nsregularexpression/options-swift.property.md), [`regularExpressionWithPattern:options:error:`](nsregularexpression/regularexpressionwithpattern:options:error:.md), and [`init(pattern:options:)`](nsregularexpression/init(pattern:options:).md).
- [NSRegularExpression.MatchingFlags](nsregularexpression/matchingflags.md)
  Set by the Block as the matching progresses, completes, or fails. Used by the method [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md).
- [NSRegularExpression.MatchingOptions](nsregularexpression/matchingoptions.md)
  The matching options constants specify the reporting, completion and matching rules to the expression matching methods. These constants are used by all methods that search for, or replace values, using a regular expression.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSDataDetector](nsdatadetector.md)
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
- [Sendable](../Swift/Sendable.md)

## See Also

- [class Scanner](scanner.md)
  A string parser that scans for substrings or characters in a character set, and for numeric values from decimal, hexadecimal, and floating-point representations.
- [class NSDataDetector](nsdatadetector.md)
  A specialized regular expression object that matches natural language text for predefined data patterns.
- [class NSTextCheckingResult](nstextcheckingresult.md)
  An occurrence of textual content found during the analysis of a block of text, such as when matching a regular expression.
- [let NSNotFound: Int](nsnotfound-4qp9h.md)
  A value indicating that a requested item couldn’t be found or doesn’t exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Foundation/nsregularexpression)*