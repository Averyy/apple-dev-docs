# automaticallyUpdateForSelection

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the style automatically updates when the button is in a selected state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
var automaticallyUpdateForSelection: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/Swift/true) for the [`plain()`](uibutton/configuration-swift.struct/plain().md), [`gray()`](uibutton/configuration-swift.struct/gray().md), and [`tinted()`](uibutton/configuration-swift.struct/tinted().md) configurations. Set this value to [`false`](https://developer.apple.com/documentation/Swift/false) to customize the selection behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/automaticallyupdateforselection)*