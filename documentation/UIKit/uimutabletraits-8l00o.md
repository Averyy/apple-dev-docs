# UIMutableTraits

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

A mutable container of traits.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
@protocol UIMutableTraits <NSObject>
```

## Mentions

- [Providing data to the view hierarchy with custom traits](./providing-data-to-the-view-hierarchy-with-custom-traits.md)

#### Overview

The [`UIMutableTraits`](./uimutabletraits-8l00o.md) protocol provides read-write access to get and set trait values on an underlying container. UIKit uses this protocol to facilitate working with instances of [`UITraitCollection`](./uitraitcollection.md), which are immutable and read-only. The [`UITraitCollection`](./uitraitcollection.md) initializer [`traitCollectionWithTraits:`](./uitraitcollection/traitcollectionwithtraits_.md) uses an instance of [`UIMutableTraits`](./uimutabletraits-8l00o.md), which enables you to set a batch of trait values in one method call. [`UITraitOverrides`](./uitraitoverrides-c.protocol.md) conforms to [`UIMutableTraits`](./uimutabletraits-8l00o.md), making it easy to set trait overrides on trait environments such as views and view controllers.

## Topics

### Getting and setting trait values
- [accessibilityContrast](./uimutabletraits-8l00o/accessibilitycontrast.md)
  The accessibility contrast associated with the current environment.
- [activeAppearance](./uimutabletraits-8l00o/activeappearance.md)
  A property that indicates whether a scene has an active appearance.
- [displayGamut](./uimutabletraits-8l00o/displaygamut.md)
  The gamut of the current display.
- [displayScale](./uimutabletraits-8l00o/displayscale.md)
  The display scale of the trait collection.
- [forceTouchCapability](./uimutabletraits-8l00o/forcetouchcapability.md)
  The Force Touch capability value of the trait collection.
- [horizontalSizeClass](./uimutabletraits-8l00o/horizontalsizeclass.md)
  The horizontal size class of the trait collection.
- [imageDynamicRange](./uimutabletraits-8l00o/imagedynamicrange.md)
  The image dynamic range associated with the current environment.
- [layoutDirection](./uimutabletraits-8l00o/layoutdirection.md)
  The layout direction associated with the current environment.
- [legibilityWeight](./uimutabletraits-8l00o/legibilityweight.md)
  The font weight to apply to text.
- [listEnvironment](./uimutabletraits-8l00o/listenvironment.md)
  The style of the containing list in a collection view or table view.
- [preferredContentSizeCategory](./uimutabletraits-8l00o/preferredcontentsizecategory.md)
  The font sizing option preferred by the user.
- [resolvesNaturalAlignmentWithBaseWritingDirection](./uimutabletraits-8l00o/resolvesnaturalalignmentwithbasewritingdirection.md)
  The setting for whether the system resolves natural alignment with base writing direction for the current environment.
- [sceneCaptureState](./uimutabletraits-8l00o/scenecapturestate.md)
  The scene capture state for the current environment.
- [splitViewControllerLayoutEnvironment](./uimutabletraits-8l00o/splitviewcontrollerlayoutenvironment.md)
  The split view controller layout for the current environment.
- [tabAccessoryEnvironment](./uimutabletraits-8l00o/tabaccessoryenvironment.md)
  The tab accessory environment for the current trait collection.
- [toolbarItemPresentationSize](./uimutabletraits-8l00o/toolbaritempresentationsize.md)
  The presentation size of a toolbar item in an AppKit toolbar.
- [typesettingLanguage](./uimutabletraits-8l00o/typesettinglanguage.md)
  The typesetting language associated with the current environment.
- [userInterfaceIdiom](./uimutabletraits-8l00o/userinterfaceidiom.md)
  The user interface idiom of the trait collection.
- [userInterfaceLevel](./uimutabletraits-8l00o/userinterfacelevel.md)
  The elevation level of the interface.
- [userInterfaceStyle](./uimutabletraits-8l00o/userinterfacestyle.md)
  The style associated with the user interface.
- [verticalSizeClass](./uimutabletraits-8l00o/verticalsizeclass.md)
  The vertical size class of the trait collection.
### Getting and setting trait data
- [- objectForTrait:](./uimutabletraits-8l00o/objectfortrait_.md)
- [- setObject:forTrait:](./uimutabletraits-8l00o/setobject_fortrait_.md)
- [UIObjectTrait](./uiobjecttrait.md)
- [- valueForCGFloatTrait:](./uimutabletraits-8l00o/valueforcgfloattrait_.md)
- [- setCGFloatValue:forTrait:](./uimutabletraits-8l00o/setcgfloatvalue_fortrait_.md)
- [UICGFloatTrait](./uicgfloattrait.md)
- [- valueForNSIntegerTrait:](./uimutabletraits-8l00o/valuefornsintegertrait_.md)
- [- setNSIntegerValue:forTrait:](./uimutabletraits-8l00o/setnsintegervalue_fortrait_.md)
- [UINSIntegerTrait](./uinsintegertrait.md)
### Instance Properties
- [systemPrefersReducedResourceUsage](./uimutabletraits-8l00o/systemprefersreducedresourceusage.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [UITraitOverrides](./uitraitoverrides-c.protocol.md)

## See Also

### Observing and managing traits
- [Automatic trait tracking](./automatic-trait-tracking.md)
  Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.
- [class UITraitCollection](./uitraitcollection.md)
  A collection of data that represents the environment for an individual element in your app’s user interface.
- [protocol UITraitEnvironment](./uitraitenvironment.md)
  A set of methods that makes the iOS interface environment available to your app.
- [UITraitChangeObservable](./uitraitchangeobservable-7qoet.md)
  A type that calls your code in reaction to changes in the trait environment.
- [protocol UIAdaptivePresentationControllerDelegate](./uiadaptivepresentationcontrollerdelegate.md)
  A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.
- [protocol UIContentContainer](./uicontentcontainer.md)
  A set of methods for adapting the contents of your view controllers to size and trait changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutabletraits-8l00o)*