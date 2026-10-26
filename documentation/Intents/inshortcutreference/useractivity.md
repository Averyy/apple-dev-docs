# userActivity

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user activity that defines the action to perform when invoking the shortcut.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var userActivity: NSUserActivity? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nullable) NSUserActivity * userActivity;
```

*macOS*

```objc
@property (atomic, strong, readonly, nullable) NSUserActivity * userActivity;
```

#### Discussion

This property is `nil` when you create the shortcut with an [`INIntent`](../inintent.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inshortcutreference/useractivity)*