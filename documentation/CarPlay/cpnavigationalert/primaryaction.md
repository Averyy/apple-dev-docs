# primaryAction

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The primary action, and button, for the navigation alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var primaryAction: CPAlertAction { get }
```

```objc
@property (nonatomic, strong, readonly) CPAlertAction * primaryAction;
```

## Discussion

Each navigation alert must have a primary action.

## See Also

### Getting the Actions
- [var secondaryAction: CPAlertAction?](./secondaryaction.md)
  An optional secondary action, and button, for the navigation alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/primaryaction)*