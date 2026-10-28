# timeZone

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The time zone used to create and parse date representations. When unspecified, GMT is used.

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
var timeZone: TimeZone! { get set }
```

```objc
@property (copy, null_resettable) NSTimeZone * timeZone;
```

## Discussion

Resetting this property can incur a significant performance cost, as it may cause internal state to be regenerated.

## See Also

### Configuring the Formatter
- [var formatOptions: ISO8601DateFormatter.Options](./formatoptions.md)
  Options for generating and parsing ISO 8601 date representations. See [`ISO8601DateFormatter.Options`](./options.md) for possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/iso8601dateformatter/timezone)*