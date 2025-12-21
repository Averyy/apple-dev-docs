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
@MainActor
optional var enableInputClicksWhenVisible: Bool { get }
```

#### Discussion

In your custom subclass of [`UIView`](uiview.md), implement this property as a getter method. Return [`true`](https://developer.apple.com/documentation/Swift/true) to enable input clicks in your custom input or keyboard accessory view, as follows:

Input clicks will be produced only if the user has also enabled keyboard clicks in Settings > Sounds.

## Parameters

- `enableInputClicksWhenVisible`: Return   to enable input clicks by way of the   method, or   to disable input clicks. The value is   by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputviewaudiofeedback/enableinputclickswhenvisible)*