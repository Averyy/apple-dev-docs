# alignedWith(appAxis:)

**Framework**: Group Activities  
**Kind**: method

Creates a direction that orients the participant to look along the specified axis in the direction of the app’s content.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func alignedWith(appAxis: SpatialTemplateElementAxis) -> SpatialTemplateElementDirection
```

#### Return Value

A direction type that faces the specified seat position.

#### Discussion

Use this function to create a seat that faces perpendicular to the app. For example, you might use it to mimic a long bench or stadium-style seating. The following code shows how to create such a line of seats:

```swift
struct Line: SpatialTemplate {
    var elements: [any SpatialTemplateElement] {
        (-2...2).map { seatIndex in
            .seat(
                position: .app.offsetBy(x: Double(seatIndex) * 2, z: 3),
                direction: .alignedWith(appAxis: .z)
            )
        }
    }
}
```

## Parameters

- `appAxis`: The axis for the participant to look along.

## See Also

- [struct SpatialTemplateElementAxis](spatialtemplateelementaxis.md)
  An axis to use when aligning elements in a spatial template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplateelementdirection/alignedwith(appaxis:))*