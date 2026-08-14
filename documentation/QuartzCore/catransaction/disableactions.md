# disableActions()

**Framework**: Core Animation  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if actions are disabled.

#### Discussion

This is a convenience method that returns the `boolValue` for the [`value(forKey:)`](catransaction/value(forkey:).md) value returned by the  [`kCATransactionDisableActions`](kcatransactiondisableactions.md) key.

## See Also

- [class func setDisableActions(Bool)](catransaction/setdisableactions(_:).md)
  Sets whether actions triggered as a result of property changes made within this transaction group are suppressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction/disableactions())*