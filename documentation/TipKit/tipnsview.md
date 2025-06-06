# TipNSView

**Framework**: TipKit  
**Kind**: class

A user interface element that represents a tip in AppKit applications.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@objc @preconcurrency final class TipNSView
```

#### Overview

You create a tip view by providing a tip and an optional arrow edge. The tip is a type that conforms to the [`Tip`](tip.md) protocol. The arrow edge is a directional arrow pointing away from the tip.

Use this view to create a tip you want to display and lay out as a [`NSView`](https://developer.apple.com/documentation/AppKit/NSView).

Adding and removing TipNSView from your app is done by listening to a tip’s [`shouldDisplayUpdates`](tip/shoulddisplayupdates.md) or [`statusUpdates`](tip/statusupdates.md).

```swift
import Cocoa
import TipKit

struct CatTracksFeatureTip: Tip {
    var title: Text {
        Text("Sample tip title")
    }

    var message: Text? {
        Text("Sample tip message")
    }

    var image: Image? {
        Image(systemName: "globe")
    }
}

class CatTracksViewController: NSViewController {
    private var catTracksFeatureTip = CatTracksFeatureTip()
    private var tipObservationTask: Task<Void, Never>?
    private weak var tipView: TipNSView?

    override func viewDidAppear() {
        super.viewDidAppear()

        tipObservationTask = tipObservationTask ?? Task { @MainActor in
            for await shouldDisplay in catTracksFeatureTip.shouldDisplayUpdates {
                if shouldDisplay {
                    let tipHostingView = TipNSView(catTracksFeatureTip)
                    view.addSubview(tipHostingView)

                    view.addConstraints([
                        tipHostingView.centerYAnchor.constraint(equalTo: view.centerYAnchor),
                        tipHostingView.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20.0),
                        tipHostingView.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20.0)
                    ])

                    tipView = tipHostingView
                }
                else {
                    tipView?.removeFromSuperview()
                    tipView = nil
                }
            }
        }
    }

    override func viewDidDisappear() {
        super.viewDidDisappear()

        tipObservationTask?.cancel()
        tipObservationTask = nil
    }
}
```

## Topics

### Initializers
- [convenience init(any Tip, arrowEdge: Edge?, actionHandler: (Tips.Action) -> Void)](tipnsview/init(_:arrowedge:actionhandler:).md)
  Creates a tip view with an optional arrow.
### Instance Properties
- [var backgroundColor: NSColor?](tipnsview/backgroundcolor.md)
  The background color to use for the tip view.
- [var cornerRadius: CGFloat](tipnsview/cornerradius.md)
  Corner radius for the tip view.
- [var imageSize: CGSize](tipnsview/imagesize.md)
  Size of the image displayed in the tip view.
- [var imageStyle: (any ShapeStyle)?](tipnsview/imagestyle.md)
  Foreground style for the tip’s image.
- [var viewStyle: any TipViewStyle](tipnsview/viewstyle.md)
  The given style for TipView within the view hierarchy

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)

## See Also

- [class TipNSPopover](tipnspopover.md)
  A subclass of NSPopover that displays a popover tip in AppKit applications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipnsview)*