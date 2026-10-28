# NSSeguePerforming

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that support the mediation of a custom segue.

**Availability**:
- macOS

## Declaration

```swift
protocol NSSeguePerforming : NSObjectProtocol
```

```objc
@protocol NSSeguePerforming <NSObject>
```

## Overview

When you subclass [`NSStoryboardSegue`](./nsstoryboardsegue.md) to express a custom transition or containment relationship between storyboard scenes, you might also want to provide code that prepares the destination/contained view or window controller object. Put this code in an override of the [`prepare(for:sender:)`](./nssegueperforming/prepare%28for,sender%29.md) method.

To conditionally disallow the performance of a segue, override the [`shouldPerformSegue(withIdentifier:sender:)`](./nssegueperforming/shouldperformsegue%28withidentifier,sender%29.md) method, returning [`false`](../Swift/false.md).If you need to programmatically trigger a segue that cannot be expressed in a storyboard file, such as a transition between scenes in different storyboards, use the [`performSegue(withIdentifier:sender:)`](./nssegueperforming/performsegue%28withidentifier,sender%29.md) method in this protocol.

## Topics

### Working with Storyboard Segues
- [func performSegue(withIdentifier: NSStoryboardSegue.Identifier, sender: Any?)](./nssegueperforming/performsegue%28withidentifier,sender%29.md)
  Performs the specified segue.
- [func prepare(for: NSStoryboardSegue, sender: Any?)](./nssegueperforming/prepare%28for,sender%29.md)
  Called when a segue is about to be performed.
- [func shouldPerformSegue(withIdentifier: NSStoryboardSegue.Identifier, sender: Any?) -> Bool](./nssegueperforming/shouldperformsegue%28withidentifier,sender%29.md)
  Called immediately prior to the performance of a storyboard segue.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [NSCollectionViewItem](./nscollectionviewitem.md)
- [NSPageController](./nspagecontroller.md)
- [NSSplitViewController](./nssplitviewcontroller.md)
- [NSSplitViewItemAccessoryViewController](./nssplitviewitemaccessoryviewcontroller.md)
- [NSTabViewController](./nstabviewcontroller.md)
- [NSTitlebarAccessoryViewController](./nstitlebaraccessoryviewcontroller.md)
- [NSViewController](./nsviewcontroller.md)
- [NSWindowController](./nswindowcontroller.md)

## See Also

### Storyboard
- [class NSStoryboard](./nsstoryboard.md)
  An encapsulation of the design-time view controller and window controller graph represented in an Interface Builder storyboard resource file.
- [class NSStoryboardSegue](./nsstoryboardsegue.md)
  A transition or containment relationship between two scenes in a storyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegueperforming)*