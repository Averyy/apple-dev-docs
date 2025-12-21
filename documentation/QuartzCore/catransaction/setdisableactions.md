# setDisableActions(_:)

**Framework**: Core Animation  
**Kind**: method

Sets whether actions triggered as a result of property changes made within this transaction group are suppressed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func setDisableActions(_ flag: Bool)
```

#### Discussion

This is a convenience method that invokes [`setValue(_:forKey:)`](catransaction/setvalue(_:forkey:).md) with an `NSNumber` containing a [`true`](https://developer.apple.com/documentation/Swift/true) for the  [`kCATransactionDisableActions`](kcatransactiondisableactions.md) key.

## Parameters

- `flag`:  , if actions should be disabled.

## See Also

- [class func disableActions() -> Bool](catransaction/disableactions.md)
  Returns whether actions triggered as a result of property changes made within this transaction group are suppressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction/setdisableactions(_:))*