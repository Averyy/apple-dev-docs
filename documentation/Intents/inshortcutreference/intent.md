# intent

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The intent that performs the action when invoking the shortcut.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@NSCopying
var intent: INIntent? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INIntent * intent;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INIntent * intent;
```

## Discussion

This property is `nil` when you create the shortcut with an [`NSUserActivity`](../../Foundation/nsuseractivity.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inshortcutreference/intent)*