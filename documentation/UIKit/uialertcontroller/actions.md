# actions

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The actions that the user can take in response to the alert or action sheet.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var actions: [UIAlertAction] { get }
```

```objc
@property (nonatomic, readonly) NSArray<UIAlertAction *> * actions;
```

## Discussion

The actions are in the order in which you added them to the alert controller. This order also corresponds to the order in which they’re displayed in the alert or action sheet. The second action in the array is displayed below the first, the third is displayed below the second, and so on.

## See Also

### Configuring the user actions
- [func addAction(UIAlertAction)](./addaction%28_%29.md)
  Attaches an action object to the alert or action sheet.
- [var preferredAction: UIAlertAction?](./preferredaction.md)
  The preferred action for the user to take from an alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertcontroller/actions)*