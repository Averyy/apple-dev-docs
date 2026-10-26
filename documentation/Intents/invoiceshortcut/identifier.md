# identifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The unique identifier for the shortcut.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var identifier: UUID { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly) NSUUID * identifier;
```

*macOS*

```objc
@property (atomic, strong, readonly) NSUUID * identifier;
```

## See Also

### Accessing Shortcut Information
- [var invocationPhrase: String](./invocationphrase.md)
  The phrase the user speaks to invoke the shortcut.
- [var shortcut: INShortcut](./shortcut.md)
  The shortcut Siri invokes when the user speaks the invocation phrase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invoiceshortcut/identifier)*