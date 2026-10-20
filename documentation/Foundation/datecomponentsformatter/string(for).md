# string(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a formatted string based on the date information in the specified object.

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
func string(for obj: Any?) -> String?
```

```objc
- (NSString *) stringForObjectValue:(id) obj;
```

#### Return Value

A formatted string representing the specified date information.

#### Discussion

This method has the same behavior as the [`string(from:)`](./string%28from%29-9exxn.md) method.

## Parameters

- `obj`: An object containing the date and time information to format. The object in this parameter must be a [`NSDateComponents`](../nsdatecomponents.md) object; if it is not, the method raises an exception. This parameter must not be `nil`.

## See Also

### Formatting Values
- [func string(from: DateComponents) -> String?](./string%28from%29-9exxn.md)
  Returns a formatted string based on the specified date component information.
- [func string(from: Date, to: Date) -> String?](./string%28from,to%29.md)
  Returns a formatted string based on the time difference between two dates.
- [func string(from: TimeInterval) -> String?](./string%28from%29-7sj4j.md)
  Returns a formatted string based on the specified number of seconds.
- [class func localizedString(from: DateComponents, unitsStyle: DateComponentsFormatter.UnitsStyle) -> String?](./localizedstring%28from,unitsstyle%29.md)
  Returns a localized string based on the specified date components and style option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/string(for:))*