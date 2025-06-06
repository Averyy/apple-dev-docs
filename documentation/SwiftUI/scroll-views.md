# Scroll views

**Framework**: SwiftUI

Enable people to scroll to content that doesn’t fit in the current display.

#### Overview

When the content of a view doesn’t fit in the display, you can wrap the view in a [`ScrollView`](scrollview.md) to enable people to scroll on one or more axes. Configure the scroll view using view modifiers. For example, you can set the visibility of the scroll indicators or the availability of scrolling in a given dimension.

![None](https://docs-assets.developer.apple.com/published/fc9311e17b13443bf22043d6155e0e7f/scroll-views-hero%402x.png)

You can put any view type in a scroll view, but you most often use a scroll view for a layout container with too many elements to fit in the display. For some container views that you put in a scroll view, like lazy stacks, the container doesn’t load views until they are visible or almost visible. For others, like regular stacks and grids, the container loads the content all at once, regardless of the state of scrolling.

[`Lists`](lists.md) and [`Tables`](tables.md) implicitly include a scroll view, so you don’t need to add scrolling to those container types. However, you can configure their implicit scroll views with the same view modifiers that apply to explicit scroll views.

For design guidance, see [`Scroll views`](https://developer.apple.com/design/Human-Interface-Guidelines/scroll-views) in the Human Interface Guidelines.

## Topics

### Creating a scroll view
- [struct ScrollView](scrollview.md)
  A scrollable view.
- [struct ScrollViewReader](scrollviewreader.md)
  A view that provides programmatic scrolling, by working with a proxy to scroll to known child views.
- [struct ScrollViewProxy](scrollviewproxy.md)
  A proxy value that supports programmatic scrolling of the scrollable views within a view hierarchy.
### Managing scroll position
- [func scrollPosition(Binding<ScrollPosition>, anchor: UnitPoint?) -> some View](view/scrollposition(_:anchor:).md)
  Associates a binding to a scroll position with a scroll view within this view.
- [func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) -> some View](view/scrollposition(id:anchor:).md)
  Associates a binding to be updated when a scroll view within this view scrolls.
- [func defaultScrollAnchor(UnitPoint?) -> some View](view/defaultscrollanchor(_:).md)
  Associates an anchor to control which part of the scroll view’s content should be rendered by default.
- [func defaultScrollAnchor(UnitPoint?, for: ScrollAnchorRole) -> some View](view/defaultscrollanchor(_:for:).md)
  Associates an anchor to control the position of a scroll view in a particular circumstance.
- [struct ScrollAnchorRole](scrollanchorrole.md)
  A type defining the role of a scroll anchor.
- [struct ScrollPosition](scrollposition.md)
  A type that defines the semantic position of where a scroll view is scrolled within its content.
### Defining scroll targets
- [func scrollTargetBehavior(some ScrollTargetBehavior) -> some View](view/scrolltargetbehavior(_:).md)
  Sets the scroll behavior of views scrollable in the provided axes.
- [func scrollTargetLayout(isEnabled: Bool) -> some View](view/scrolltargetlayout(isenabled:).md)
  Configures the outermost layout as a scroll target layout.
- [struct ScrollTarget](scrolltarget.md)
  A type defining the target in which a scroll view should try and scroll to.
- [protocol ScrollTargetBehavior](scrolltargetbehavior.md)
  A type that defines the scroll behavior of a scrollable view.
- [struct ScrollTargetBehaviorContext](scrolltargetbehaviorcontext.md)
  The context in which a scroll target behavior updates its scroll target.
- [struct PagingScrollTargetBehavior](pagingscrolltargetbehavior.md)
  The scroll behavior that aligns scroll targets to container-based geometry.
- [struct ViewAlignedScrollTargetBehavior](viewalignedscrolltargetbehavior.md)
  The scroll behavior that aligns scroll targets to view-based geometry.
- [struct AnyScrollTargetBehavior](anyscrolltargetbehavior.md)
  A type-erased scroll target behavior.
### Animating scroll transitions
- [func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](view/scrolltransition(_:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view, or other container specified using the `coordinateSpace` parameter.
- [func scrollTransition(topLeading: ScrollTransitionConfiguration, bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](view/scrolltransition(topleading:bottomtrailing:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view, or other container specified using the `coordinateSpace` parameter.
- [enum ScrollTransitionPhase](scrolltransitionphase.md)
  The phases that a view transitions between when it scrolls among other views.
- [struct ScrollTransitionConfiguration](scrolltransitionconfiguration.md)
  The configuration of a scroll transition that controls how a transition is applied as a view is scrolled through the visible region of a containing scroll view or other container.
### Responding to scroll view changes
- [func onScrollGeometryChange<T>(for: T.Type, of: (ScrollGeometry) -> T, action: (T, T) -> Void) -> some View](view/onscrollgeometrychange(for:of:action:).md)
  Adds an action to be performed when a value, created from a scroll geometry, changes.
- [func onScrollTargetVisibilityChange<ID>(idType: ID.Type, threshold: Double, ([ID]) -> Void) -> some View](view/onscrolltargetvisibilitychange(idtype:threshold:_:).md)
  Adds an action to be called with information about what views would be considered visible.
- [func onScrollVisibilityChange(threshold: Double, (Bool) -> Void) -> some View](view/onscrollvisibilitychange(threshold:_:).md)
  Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [func onScrollPhaseChange(_:)](view/onscrollphasechange(_:).md)
  Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [struct ScrollGeometry](scrollgeometry.md)
  A type that defines the geometry of a scroll view.
- [enum ScrollPhase](scrollphase.md)
  A type that describes the state of a scroll gesture of a scrollable view like a scroll view.
- [struct ScrollPhaseChangeContext](scrollphasechangecontext.md)
  A type that provides you with more content when the phase of a scroll view changes.
### Showing scroll indicators
- [func scrollIndicatorsFlash(onAppear: Bool) -> some View](view/scrollindicatorsflash(onappear:).md)
  Flashes the scroll indicators of a scrollable view when it appears.
- [func scrollIndicatorsFlash(trigger: some Equatable) -> some View](view/scrollindicatorsflash(trigger:).md)
  Flashes the scroll indicators of scrollable views when a value changes.
- [func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some View](view/scrollindicators(_:axes:).md)
  Sets the visibility of scroll indicators within this view.
- [var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility](environmentvalues/horizontalscrollindicatorvisibility.md)
  The visibility to apply to scroll indicators of any horizontally scrollable content.
- [var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility](environmentvalues/verticalscrollindicatorvisibility.md)
  The visiblity to apply to scroll indicators of any vertically scrollable content.
- [struct ScrollIndicatorVisibility](scrollindicatorvisibility.md)
  The visibility of scroll indicators of a UI element.
### Managing content visibility
- [func scrollContentBackground(Visibility) -> some View](view/scrollcontentbackground(_:).md)
  Specifies the visibility of the background for scrollable views within this view.
- [func scrollClipDisabled(Bool) -> some View](view/scrollclipdisabled(_:).md)
  Sets whether a scroll view clips its content to its bounds.
- [struct ScrollContentOffsetAdjustmentBehavior](scrollcontentoffsetadjustmentbehavior.md)
  A type that defines the different kinds of content offset adjusting behaviors a scroll view can have.
### Disabling scrolling
- [func scrollDisabled(Bool) -> some View](view/scrolldisabled(_:).md)
  Disables or enables scrolling in scrollable views.
- [var isScrollEnabled: Bool](environmentvalues/isscrollenabled.md)
  A Boolean value that indicates whether any scroll views associated with this environment allow scrolling to occur.
### Configuring scroll bounce behavior
- [func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View](view/scrollbouncebehavior(_:axes:).md)
  Configures the bounce behavior of scrollable views along the specified axis.
- [var horizontalScrollBounceBehavior: ScrollBounceBehavior](environmentvalues/horizontalscrollbouncebehavior.md)
  The scroll bounce mode for the horizontal axis of scrollable views.
- [var verticalScrollBounceBehavior: ScrollBounceBehavior](environmentvalues/verticalscrollbouncebehavior.md)
  The scroll bounce mode for the vertical axis of scrollable views.
- [struct ScrollBounceBehavior](scrollbouncebehavior.md)
  The ways that a scrollable view can bounce when it reaches the end of its content.
### Interacting with a software keyboard
- [func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View](view/scrolldismisseskeyboard(_:).md)
  Configures the behavior in which scrollable content interacts with the software keyboard.
- [var scrollDismissesKeyboardMode: ScrollDismissesKeyboardMode](environmentvalues/scrolldismisseskeyboardmode.md)
  The way that scrollable content interacts with the software keyboard.
- [struct ScrollDismissesKeyboardMode](scrolldismisseskeyboardmode.md)
  The ways that scrollable content can interact with the software keyboard.
### Managing scrolling for different inputs
- [func scrollInputBehavior(ScrollInputBehavior, for: ScrollInputKind) -> some View](view/scrollinputbehavior(_:for:).md)
  Enables or disables scrolling in scrollable views when using particular inputs.
- [struct ScrollInputKind](scrollinputkind.md)
  Inputs used to scroll views.
- [struct ScrollInputBehavior](scrollinputbehavior.md)
  A type that defines whether input should scroll a view.

## See Also

- [Layout fundamentals](layout-fundamentals.md)
  Arrange views inside built-in layout containers like stacks and grids.
- [Layout adjustments](layout-adjustments.md)
  Make fine adjustments to alignment, spacing, padding, and other layout parameters.
- [Custom layout](custom-layout.md)
  Place views in custom arrangements and create animated transitions between layout types.
- [Lists](lists.md)
  Display a structured, scrollable column of information.
- [Tables](tables.md)
  Display selectable, sortable data arranged in rows and columns.
- [View groupings](view-groupings.md)
  Present views in different kinds of purpose-driven containers, like forms or control groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scroll-views)*