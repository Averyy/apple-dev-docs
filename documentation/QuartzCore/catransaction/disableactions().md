# disableActions()

**Framework**: Core Animation  
**Kind**: method  
**Role**: Type Method

Returns whether actions triggered as a result of property changes made within this transaction group are suppressed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func disableActions() -> Bool
```

```objc
+ (BOOL) disableActions;
```

#### Return Value

[`true`](../../Swift/true.md) if actions are disabled.

#### Discussion

This is a convenience method that returns the `boolValue` for the [`value(forKey:)`](./value%28forkey%29.md) value returned by the  [`kCATransactionDisableActions`](../kcatransactiondisableactions.md) key.

## See Also

### Temporarily Disabling Property Animations
- [class func setDisableActions(Bool)](./setdisableactions%28_%29.md)
  Sets whether actions triggered as a result of property changes made within this transaction group are suppressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction/disableactions())*