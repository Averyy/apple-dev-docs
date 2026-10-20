# verticalBarCompressionBehavior

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

When the tab bar and navigation/toolbar items are both rendered together in the vertical bar, this property controls which items compress first.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
var verticalBarCompressionBehavior: UIVerticalBarCompressionBehavior { get set }
```

```objc
@property (nonatomic, assign, readwrite) UIVerticalBarCompressionBehavior verticalBarCompressionBehavior;
```

#### Discussion

The default value is `UIVerticalBarCompressionBehaviorAutomatic`.

## See Also

### Configuring bars on the vertical axis
- [enum UIVerticalBarCompressionBehavior](../uiverticalbarcompressionbehavior.md)
  How bars compress when different types of bars are hosted together and space is constrained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/verticalbarcompressionbehavior)*