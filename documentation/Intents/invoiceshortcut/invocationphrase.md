# invocationPhrase

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The phrase the user speaks to invoke the shortcut.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var invocationPhrase: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * invocationPhrase;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * invocationPhrase;
```

## Discussion

The user sets the invocation phrase when they add the shortcut to Siri.

## See Also

### Accessing Shortcut Information
- [var identifier: UUID](./identifier.md)
  The unique identifier for the shortcut.
- [var shortcut: INShortcut](./shortcut.md)
  The shortcut Siri invokes when the user speaks the invocation phrase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invoiceshortcut/invocationphrase)*