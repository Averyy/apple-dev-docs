# isAccessibilityElement

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the item is an accessibility element an assistive application can access.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isAccessibilityElement: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL isAccessibilityElement;
```

#### Discussion

The default value for this property is [`false`](../../Swift/false.md). If the receiver is a UIKit control, the default value is [`true`](../../Swift/true.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/isaccessibilityelement)*