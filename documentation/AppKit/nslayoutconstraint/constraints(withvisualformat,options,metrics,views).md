# constraints(withVisualFormat:options:metrics:views:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates constraints described by an ASCII art-like visual format string.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class func constraints(withVisualFormat format: String, options opts: NSLayoutConstraint.FormatOptions = [], metrics: [String : Any]?, views: [String : Any]) -> [NSLayoutConstraint]
```

```objc
+ (NSArray<NSLayoutConstraint *> *) constraintsWithVisualFormat:(NSString *) format options:(NSLayoutFormatOptions) opts metrics:(NSDictionary<NSString *,id> *) metrics views:(NSDictionary<NSString *,id> *) views;
```

#### Return Value

An array of constraints that, combined, express the constraints between the provided views and their parent view as described by the visual format string. The constraints are returned in the same order they were specified in the visual format string.

#### Discussion

For more information, see [`NSLayoutConstraint`](../nslayoutconstraint.md).

## Parameters

- `format`: The format specification for the constraints.
- `opts`: Options describing the attribute and the direction of layout for all objects in the visual format string.
- `metrics`: A dictionary of constants that appear in the visual format string. The dictionary’s keys must be the string values used in the visual format string. Their values must be [`NSNumber`](../../Foundation/nsnumber.md) objects.
- `views`: A dictionary of views that appear in the visual format string. The keys must be the string values used in the visual format string, and the values must be the view objects.

## See Also

### Related Documentation
- [class NSLayoutConstraint](../nslayoutconstraint.md)
  The relationship between two user interface objects that must be satisfied by the constraint-based layout system.
### Creating constraints
- [convenience init(item: Any, attribute: NSLayoutConstraint.Attribute, relatedBy: NSLayoutConstraint.Relation, toItem: Any?, attribute: NSLayoutConstraint.Attribute, multiplier: CGFloat, constant: CGFloat)](./init%28item,attribute,relatedby,toitem,attribute,multiplier,constant%29.md)
  Creates a constraint that defines the relationship between the specified attributes of the given views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/constraints(withvisualformat:options:metrics:views:))*