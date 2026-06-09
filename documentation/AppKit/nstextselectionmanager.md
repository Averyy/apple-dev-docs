# NSTextSelectionManager

**Framework**: AppKit  
**Kind**: class

An object that coordinates text selection behavior for custom text views.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
class NSTextSelectionManager
```

#### Overview

[`NSTextSelectionManager`](nstextselectionmanager.md) provides a centralized way to manage text selection interactions using a set of gesture recognizers. For keyboard-based selection, integrate [`NSTextSelectionNavigation`](nstextselectionnavigation.md) with your view. The selection manager works with a delegate to update and respond to selection changes, and with a data source to query the text layout system.

## Topics

### Protocols
- [NSTextSelectionManager.Delegate](nstextselectionmanager/delegate-swift.protocol.md)
  A set of methods that manage text selection state and let you customize selection behavior.
### Instance Properties
- [var delegate: (any NSTextSelectionManager.Delegate)?](nstextselectionmanager/delegate-swift.property.md)
  The delegate of the text selection manager.
- [var gesturesForFailureRequirements: [NSGestureRecognizer]](nstextselectionmanager/gesturesforfailurerequirements.md)
  The gesture recognizers managed by the selection manager.
- [var textSelectionDataSource: (any NSTextSelectionDataSource)?](nstextselectionmanager/textselectiondatasource.md)
  The data source that provides text layout information to the selection manager.
- [var textSelectionMode: NSTextSelectionManager.Mode](nstextselectionmanager/textselectionmode.md)
  The interaction mode for text selection.
### Enumerations
- [NSTextSelectionManager.Mode](nstextselectionmanager/mode.md)
  Values for text selection interaction modes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager)*