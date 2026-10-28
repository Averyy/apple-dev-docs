# shared

**Framework**: Intents  
**Kind**: property  
**Role**: Type Property

The shared shortcut center.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class var shared: INVoiceShortcutCenter { get }
```

```objc
@property (class, strong, readonly) INVoiceShortcutCenter * sharedCenter;
```

## Discussion

To get an instance of [`INVoiceShortcutCenter`](../invoiceshortcutcenter.md), always use the [`shared`](./shared.md) class property. Creating an instance of the shortcut center isn’t allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invoiceshortcutcenter/shared)*