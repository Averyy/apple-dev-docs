# isLenient

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver uses heuristics when parsing a string.

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
var isLenient: Bool { get set }
```

```objc
@property (getter=isLenient) BOOL lenient;
```

#### Discussion

[`true`](../../Swift/true.md) if the receiver has been set to use heuristics when parsing a string to guess at the date which is intended, otherwise [`false`](../../Swift/false.md).

If a formatter is set to be lenient, when parsing a string it uses heuristics to guess at the date which is intended. As with any guessing, it may get the result date wrong (that is, a date other than that which was intended).

## See Also

### Managing Natural Language Support
- [var doesRelativeDateFormatting: Bool](./doesrelativedateformatting.md)
  A Boolean value that indicates whether the receiver uses phrases such as “today” and “tomorrow” for the date component.
- [- allowsNaturalLanguage](../nsdateformatter/allowsnaturallanguage.md)
  Returns a Boolean value that indicates whether the receiver attempts to process dates entered as a vernacular string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/islenient)*