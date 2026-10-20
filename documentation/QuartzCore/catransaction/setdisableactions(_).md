# setDisableActions(_:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (void) setDisableActions:(BOOL) flag;
```

#### Discussion

This is a convenience method that invokes [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md) with an `NSNumber` containing a [`true`](../../Swift/true.md) for the  [`kCATransactionDisableActions`](../kcatransactiondisableactions.md) key.

## Parameters

- `flag`: [`true`](../../Swift/true.md), if actions should be disabled.

## See Also

### Temporarily Disabling Property Animations
- [class func disableActions() -> Bool](./disableactions%28%29.md)
  Returns whether actions triggered as a result of property changes made within this transaction group are suppressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction/setdisableactions(_:))*