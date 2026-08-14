# AUGenericViewInternal

**Framework**: CoreAudioKit  
**Kind**: class

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
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
- [NSView](../appkit/nsview.md)
- [UIView](../uikit/uiview.md)
### Conforms To
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCollectionViewDelegate](../appkit/nscollectionviewdelegate.md)
- [NSDraggingDestination](../appkit/nsdraggingdestination.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UICollectionViewDelegate](../uikit/uicollectionviewdelegate.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIDynamicItem](../uikit/uidynamicitem.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIScrollViewDelegate](../uikit/uiscrollviewdelegate.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [typealias AUGenericViewInternalBase](augenericviewinternalbase.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/augenericviewinternal)*