# isValidDate

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the current combination of properties represents a date which exists in the current calendar.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isValidDate: Bool { get }
```

```objc
@property (readonly, getter=isValidDate) BOOL validDate;
```

## Discussion

If the [`timeZone`](./timezone.md) property is set on the receiver, the time zone property value is used. If the [`calendar`](./calendar.md) property is not set on the receiver, `nil` is returned.

## See Also

### Validating a Date
- [func isValidDate(in: Calendar) -> Bool](./isvaliddate%28in%29.md)
  Returns a Boolean value that indicates whether the current combination of properties represents a date which exists in the specified calendar.
- [var date: Date?](./date.md)
  The date calculated from the current components using the stored calendar.
- [Undefined Components](../api-1430344-undefined-components.md)
  Constants that denote that the value of a date component is undefined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/isvaliddate)*