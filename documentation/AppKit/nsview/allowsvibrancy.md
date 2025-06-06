# allowsVibrancy

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view ensures it is vibrant on top of other content.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var allowsVibrancy: Bool { get }
```

#### Discussion

AppKit checks this property when the view is incorporated into a view hierarchy that uses vibrancy. If the property is [`true`](https://developer.apple.com/documentation/swift/true), the view takes appropriate measures to ensure its content is vibrant on top of any underlying material. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false). However, some of AppKit’s view subclasses change the value of this property based on the artwork they draw.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/allowsvibrancy)*