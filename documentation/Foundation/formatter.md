# Formatter

**Framework**: Foundation  
**Kind**: class

An abstract class that declares an interface for objects that create, interpret, and validate the textual representation of values.

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
class Formatter
```

#### Overview

The Foundation framework provides several concrete subclasses of [`Formatter`](formatter.md), including [`ByteCountFormatter`](bytecountformatter.md), [`DateFormatter`](dateformatter.md), [`DateComponentsFormatter`](datecomponentsformatter.md), [`DateIntervalFormatter`](dateintervalformatter.md), [`MeasurementFormatter`](measurementformatter.md), [`NumberFormatter`](numberformatter.md), and [`PersonNameComponentsFormatter`](personnamecomponentsformatter.md).

> 💡 **Tip**:  In Swift, you can use implementations of [`FormatStyle`](formatstyle.md) rather than [`Formatter`](formatter.md). The [`FormatStyle`](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [`FormatStyle`](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

 In Swift, you can use implementations of [`FormatStyle`](formatstyle.md) rather than [`Formatter`](formatter.md). The [`FormatStyle`](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [`FormatStyle`](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

##### Subclassing Notes

[`Formatter`](formatter.md) is intended for subclassing. A custom formatter can restrict the input and enhance the display of data in novel ways. For example, you could have a custom formatter that ensures that serial numbers entered by a user conform to predefined formats. Before you decide to create a custom formatter, make sure that you cannot configure the public subclasses to satisfy your requirements.

For instructions on how to create your own custom formatter, see [`Creating a Custom Formatter`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/Articles/CreatingACustomFormatter.html#//apple_ref/doc/uid/20000196).

## Topics

### Getting Textual Representations of Object Values
- [func string(for: Any?) -> String?](formatter/string(for:).md)
  The default implementation of this method raises an exception.
- [func attributedString(for: Any, withDefaultAttributes: [NSAttributedString.Key : Any]?) -> NSAttributedString?](formatter/attributedstring(for:withdefaultattributes:).md)
  The default implementation returns `nil` to indicate that the formatter object does not provide an attributed string.
- [func editingString(for: Any) -> String?](formatter/editingstring(for:).md)
  The default implementation of this method invokes [`string(for:)`](formatter/string(for:).md).
### Getting Object Values for Textual Representations
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](formatter/getobjectvalue(_:for:errordescription:).md)
  The default implementation of this method raises an exception.
### Validating Partial Strings
- [func isPartialStringValid(String, newEditingString: AutoreleasingUnsafeMutablePointer<NSString?>?, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](formatter/ispartialstringvalid(_:neweditingstring:errordescription:).md)
  Returns a Boolean value that indicates whether a partial string is valid.
- [func isPartialStringValid(AutoreleasingUnsafeMutablePointer<NSString>, proposedSelectedRange: NSRangePointer?, originalString: String, originalSelectedRange: NSRange, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](formatter/ispartialstringvalid(_:proposedselectedrange:originalstring:originalselectedrange:errordescription:).md)
  This method should be implemented in subclasses that want to validate user changes to a string in a field, where the user changes are not necessarily at the end of the string, and preserve the selection (or set a different one, such as selecting the erroneous part of the string the user has typed).
### Constants
- [Formatter.Context](formatter/context.md)
  The formatting context for a formatter.
- [Formatter.UnitStyle](formatter/unitstyle.md)
  Specifies the width of the unit, determining the textual representation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [ByteCountFormatter](bytecountformatter.md)
- [DateComponentsFormatter](datecomponentsformatter.md)
- [DateFormatter](dateformatter.md)
- [DateIntervalFormatter](dateintervalformatter.md)
- [EnergyFormatter](energyformatter.md)
- [ISO8601DateFormatter](iso8601dateformatter.md)
- [LengthFormatter](lengthformatter.md)
- [ListFormatter](listformatter.md)
- [MassFormatter](massformatter.md)
- [MeasurementFormatter](measurementformatter.md)
- [NumberFormatter](numberformatter.md)
- [PersonNameComponentsFormatter](personnamecomponentsformatter.md)
- [RelativeDateTimeFormatter](relativedatetimeformatter.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatter)*