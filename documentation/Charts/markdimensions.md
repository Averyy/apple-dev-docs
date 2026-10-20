# MarkDimensions

**Framework**: Swift Charts  
**Kind**: struct  
**Role**: Structure

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
- [init(floatLiteral: Double)](./markdimensions/init%28floatliteral%29.md)
  Creates a constant width or height from a floating point value.
- [init(integerLiteral: Int)](./markdimensions/init%28integerliteral%29.md)
  Creates a constant width or height from an integer.
### Type Properties
- [static var automatic: MarkDimensions<DataElement>](./markdimensions/automatic.md)
  A dimension that determines its value automatically.
### Type Methods
- [static func fixed(CGFloat) -> MarkDimensions<DataElement>](./markdimensions/fixed%28_%29-14cur.md)
  A constant dimension.
- [static func fixed(KeyPath<DataElement, CGFloat>) -> MarkDimensions<DataElement>](./markdimensions/fixed%28_%29-7k7pv.md)
  A constant dimension.
- [static func inset(KeyPath<DataElement, CGFloat>) -> MarkDimensions<DataElement>](./markdimensions/inset%28_%29-309e3.md)
  A dimension that’s the step size minus the specified inset value on each side.
- [static func inset(CGFloat) -> MarkDimensions<DataElement>](./markdimensions/inset%28_%29-5nddx.md)
  A dimension that’s the step size minus the specified inset value on each side.
- [static func ratio(CGFloat) -> MarkDimensions<DataElement>](./markdimensions/ratio%28_%29-8ufgm.md)
  A dimension that’s proportional to the scale step size, using the specified ratio.
- [static func ratio(KeyPath<DataElement, CGFloat>) -> MarkDimensions<DataElement>](./markdimensions/ratio%28_%29-r23h.md)
  A dimension that’s proportional to the scale step size, using the specified ratio.

## Relationships

### Conforms To
- [ExpressibleByFloatLiteral](../Swift/expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](../Swift/expressiblebyintegerliteral.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/markdimensions)*