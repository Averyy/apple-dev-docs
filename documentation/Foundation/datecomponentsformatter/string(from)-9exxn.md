# string(from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a formatted string based on the specified date component information.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func string(from components: DateComponents) -> String?
```

```objc
- (NSString *) stringFromDateComponents:(NSDateComponents *) components;
```

## Return Value

A formatted string representing the specified date information.

## Discussion

Use this method to format date information that is already broken down into the component day and time values.

## Parameters

- `components`: A date components object containing the date and time information to format. The [`allowedUnits`](./allowedunits.md) property determines which date components are actually used to generate the string. All other date components are ignored. This parameter must not be `nil`.

## See Also

### Formatting Values
- [func string(for: Any?) -> String?](./string%28for%29.md)
  Returns a formatted string based on the date information in the specified object.
- [func string(from: Date, to: Date) -> String?](./string%28from,to%29.md)
  Returns a formatted string based on the time difference between two dates.
- [func string(from: TimeInterval) -> String?](./string%28from%29-7sj4j.md)
  Returns a formatted string based on the specified number of seconds.
- [class func localizedString(from: DateComponents, unitsStyle: DateComponentsFormatter.UnitsStyle) -> String?](./localizedstring%28from,unitsstyle%29.md)
  Returns a localized string based on the specified date components and style option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/string(from:)-9exxn)*