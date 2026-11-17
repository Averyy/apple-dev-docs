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

### Getting the actions
- [var actions: [CPAlertAction]](./actions.md)
  The array of actions associated with this navigation alert.
- [var secondaryAction: CPAlertAction?](./secondaryaction.md)
  An optional secondary action, and button, for the navigation alert.
- [class var maximumActionsCount: Int](./maximumactionscount.md)
  The maximum number of actions that a @c CPNavigationAlert can display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/primaryaction)*