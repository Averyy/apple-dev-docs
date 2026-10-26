# shortcut

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The shortcut Siri invokes when the user speaks the invocation phrase.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var shortcut: INShortcut { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) INShortcut * shortcut;
```

*macOS*

```objc
@property (atomic, copy, readonly) INShortcut * shortcut;
```

#### Discussion

Use the [`shortcut`](./shortcut.md) property to access the [`intent`](../inshortcutreference/intent.md) or [`userActivity`](../inshortcutreference/useractivity.md) used to create the [`INShortcutReference`](../inshortcutreference.md) object.

## See Also

### Accessing Shortcut Information
- [var identifier: UUID](./identifier.md)
  The unique identifier for the shortcut.
- [var invocationPhrase: String](./invocationphrase.md)
  The phrase the user speaks to invoke the shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invoiceshortcut/shortcut)*