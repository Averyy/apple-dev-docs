# style

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The display style for the action button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var style: CPAlertAction.Style { get }
```

```objc
@property (nonatomic, assign, readonly) CPAlertActionStyle style;
```

#### Discussion

The combination of [`style`](./style-swift.property.md) and the template type, [`CPActionSheetTemplate`](../cpactionsheettemplate.md) or [`CPAlertTemplate`](../cpalerttemplate.md), determines the appearance of the action button.

## See Also

### Getting the Action Style
- [CPAlertAction.Style](./style-swift.enum.md)
  Display styles for an alert’s action button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpalertaction/style-swift.property)*