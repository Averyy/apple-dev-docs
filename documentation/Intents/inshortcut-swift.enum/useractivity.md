# userActivity

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user activity that defines the action to perform when invoking the shortcut.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 11.0+
- watchOS 5.0+

## Declaration

```swift
var userActivity: NSUserActivity? { get }
```

## Discussion

This property is nil when you create the shortcut with an [`INIntent`](../inintent.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inshortcut-swift.enum/useractivity)*