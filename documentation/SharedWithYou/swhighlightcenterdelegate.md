# SWHighlightCenterDelegate

**Framework**: Shared with You  
**Kind**: protocol  
**Role**: Protocol

The protocol you use to notify the delegate when the list or rank order of surfaced highlights changes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
protocol SWHighlightCenterDelegate : NSObjectProtocol
```

```objc
@protocol SWHighlightCenterDelegate <NSObject>
```

## Topics

### Protocol Attributes
- [func highlightCenterHighlightsDidChange(SWHighlightCenter)](./swhighlightcenterdelegate/highlightcenterhighlightsdidchange%28_%29.md)
  Notifies the delegate that the list or rank order of surfaced highlights has changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Setting the delegate
- [var delegate: (any SWHighlightCenterDelegate)?](./swhighlightcenter/delegate.md)
  The delegate object for the highlight center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightcenterdelegate)*