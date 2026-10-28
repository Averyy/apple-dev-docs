# delegate

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property

A delegate for a drag interaction.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
weak var delegate: (any BEDragInteractionDelegate)? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) id<BEDragInteractionDelegate> delegate;
```

## Discussion

The delegate conforms to [`BEDragInteractionDelegate`](../bedraginteractiondelegate.md).

## See Also

### Handling drag gestures
- [protocol BEDragInteractionDelegate](../bedraginteractiondelegate.md)
  A protocol for a drag interaction delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedraginteraction/delegate)*