# defaultFormatterBehavior

**Framework**: Foundation  
**Kind**: property

Returns the default formatting behavior for instances of the class.

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
class var defaultFormatterBehavior: DateFormatter.Behavior { get set }
```

#### Return Value

The default formatting behavior for instances of the class. For possible values, see [`DateFormatter.Behavior`](dateformatter/behavior.md).

#### Discussion

For iOS and for macOS applications linked against macOS 10.5 and later, the default is `NSDateFormatterBehavior10_4`.

## See Also

- [var formatterBehavior: DateFormatter.Behavior](dateformatter/formatterbehavior.md)
  The formatter behavior for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/defaultformatterbehavior)*