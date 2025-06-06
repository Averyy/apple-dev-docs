# MarkDimensions

**Framework**: Swift Charts  
**Kind**: struct

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct MarkDimensions<DataElement>
```

## Topics

### Initializers
- [init(floatLiteral: Double)](markdimensions/init(floatliteral:).md)
  Creates a constant width or height from a floating point value.
- [init(integerLiteral: Int)](markdimensions/init(integerliteral:).md)
  Creates a constant width or height from an integer.
### Type Properties
- [static var automatic: MarkDimensions<DataElement>](markdimensions/automatic.md)
  A dimension that determines its value automatically.
### Type Methods
- [static func fixed(CGFloat) -> MarkDimensions<DataElement>](markdimensions/fixed(_:)-14cur.md)
  A constant dimension.
- [static func fixed(KeyPath<DataElement, CGFloat>) -> MarkDimensions<DataElement>](markdimensions/fixed(_:)-7k7pv.md)
  A constant dimension.
- [static func inset(KeyPath<DataElement, CGFloat>) -> MarkDimensions<DataElement>](markdimensions/inset(_:)-309e3.md)
  A dimension that’s the step size minus the specified inset value on each side.
- [static func inset(CGFloat) -> MarkDimensions<DataElement>](markdimensions/inset(_:)-5nddx.md)
  A dimension that’s the step size minus the specified inset value on each side.
- [static func ratio(CGFloat) -> MarkDimensions<DataElement>](markdimensions/ratio(_:)-8ufgm.md)
  A dimension that’s proportional to the scale step size, using the specified ratio.
- [static func ratio(KeyPath<DataElement, CGFloat>) -> MarkDimensions<DataElement>](markdimensions/ratio(_:)-r23h.md)
  A dimension that’s proportional to the scale step size, using the specified ratio.

## Relationships

### Conforms To
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/markdimensions)*