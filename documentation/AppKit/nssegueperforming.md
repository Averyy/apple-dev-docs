# NSSeguePerforming

**Framework**: AppKit  
**Kind**: protocol

A set of methods that support the mediation of a custom segue.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSSeguePerforming : NSObjectProtocol
```

#### Overview

When you subclass [`NSStoryboardSegue`](nsstoryboardsegue.md) to express a custom transition or containment relationship between storyboard scenes, you might also want to provide code that prepares the destination/contained view or window controller object. Put this code in an override of the [`prepare(for:sender:)`](nssegueperforming/prepare(for:sender:).md) method.

To conditionally disallow the performance of a segue, override the [`shouldPerformSegue(withIdentifier:sender:)`](nssegueperforming/shouldperformsegue(withidentifier:sender:).md) method, returning [`false`](https://developer.apple.com/documentation/swift/false).If you need to programmatically trigger a segue that cannot be expressed in a storyboard file, such as a transition between scenes in different storyboards, use the [`performSegue(withIdentifier:sender:)`](nssegueperforming/performsegue(withidentifier:sender:).md) method in this protocol.

## Topics

### Working with Storyboard Segues
- [func performSegue(withIdentifier: NSStoryboardSegue.Identifier, sender: Any?)](nssegueperforming/performsegue(withidentifier:sender:).md)
  Performs the specified segue.
- [func prepare(for: NSStoryboardSegue, sender: Any?)](nssegueperforming/prepare(for:sender:).md)
  Called when a segue is about to be performed.
- [func shouldPerformSegue(withIdentifier: NSStoryboardSegue.Identifier, sender: Any?) -> Bool](nssegueperforming/shouldperformsegue(withidentifier:sender:).md)
  Called immediately prior to the performance of a storyboard segue.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSCollectionViewItem](nscollectionviewitem.md)
- [NSPageController](nspagecontroller.md)
- [NSSplitViewController](nssplitviewcontroller.md)
- [NSTabViewController](nstabviewcontroller.md)
- [NSTitlebarAccessoryViewController](nstitlebaraccessoryviewcontroller.md)
- [NSViewController](nsviewcontroller.md)
- [NSWindowController](nswindowcontroller.md)

## See Also

- [class NSStoryboard](nsstoryboard.md)
  An encapsulation of the design-time view controller and window controller graph represented in an Interface Builder storyboard resource file.
- [class NSStoryboardSegue](nsstoryboardsegue.md)
  A transition or containment relationship between two scenes in a storyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegueperforming)*