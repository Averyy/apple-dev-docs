# defaultFormatterBehavior

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class) NSDateFormatterBehavior defaultFormatterBehavior;
```

## Return Value

The default formatting behavior for instances of the class. For possible values, see [`DateFormatter.Behavior`](./behavior.md).

## Discussion

For iOS and for macOS applications linked against macOS 10.5 and later, the default is `NSDateFormatterBehavior10_4`.

## See Also

### Managing Behavior Version
- [var formatterBehavior: DateFormatter.Behavior](./formatterbehavior.md)
  The formatter behavior for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/defaultformatterbehavior)*