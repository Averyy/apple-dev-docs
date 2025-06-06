# AUGenericViewInternal

**Framework**: CoreAudioKit  
**Kind**: class

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@objc @preconcurrency class AUGenericViewInternal
```

#### Overview

Apple discourages the use of this symbol.

## Topics

### Initializers
- [init?(coder: NSCoder)](augenericviewinternal/init(coder:).md)
- [init(frame: CGRect)](augenericviewinternal/init(frame:).md)
### Instance Properties
- [var auAudioUnit: AUAudioUnit?](augenericviewinternal/auaudiounit.md)
- [var owningController: UIViewController?](augenericviewinternal/owningcontroller.md)
- [var paramObserverToken: AUParameterObserverToken?](augenericviewinternal/paramobservertoken.md)
- [var showSingleClumpIndex: Int?](augenericviewinternal/showsingleclumpindex.md)
### Instance Methods
- [func removeFromSuperview()](augenericviewinternal/removefromsuperview.md)
- [func removeScheduledUpdatesTimer()](augenericviewinternal/removescheduledupdatestimer.md)
- [func traitCollectionDidChange(UITraitCollection?)](augenericviewinternal/traitcollectiondidchange(_:).md)

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
- [UIView](../UIKit/UIView.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCollectionViewDelegate](../AppKit/NSCollectionViewDelegate.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICollectionViewDelegate](../UIKit/UICollectionViewDelegate.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIScrollViewDelegate](../UIKit/UIScrollViewDelegate.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [typealias AUGenericViewInternalBase](augenericviewinternalbase.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/augenericviewinternal)*