# secondaryAction

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An optional secondary action, and button, for the navigation alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var secondaryAction: CPAlertAction? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) CPAlertAction * secondaryAction;
```

## Discussion

The alert displays the button for a secondary action on the trailing edge of the alert.

## See Also

### Getting the actions
- [var actions: [CPAlertAction]](./actions.md)
  The array of actions associated with this navigation alert.
- [var primaryAction: CPAlertAction](./primaryaction.md)
  The primary action, and button, for the navigation alert.
- [class var maximumActionsCount: Int](./maximumactionscount.md)
  The maximum number of actions that a @c CPNavigationAlert can display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/secondaryaction)*