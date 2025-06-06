# indexDelegate

**Framework**: Core Spotlight  
**Kind**: property

The delegate object that can handle index-management tasks.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
weak var indexDelegate: (any CSSearchableIndexDelegate)? { get set }
```

#### Discussion

The delegate should conform to the [`CSSearchableIndexDelegate`](cssearchableindexdelegate.md) protocol. Set this property to handle communication with the index and perform index-management tasks for your app. In particular, long-running apps should set a delegate so that the index can be updated while the app is in the background. Alternatively, you can create an extension with a request handler that conforms to the [`CSSearchableIndexDelegate`](cssearchableindexdelegate.md) protocol and let the extension perform index updates when your app isn’t running.

## See Also

- [protocol CSSearchableIndexDelegate](cssearchableindexdelegate.md)
  A protocol that defines methods a delegate object or app extension uses to handle communication from the on-device index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/indexdelegate)*