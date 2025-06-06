# Lists

**Framework**: SwiftUI

Display a structured, scrollable column of information.

#### Overview

Use a list to display a one-dimensional vertical collection of views.

![None](https://docs-assets.developer.apple.com/published/15c88d97bce9de9704854a5490b6aee5/lists-hero%402x.png)

The list is a complex container type that automatically provides scrolling when it grows too large for the current display. You build a list by providing it with individual views for the rows in the list, or by using a [`ForEach`](foreach.md) to enumerate a group of rows. You can also mix these strategies, blending any number of individual views and `ForEach` constructs.

Use view modifiers to configure the appearance and behavior of a list and its rows, headers, sections, and separators. For example, you can apply a style to the list, add swipe gestures to individual rows, or make the list refreshable with a pull-down gesture. You can also use the configuration associated with [`Scroll views`](scroll-views.md) to control the list’s implicit scrolling behavior.

For design guidance, see [`Lists and tables`](https://developer.apple.com/design/Human-Interface-Guidelines/lists-and-tables) in the Human Interface Guidelines.

## Topics

### Creating a list
- [Displaying data in lists](displaying-data-in-lists.md)
  Visualize collections of data with platform-appropriate appearance.
- [struct List](list.md)
  A container that presents rows of data arranged in a single column, optionally providing the ability to select one or more members.
- [func listStyle<S>(S) -> some View](view/liststyle(_:).md)
  Sets the style for lists within this view.
### Disclosing information progressively
- [struct OutlineGroup](outlinegroup.md)
  A structure that computes views and disclosure groups on demand from an underlying collection of tree-structured, identified data.
- [struct DisclosureGroup](disclosuregroup.md)
  A view that shows or hides another content view, based on the state of a disclosure control.
- [func disclosureGroupStyle<S>(S) -> some View](view/disclosuregroupstyle(_:).md)
  Sets the style for disclosure groups within this view.
### Configuring rows
- [func listRowInsets(EdgeInsets?) -> some View](view/listrowinsets(_:).md)
  Applies an inset to the rows in a list.
- [func listRowHoverEffect(HoverEffect?) -> some View](view/listrowhovereffect(_:).md)
  Requests that the containing list row use the provided hover effect.
- [func listRowHoverEffectDisabled(Bool) -> some View](view/listrowhovereffectdisabled(_:).md)
  Requests that the containing list row have its hover effect disabled.
- [func listItemTint(_:)](view/listitemtint(_:).md)
  Sets a fixed tint color for content in a list.
- [struct ListItemTint](listitemtint.md)
  A tint effect configuration that you can apply to content in a list.
- [var defaultMinListRowHeight: CGFloat](environmentvalues/defaultminlistrowheight.md)
  The default minimum height of a row in a `List`. The default minimum height of a row in a list.
### Configuring separators
- [func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](view/listrowseparatortint(_:edges:).md)
  Sets the tint color associated with a row.
- [func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](view/listsectionseparatortint(_:edges:).md)
  Sets the tint color associated with a section.
- [func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View](view/listrowseparator(_:edges:).md)
  Sets the display mode for the separator associated with this specific row.
- [func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View](view/listsectionseparator(_:edges:).md)
  Sets whether to hide the separator associated with a list section.
### Configuring headers
- [func headerProminence(Prominence) -> some View](view/headerprominence(_:).md)
  Sets the header prominence for this view.
- [var headerProminence: Prominence](environmentvalues/headerprominence.md)
  The prominence to apply to section headers within a view.
- [enum Prominence](prominence.md)
  A type indicating the prominence of a view hierarchy.
- [var defaultMinListHeaderHeight: CGFloat?](environmentvalues/defaultminlistheaderheight.md)
  The default minimum height of a header in a list.
### Configuring spacing
- [func listRowSpacing(CGFloat?) -> some View](view/listrowspacing(_:).md)
  Sets the vertical spacing between two adjacent rows in a List.
- [func listSectionSpacing(_:)](view/listsectionspacing(_:).md)
  Sets the spacing between adjacent sections in a [`List`](list.md) to a custom value.
- [struct ListSectionSpacing](listsectionspacing.md)
  The spacing options between two adjacent sections in a list.
### Configuring backgrounds
- [func listRowBackground<V>(V?) -> some View](view/listrowbackground(_:).md)
  Places a custom background view behind a list row item.
- [func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some View](view/alternatingrowbackgrounds(_:).md)
  Overrides whether lists and tables in this view have alternating row backgrounds.
- [struct AlternatingRowBackgroundBehavior](alternatingrowbackgroundbehavior.md)
  The styling of views with respect to alternating row backgrounds.
- [var backgroundProminence: BackgroundProminence](environmentvalues/backgroundprominence.md)
  The prominence of the background underneath views associated with this environment.
- [struct BackgroundProminence](backgroundprominence.md)
  The prominence of backgrounds underneath other views.
### Displaying a badge on a list item
- [func badge(_:)](view/badge(_:).md)
  Generates a badge for the view from an integer value.
- [func badgeProminence(BadgeProminence) -> some View](view/badgeprominence(_:).md)
  Specifies the prominence of badges created by this view.
- [var badgeProminence: BadgeProminence](environmentvalues/badgeprominence.md)
  The prominence to apply to badges associated with this environment.
- [struct BadgeProminence](badgeprominence.md)
  The visual prominence of a badge.
### Configuring interaction
- [func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: () -> T) -> some View](view/swipeactions(edge:allowsfullswipe:content:).md)
  Adds custom swipe actions to a row in a list.
- [func selectionDisabled(Bool) -> some View](view/selectiondisabled(_:).md)
  Adds a condition that controls whether users can select this view.
### Refreshing a list’s content
- [func refreshable(action: () async -> Void) -> some View](view/refreshable(action:).md)
  Marks this view as refreshable.
- [var refresh: RefreshAction?](environmentvalues/refresh.md)
  A refresh action stored in a view’s environment.
- [struct RefreshAction](refreshaction.md)
  An action that initiates a refresh operation.
### Editing a list
- [func moveDisabled(Bool) -> some View](view/movedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is movable.
- [func deleteDisabled(Bool) -> some View](view/deletedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is deletable.
- [var editMode: Binding<EditMode>?](environmentvalues/editmode.md)
  An indication of whether the user can edit the contents of a view associated with this environment.
- [enum EditMode](editmode.md)
  A mode that indicates whether the user can edit a view’s content.
- [struct EditActions](editactions.md)
  A set of edit actions on a collection of data that a view can offer to a user.
- [struct EditableCollectionContent](editablecollectioncontent.md)
  An opaque wrapper view that adds editing capabilities to a row in a list.
- [struct IndexedIdentifierCollection](indexedidentifiercollection.md)
  A collection wrapper that iterates over the indices and identifiers of a collection together.

## See Also

- [Layout fundamentals](layout-fundamentals.md)
  Arrange views inside built-in layout containers like stacks and grids.
- [Layout adjustments](layout-adjustments.md)
  Make fine adjustments to alignment, spacing, padding, and other layout parameters.
- [Custom layout](custom-layout.md)
  Place views in custom arrangements and create animated transitions between layout types.
- [Tables](tables.md)
  Display selectable, sortable data arranged in rows and columns.
- [View groupings](view-groupings.md)
  Present views in different kinds of purpose-driven containers, like forms or control groups.
- [Scroll views](scroll-views.md)
  Enable people to scroll to content that doesn’t fit in the current display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/lists)*