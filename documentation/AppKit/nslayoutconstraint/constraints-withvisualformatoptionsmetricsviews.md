# constraints(withVisualFormat:options:metrics:views:)

**Framework**: AppKit  
**Kind**: method

Creates constraints described by an ASCII art-like visual format string.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class func constraints(withVisualFormat format: String, options opts: NSLayoutConstraint.FormatOptions = [], metrics: [String : Any]?, views: [String : Any]) -> [NSLayoutConstraint]
```

#### Return Value

An array of constraints that, combined, express the constraints between the provided views and their parent view as described by the visual format string. The constraints are returned in the same order they were specified in the visual format string.

#### Discussion

The language used for the visual format string is described in [`Auto Layout Cookbook`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/LayoutUsingStackViews.html#//apple_ref/doc/uid/TP40010853-CH3) in [`Auto Layout Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html#//apple_ref/doc/uid/TP40010853).

## Parameters

- `format`: The format specification for the constraints. For more information, see   in  .
- `opts`: Options describing the attribute and the direction of layout for all objects in the visual format string.
- `metrics`: A dictionary of constants that appear in the visual format string. The dictionary’s keys must be the string values used in the visual format string. Their values must be   objects.
- `views`: A dictionary of views that appear in the visual format string. The keys must be the string values used in the visual format string, and the values must be the view objects.

## See Also

- [Auto Layout Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html#//apple_ref/doc/uid/TP40010853)
- [convenience init(item: Any, attribute: NSLayoutConstraint.Attribute, relatedBy: NSLayoutConstraint.Relation, toItem: Any?, attribute: NSLayoutConstraint.Attribute, multiplier: CGFloat, constant: CGFloat)](nslayoutconstraint/init(item:attribute:relatedby:toitem:attribute:multiplier:constant:).md)
  Creates a constraint that defines the relationship between the specified attributes of the given views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/constraints(withvisualformat:options:metrics:views:))*