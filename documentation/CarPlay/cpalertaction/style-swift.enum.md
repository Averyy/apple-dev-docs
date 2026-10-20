# CPAlertAction.Style

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

Display styles for an alert’s action button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum Style
```

```c
enum CPAlertActionStyle : NSUInteger;
```

## Topics

### Styles
- [CPAlertAction.Style.default](./style-swift.enum/default.md)
  The default display style for an action button.
- [CPAlertAction.Style.cancel](./style-swift.enum/cancel.md)
  The display style indicating that the action leaves data unchanged.
- [CPAlertAction.Style.destructive](./style-swift.enum/destructive.md)
  The style indicating that the action changes or deletes data.
### Initializers
- [init?(rawValue: UInt)](./style-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the Action Style
- [var style: CPAlertAction.Style](./style-swift.property.md)
  The display style for the action button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpalertaction/style-swift.enum)*