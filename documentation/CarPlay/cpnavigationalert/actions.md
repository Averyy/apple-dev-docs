# actions

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The array of actions associated with this navigation alert.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var actions: [CPAlertAction] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<CPAlertAction *> * actions;
```

## Discussion

If the alert was created with the older @c primaryAction / @c secondaryAction initializer, this property returns those actions as an array for backward compatibility.

> **Note**: CPAlertActionStyleCancel actions are rendered as standard labeled buttons in the primary action row.

## See Also

### Getting the actions
- [var primaryAction: CPAlertAction](./primaryaction.md)
  The primary action, and button, for the navigation alert.
- [var secondaryAction: CPAlertAction?](./secondaryaction.md)
  An optional secondary action, and button, for the navigation alert.
- [class var maximumActionsCount: Int](./maximumactionscount.md)
  The maximum number of actions that a @c CPNavigationAlert can display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/actions)*