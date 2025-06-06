# NSPlaceholders

**Framework**: AppKit

A set of methods that an object can implement to register default placeholders to be displayed for a binding, when no other placeholder is specified.

#### Overview

Individual placeholder values can be specified for each of the marker objects (described in [`Selection Markers`](selection-markers.md)), as well as when the property is `nil`.

Placeholders are used when a property of an instance of the receiving class is accessed through a key value coding compliant method, and returns `nil` or a specialized marker.

## Topics

### Managing default placeholders
- [class func setDefaultPlaceholder(_ placeholder: Any?, for marker: Any?, with binding: NSBindingName)](../ObjectiveC/NSObject-swift.class/setDefaultPlaceholder(_:for:with:).md)
  Sets `placeholder` as the default placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.
- [class func defaultPlaceholder(for marker: Any?, with binding: NSBindingName) -> Any?](../ObjectiveC/NSObject-swift.class/defaultPlaceholder(for:with:).md)
  Returns an object that will be used as the placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.
### Constants
- [Selection Markers](selection-markers.md)
  The following constants are used to describe special cases for a controller’s selection.

## See Also

- [class NSBindingSelectionMarker](nsbindingselectionmarker.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsplaceholders)*