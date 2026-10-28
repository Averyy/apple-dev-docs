# AUGenericViewInternal

**Framework**: CoreAudioKit  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS

## Declaration

```swift
@MainActor
@objc @preconcurrency class AUGenericViewInternal
```

## Overview

Apple discourages the use of this symbol.

## Topics

### Initializers
- [init?(coder: NSCoder)](./augenericviewinternal/init%28coder%29.md)
- [init(frame: CGRect)](./augenericviewinternal/init%28frame%29.md)
### Instance Properties
- [var auAudioUnit: AUAudioUnit?](./augenericviewinternal/auaudiounit.md)
- [var owningController: UIViewController?](./augenericviewinternal/owningcontroller.md)
- [var paramObserverToken: AUParameterObserverToken?](./augenericviewinternal/paramobservertoken.md)
- [var showSingleClumpIndex: Int?](./augenericviewinternal/showsingleclumpindex.md)
### Instance Methods
- [func removeFromSuperview()](./augenericviewinternal/removefromsuperview%28%29.md)
- [func removeScheduledUpdatesTimer()](./augenericviewinternal/removescheduledupdatestimer%28%29.md)
- [func traitCollectionDidChange(UITraitCollection?)](./augenericviewinternal/traitcollectiondidchange%28_%29.md)

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
- [UIView](../UIKit/uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCollectionViewDelegate](../AppKit/nscollectionviewdelegate.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UICollectionViewDelegate](../UIKit/uicollectionviewdelegate.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIScrollViewDelegate](../UIKit/uiscrollviewdelegate.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Deprecations
- [typealias AUGenericViewInternalBase](./augenericviewinternalbase.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/augenericviewinternal)*