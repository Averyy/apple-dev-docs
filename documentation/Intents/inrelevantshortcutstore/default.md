# default

**Framework**: Intents  
**Kind**: property  
**Role**: Type Property

The default relevant shortcut store.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class var `default`: INRelevantShortcutStore { get }
```

```objc
@property (class, strong, readonly) INRelevantShortcutStore * defaultStore;
```

## Mentions

- [Defining Relevant Shortcuts for the Siri Watch Face](../../SiriKit/defining-relevant-shortcuts-for-the-siri-watch-face.md)

#### Discussion

Always use [`default`](./default.md) to get a reference to the Relevant Shortcut Store instead of creating an instance of [`INRelevantShortcutStore`](../inrelevantshortcutstore.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrelevantshortcutstore/default)*