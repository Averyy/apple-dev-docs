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

### Setting a delegate
- [var delegate: (any NSTextSelectionManager.Delegate)?](nstextselectionmanager/delegate-swift.property.md)
  The delegate of the text selection manager.
- [NSTextSelectionManager.Delegate](nstextselectionmanager/delegate-swift.protocol.md)
  A set of methods that manage text selection state and let you customize selection behavior.
### Configuring text selection
- [var textSelectionMode: NSTextSelectionManager.Mode](nstextselectionmanager/textselectionmode.md)
  The interaction mode for text selection.
- [NSTextSelectionManager.Mode](nstextselectionmanager/mode.md)
  Values for text selection interaction modes.
- [var textSelectionDataSource: (any NSTextSelectionDataSource)?](nstextselectionmanager/textselectiondatasource.md)
  The data source that provides text layout information to the selection manager.
### Managing gesture recognizers
- [var gesturesForFailureRequirements: [NSGestureRecognizer]](nstextselectionmanager/gesturesforfailurerequirements.md)
  The gesture recognizers managed by the selection manager.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)

## See Also

- [class NSTextRange](nstextrange.md)
  A class that represents a contiguous range between two locations inside document contents.
- [class NSTextSelection](nstextselection.md)
  A class that represents a single logical selection context that corresponds to an insertion point.
- [class NSTextSelectionNavigation](nstextselectionnavigation.md)
  An interface you use to expose methods for obtaining results from actions performed on text selections.
- [protocol NSTextLocation](nstextlocation.md)
  An interface you implement that represents an abstract location inside your document’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager)*