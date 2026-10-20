# NSRefreshController

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A controller that provides pull-to-refresh functionality for scroll views.

**Availability**:
- macOS 27.0+

## Declaration

```swift
@MainActor
class NSRefreshController
```

```objc
@interface NSRefreshController : NSObject
```

#### Overview

`NSRefreshController` enables users to trigger refresh operations by pulling down on scrollable content. Add a refresh controller to an `NSScrollView` to provide this functionality. Configure the target and action to handle refresh events.

## Topics

### Instance Properties
- [var action: Selector?](./nsrefreshcontroller/action.md)
  The action method to call when refresh is triggered.
- [var attributedTitle: NSAttributedString?](./nsrefreshcontroller/attributedtitle.md)
  The styled text to display in the refresh controller.
- [var isRefreshing: Bool](./nsrefreshcontroller/isrefreshing.md)
  A Boolean value indicating whether a refresh operation is in progress.
- [var target: AnyObject?](./nsrefreshcontroller/target.md)
  The target object that receives action messages.
- [var tintColor: NSColor?](./nsrefreshcontroller/tintcolor.md)
  The tint color for the refresh controller.
### Instance Methods
- [func beginRefreshing()](./nsrefreshcontroller/beginrefreshing%28%29.md)
  Tells the refresh controller that a refresh operation has begun.
- [func endRefreshing()](./nsrefreshcontroller/endrefreshing%28%29.md)
  Tells the refresh controller that a refresh operation has ended.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrefreshcontroller)*