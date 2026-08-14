# TipNSPopover

**Framework**: TipKit  
**Kind**: class

A subclass of NSPopover that displays a popover tip in AppKit applications.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@objc @preconcurrency final class TipNSPopover
```

#### Overview

Use this to create a tip you want to display and lay out as a [`NSPopover`](https://developer.apple.com/documentation/appkit/nspopover).

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
    @IBOutlet weak var catTracksFeatureButton: NSButton!

    private var catTracksFeatureTip = CatTracksFeatureTip()
    private var tipObservationTask: Task<Void, Never>?
    private var tipPopover: TipNSPopover?

    override func viewDidAppear() {
        super.viewDidAppear()

        tipObservationTask = tipObservationTask ?? Task { @MainActor in
            for await shouldDisplay in catTracksFeatureTip.shouldDisplayUpdates {
                if shouldDisplay {
                    tipPopover = TipNSPopover(catTracksFeatureTip)
                    tipPopover?.show(relativeTo: catTracksFeatureButton.bounds, of: catTracksFeatureButton, preferredEdge: .minY)
                }
                else {
                    tipPopover?.close()
                    tipPopover = nil
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
- [init(any Tip, delegate: (any NSPopoverDelegate)?, actionHandler: (Tips.Action) -> Void)](tipnspopover/init(_:delegate:actionhandler:).md)
  Initializes a popover with the specified tip.
### Instance Properties
- [var backgroundColor: NSColor?](tipnspopover/backgroundcolor.md)
  The background color to use for the tip view.
- [var backgroundStyle: any ShapeStyle](tipnspopover/backgroundstyle.md)
  The background style to use for the tip view.
- [var cornerRadius: CGFloat](tipnspopover/cornerradius.md)
  Corner radius for the tip view.
- [var imageSize: CGSize](tipnspopover/imagesize.md)
  Size of the image displayed in the tip view.
- [var imageStyle: (any ShapeStyle)?](tipnspopover/imagestyle.md)
  Foreground style for the tip’s image.
- [var viewStyle: any TipViewStyle](tipnspopover/viewstyle.md)
  The given style for TipView within the view hierarchy

## Relationships

### Inherits From
- [NSPopover](../appkit/nspopover.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)

## See Also

- [class TipNSView](tipnsview.md)
  A user interface element that represents a tip in AppKit applications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipnspopover)*