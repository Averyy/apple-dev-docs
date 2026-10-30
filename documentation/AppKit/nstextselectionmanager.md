# NSTextSelectionManager

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that coordinates text selection behavior for custom text views.

**Availability**:
- macOS 27.0+

## Declaration

```swift
@MainActor
class NSTextSelectionManager
```

```objc
@interface NSTextSelectionManager : NSObject
```

## Mentions

- [Adopting gesture recognizers in your app](./adopting-gesture-recognizers-in-your-app.md)

## Overview

`NSTextSelectionManager` provides a centralized way to manage text selection interactions using a set of gesture recognizers. For keyboard-based selection, integrate [`NSTextSelectionNavigation`](./nstextselectionnavigation.md) with your view. The selection manager works with a delegate to update and respond to selection changes, and with a data source to query the text layout system.

### Gesture recognizer priority

Attach an `NSTextSelectionManager` to a view that isn’t [`NSTextView`](./nstextview.md) or [`NSTextField`](./nstextfield.md) by setting the manager’s `view` property, and set its [`textSelectionDataSource`](./nstextselectionmanager/textselectiondatasource.md) property to your text layout object — typically an `NSTextLayoutManager`. Together, these give your custom view classic macOS text-selection behavior: bidirectional selection, drag-and-drop of text, and toggling.

`NSTextSelectionManager` builds on gesture recognizers. If you attach your own gesture recognizers to the same view, use [`gesturesForFailureRequirements`](./nstextselectionmanager/gesturesforfailurerequirements.md) to make your gesture recognizers wait for the selection manager’s gestures to fail before recognizing — so the selection manager gets first chance at the touch or click, instead of your gesture recognizers competing with it. For more information, see [Prioritize gesture recognizers](./handling-appkit-gestures.md#Prioritize-gesture-recognizers).

## Topics

### Setting a delegate
- [var delegate: (any NSTextSelectionManager.Delegate)?](./nstextselectionmanager/delegate-swift.property.md)
  The delegate of the text selection manager.
- [NSTextSelectionManager.Delegate](./nstextselectionmanager/delegate-swift.protocol.md)
  A set of methods that manage text selection state and let you customize selection behavior.
### Configuring text selection
- [var textSelectionMode: NSTextSelectionManager.Mode](./nstextselectionmanager/textselectionmode.md)
  The interaction mode for text selection.
- [NSTextSelectionManager.Mode](./nstextselectionmanager/mode.md)
  Values for text selection interaction modes.
- [var textSelectionDataSource: (any NSTextSelectionDataSource)?](./nstextselectionmanager/textselectiondatasource.md)
  The data source that provides text layout information to the selection manager.
### Managing gesture recognizers
- [var gesturesForFailureRequirements: [NSGestureRecognizer]](./nstextselectionmanager/gesturesforfailurerequirements.md)
  The gesture recognizers managed by the selection manager.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Location and selection
- [class NSTextRange](./nstextrange.md)
  A class that represents a contiguous range between two locations inside document contents.
- [class NSTextSelection](./nstextselection.md)
  A class that represents a single logical selection context that corresponds to an insertion point.
- [class NSTextSelectionNavigation](./nstextselectionnavigation.md)
  An interface you use to expose methods for obtaining results from actions performed on text selections.
- [protocol NSTextLocation](./nstextlocation.md)
  An interface you implement that represents an abstract location inside your document’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager)*