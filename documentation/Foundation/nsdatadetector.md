# NSDataDetector

**Framework**: Foundation  
**Kind**: class

A specialized regular expression object that matches natural language text for predefined data patterns.

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
class NSDataDetector
```

#### Overview

Find dates, addresses, links, phone numbers, and transit information in natural language text with `NSDataDetector`.

`NSDataDetector` returns the results of matching content in [`NSTextCheckingResult`](nstextcheckingresult.md) objects. The [`NSTextCheckingResult`](nstextcheckingresult.md) objects that `NSDataDetector` returns are different from those that [`NSRegularExpression`](nsregularexpression.md) returns. The results are one of the data detector’s types and contain the corresponding properties. For example, results of type [`date`](nstextcheckingresult/checkingtype/date.md) have a [`date`](nstextcheckingresult/date.md), [`timeZone`](nstextcheckingresult/timezone.md), and [`duration`](nstextcheckingresult/duration.md); and results of type [`link`](nstextcheckingresult/checkingtype/link.md) have a [`url`](nstextcheckingresult/url.md).

> ❗ **Important**:  Don’t use `NSDataDetector` to validate data. `NSDataDetector` discards potential matches in case of uncertainty. Use a class specific to the type of data for validation instead. For example, attempt to instantiate a [`URL`](url.md) object using [`init(string:)`](url/init(string:).md) to validate a URL string. A valid URL string returns an instance of [`URL`](url.md), while an invalid URL string returns [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0).

##### Examples

The following shows several graduated examples of using the `NSDataDetector` class.

This code fragment creates a data detector that finds URL links and phone numbers. If an error occurs, it returns in `error`.

```objc
   NSError *error = nil;
   NSDataDetector *detector = [NSDataDetector dataDetectorWithTypes:NSTextCheckingTypeLink|NSTextCheckingTypePhoneNumber
                                                              error:&error];
```

After creating the data detector instance, you can determine the number of matches within a range of a string using the `NSRegularExpression` method [`numberOfMatches(in:options:range:)`](nsregularexpression/numberofmatches(in:options:range:).md).

```objc
   NSUInteger numberOfMatches = [detector numberOfMatchesInString:string
                                                          options:0
                                                            range:NSMakeRange(0, [string length])];
```

If you’re interested only in the overall range of the first match, the [`numberOfMatches(in:options:range:)`](nsregularexpression/numberofmatches(in:options:range:).md) method provides it.  However, with data detectors, this is less likely than with regular expressions because clients are usually interested in additional information as well.

The additional information available depends on the type of the result.  For results of type [`link`](nstextcheckingresult/checkingtype/link.md), it’s the `URL` property that’s significant.  For results of type `NSTextCheckingTypePhoneNumber` , it’s the `phoneNumber` property instead.

The [`matches(in:options:range:)`](nsregularexpression/matches(in:options:range:).md) method is similar to [`firstMatch(in:options:range:)`](nsregularexpression/firstmatch(in:options:range:).md), except that it returns all matches rather than only the first. The following code fragment finds all the matches for links and phone numbers in a string:

```objc
   NSArray *matches = [detector matchesInString:string
                                        options:0
                                          range:NSMakeRange(0, [string length])];
   for (NSTextCheckingResult *match in matches) {
        NSRange matchRange = [match range];
        if ([match resultType] == NSTextCheckingTypeLink) {
            NSURL *url = [match URL];
        } else if ([match resultType] == NSTextCheckingTypePhoneNumber) {
            NSString *phoneNumber = [match phoneNumber];
        }
   }
```

The `NSRegularExpression` block object enumerator is the most general and flexible of the matching methods.  It allows you to iterate through matches in a string, performing arbitrary actions on each as specified by the code in the block, and to stop partway through if desired. In the following code fragment, the iteration stops after finding a certain number of matches:

```objc
   __block NSUInteger count = 0;
   [detector enumerateMatchesInString:string
                              options:0
                                range:NSMakeRange(0, [string length])
                           usingBlock:^(NSTextCheckingResult *match, NSMatchingFlags flags, BOOL *stop){
        NSRange matchRange = [match range];
        if ([match resultType] == NSTextCheckingTypeLink) {
            NSURL *url = [match URL];
        } else if ([match resultType] == NSTextCheckingTypePhoneNumber) {
            NSString *phoneNumber = [match phoneNumber];
        }
        if (++count >= 100) *stop = YES;
   }];
```

> **Note**:  Only use `NSDataDetector` on natural language text. If you expect text to be in a particular format, use an [`Formatter`](formatter.md) or [`ValueTransformer`](valuetransformer.md) subclass instead. For instance, if you’re expecting a date field to be an ISO 8601 timestamp, use [`DateFormatter`](dateformatter.md) to parse that into an [`NSDate`](nsdate.md) object. If the text is in a machine-readable format, such as XML or JSON, extract the natural language text, such as by using [`XMLParser`](xmlparser.md) or [`JSONSerialization`](jsonserialization.md), and match on that rather than attempt to match on the entire document.

## Topics

### Creating data detector instances
- [init(types: NSTextCheckingTypes) throws](nsdatadetector/init(types:).md)
  Initializes and returns a data detector instance.
### Getting the checking types
- [var checkingTypes: NSTextCheckingTypes](nsdatadetector/checkingtypes.md)
  Returns the checking types for the data detector.

## Relationships

### Inherits From
- [NSRegularExpression](nsregularexpression.md)
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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class Scanner](scanner.md)
  A string parser that scans for substrings or characters in a character set, and for numeric values from decimal, hexadecimal, and floating-point representations.
- [class NSRegularExpression](nsregularexpression.md)
  An immutable representation of a compiled regular expression that you apply to Unicode strings.
- [class NSTextCheckingResult](nstextcheckingresult.md)
  An occurrence of textual content found during the analysis of a block of text, such as when matching a regular expression.
- [let NSNotFound: Int](nsnotfound-4qp9h.md)
  A value indicating that a requested item couldn’t be found or doesn’t exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatadetector)*