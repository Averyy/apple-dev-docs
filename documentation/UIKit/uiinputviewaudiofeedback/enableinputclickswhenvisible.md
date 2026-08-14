# enableInputClicksWhenVisible

**Framework**: UIKit  
**Kind**: property

Specifies whether or not an input view enables input clicks.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+

## Declaration

```swift
optional var enableInputClicksWhenVisible: Bool { get }
```

#### Discussion

In your custom subclass of [`UIView`](uiview.md), implement this property as a getter method. Return [`true`](https://developer.apple.com/documentation/swift/true) to enable input clicks in your custom input or keyboard accessory view, as follows:

**Swift**:

```swift
var enableInputClicksWhenVisible: Bool {
    return true
}
```

**Objective-C**:

```objc
- (BOOL) enableInputClicksWhenVisible {
    return YES;
}
```

Input clicks will be produced only if the user has also enabled keyboard clicks in Settings > Sounds.

## Parameters

- `enableInputClicksWhenVisible`: Return [`true`](https://developer.apple.com/documentation/swift/true) to enable input clicks by way of the [`playInputClick()`](uidevice/playinputclick().md) method, or [`false`](https://developer.apple.com/documentation/swift/false) to disable input clicks. The value is [`false`](https://developer.apple.com/documentation/swift/false) by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputviewaudiofeedback/enableinputclickswhenvisible)*