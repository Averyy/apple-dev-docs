# needsInputModeSwitchKey

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the keyboard must display an input switcher key.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var needsInputModeSwitchKey: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL needsInputModeSwitchKey;
```

## Discussion

The input switcher key allows the user to switch between different keyboards. When this property is true, your custom keyboard should provide such a key.

## See Also

### Configuring the keyboard behaviors
- [var hasFullAccess: Bool](./hasfullaccess.md)
  A Boolean value that indicates whether the keyboard has full access.
- [var hasDictationKey: Bool](./hasdictationkey.md)
  A Boolean value that indicates whether the keyboard has a dictation key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/needsinputmodeswitchkey)*