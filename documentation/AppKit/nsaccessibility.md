# NSAccessibility

**Framework**: AppKit

A legacy, informal protocol that Apple doesn’t recommend for active use.

#### Overview

The `NSAccessibility` informal protocol defines an old, key-based API. For the most part, Apple doesn’t recommend using this API. Use the method-based API in [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) instead. However, there are a few methods and properties that are still relevant. You can combine the [`accessibilityHitTest(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/accessibilityHitTest(_:)) method, and the [`accessibilityFocusedUIElement`](nsaccessibilitylayoutarea/accessibilityfocuseduielement.md) and [`accessibilityNotifiesWhenDestroyed`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/accessibilityNotifiesWhenDestroyed) properties with the new [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol.

## Topics

### Available Methods and Properties
- [var accessibilityFocusedUIElement: Any?](../ObjectiveC/NSObject-swift.class/accessibilityFocusedUIElement.md)
- [func accessibilityHitTest(NSPoint) -> Any?](../ObjectiveC/NSObject-swift.class/accessibilityHitTest(_:).md)
- [var accessibilityNotifiesWhenDestroyed: Bool](../ObjectiveC/NSObject-swift.class/accessibilityNotifiesWhenDestroyed.md)
  A Boolean value that indicates whether a custom accessibility object sends a notification when its corresponding UI element is destroyed.
### Constants
- [Standard Attributes](standard-attributes.md)
  Standard attributes that can be adopted by any accessibility object.
- [Text-Specific Attributes](text-specific-attributes.md)
  Attributes that are specific to text.
- [Text-Specific Parameterized Attributes](text-specific-parameterized-attributes.md)
  Parameterized attributes specific to text.
- [Text Attributed-String Attributes and Constants](text-attributed-string-attributes-and-constants.md)
  Attributes and key constants used with attributed strings.
- [Window-Specific Attributes](window-specific-attributes.md)
  Attributes specific to windows.
- [App-Specific Attributes](app-specific-attributes.md)
  Attributes that are specific to the app object.
- [Grid View Attributes](grid-view-attributes.md)
  Attributes that are used with grid views, such as thumbnails and media browsers that present a grid of items. The children of a grid are ordered.
- [Table View and Outline View Attributes](table-view-and-outline-view-attributes.md)
  Attributes that are specific to tables and outlines.
- [Outline View Attributes](outline-view-attributes.md)
  Attributes that are used in outline views.
- [Cell-Based Table Attributes](cell-based-table-attributes.md)
  Attributes that are specific to cell-based tables.
- [Cell-Based Table Parameterized Attributes](cell-based-table-parameterized-attributes.md)
  Parameterized attributes specific to cell-based tables.
- [Cell Attributes](cell-attributes.md)
  Attributes that are specific to individual table cells.
- [Layout Area Attributes](layout-area-attributes.md)
  Attributes that are specific to layout areas.
- [Layout Area Parameterized Attributes](layout-area-parameterized-attributes.md)
  Parameterized attributes that are specific to layout areas.
- [Layout Item Attributes](layout-item-attributes.md)
  Attributes that are specific to the items in a layout area.
- [Slider Attributes](slider-attributes.md)
  Attributes that are specific to sliders.
- [Screen Matte Attributes](screen-matte-attributes.md)
  Attributes that are specific to screen mattes.
- [Ruler View Attributes](ruler-view-attributes.md)
  Attributes that are specific to ruler views.
- [Linkage Elements](linkage-elements.md)
  Constants that specify links between accessibility elements.
- [Miscellaneous Attributes](miscellaneous-attributes.md)
  Miscellaneous attributes that can apply to various types of elements.
- [Column Sort Direction](column-sort-direction.md)
  Values that indicate the sort direction of a column.
- [Measurement Unit Attributes](measurement-unit-attributes.md)
  Values that indicate the unit values of a ruler or layout area.
- [Orientations](orientations.md)
  Values that indicate the orientation of elements, such as scroll bars and split views.
- [Ruler Marker Type Values](ruler-marker-type-values.md)
  Values that indicate the marker type of an element.
- [Actions](actions.md)
  Standard actions that accessibility objects can perform.
### Deprecated
- [func accessibilityActionDescription(NSAccessibility.Action) -> String?](../ObjectiveC/NSObject-swift.class/accessibilityActionDescription(_:).md)
  Returns a localized description of the specified action.
- [func accessibilityActionNames() -> [NSAccessibility.Action]](../ObjectiveC/NSObject-swift.class/accessibilityActionNames.md)
  Returns an array of action names supported by the accessibility element.
- [func accessibilityArrayAttributeCount(NSAccessibility.Attribute) -> Int](../ObjectiveC/NSObject-swift.class/accessibilityArrayAttributeCount(_:).md)
  Returns the count of the specified accessibility array attribute.
- [func accessibilityArrayAttributeValues(NSAccessibility.Attribute, index: Int, maxCount: Int) -> [Any]](../ObjectiveC/NSObject-swift.class/accessibilityArrayAttributeValues(_:index:maxCount:).md)
  Returns a subarray of values of an accessibility array attribute.
- [func accessibilityAttributeNames() -> [NSAccessibility.Attribute]](../ObjectiveC/NSObject-swift.class/accessibilityAttributeNames.md)
  Returns an array of attribute names supported by the receiver.
- [func accessibilityAttributeValue(NSAccessibility.Attribute) -> Any?](../ObjectiveC/NSObject-swift.class/accessibilityAttributeValue(_:).md)
  Returns the value of the specified attribute in the receiver.
- [func accessibilityAttributeValue(NSAccessibility.ParameterizedAttribute, forParameter: Any?) -> Any?](../ObjectiveC/NSObject-swift.class/accessibilityAttributeValue(_:forParameter:).md)
  Returns the value of the receiver’s parameterized attribute corresponding to the specified attribute name and parameter.
- [func accessibilityIndex(ofChild: Any) -> Int](../ObjectiveC/NSObject-swift.class/accessibilityIndex(ofChild:).md)
  Returns the index of the specified accessibility child in the parent.
- [func accessibilityIsAttributeSettable(NSAccessibility.Attribute) -> Bool](../ObjectiveC/NSObject-swift.class/accessibilityIsAttributeSettable(_:).md)
  Returns a Boolean value that indicates whether the value for the specified attribute in the receiver can be set.
- [func accessibilityIsIgnored() -> Bool](../ObjectiveC/NSObject-swift.class/accessibilityIsIgnored.md)
  Returns a Boolean value indicating whether the receiver should be ignored in the parent-child accessibility hierarchy.
- [func accessibilityParameterizedAttributeNames() -> [NSAccessibility.ParameterizedAttribute]](../ObjectiveC/NSObject-swift.class/accessibilityParameterizedAttributeNames.md)
  Returns a list of parameterized attribute names supported by the receiver.
- [func accessibilityPerformAction(NSAccessibility.Action)](../ObjectiveC/NSObject-swift.class/accessibilityPerformAction(_:).md)
  Performs the action associated with the specified action.
- [func accessibilitySetOverrideValue(Any?, forAttribute: NSAccessibility.Attribute) -> Bool](../ObjectiveC/NSObject-swift.class/accessibilitySetOverrideValue(_:forAttribute:).md)
  Overrides the specified attribute in the receiver or adds it if it does not exist, and sets its value to the specified value.
- [func accessibilitySetValue(Any?, forAttribute: NSAccessibility.Attribute)](../ObjectiveC/NSObject-swift.class/accessibilitySetValue(_:forAttribute:).md)
  Sets the value of the specified attribute in the receiver to the specified value.

## See Also

- [protocol NSEditorRegistration](nseditorregistration.md)
  A set of methods that controllers can implement to enable an editor view to inform the controller when it has uncommitted changes.
- [protocol NSInputServiceProvider](nsinputserviceprovider.md)
- [protocol NSInputServerMouseTracker](nsinputservermousetracker.md)
- [protocol NSDrawerDelegate](nsdrawerdelegate.md)
  A set of methods that drawer delegates implement to open, close, and resize the drawer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility)*