# value(forAnimatedKey:)

**Framework**: UIKit  
**Kind**: method

Returns the most recently set value for the specified key.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func value(forAnimatedKey key: String) -> CGFloat
```

#### Return Value

The last value set for the key.

#### Discussion

Use this method to retrieve floating-point values that are useful when laying out the contents of your collection view. The key you specify is a string that you define and that has some meaning to your implementation. At points during an interactive transition, you can assign new values to that key using the [`updateValue(_:forAnimatedKey:)`](uicollectionviewtransitionlayout/updatevalue(_:foranimatedkey:).md) method.

## Parameters

- `key`: A key whose value you set using the   method.

## See Also

- [var transitionProgress: CGFloat](uicollectionviewtransitionlayout/transitionprogress.md)
  The completion percentage of the transition.
- [func updateValue(CGFloat, forAnimatedKey: String)](uicollectionviewtransitionlayout/updatevalue(_:foranimatedkey:).md)
  Sets the value for an animatable key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/value(foranimatedkey:))*