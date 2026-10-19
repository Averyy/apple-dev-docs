# setViewProperties(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Sets the view properties for a placement in the arrangement.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
mutating func setViewProperties(_ properties: Self.ViewProperties, for placement: UIArrangementViewController.ViewPlacement)
```

#### Discussion

Set view properties to configure how an arrangement presents a view in the placement you specify.

For more information on configuring arrangements with view properties, refer to specific implementations such as [`UIOverlayArrangement`](uioverlayarrangement-swift.struct.md) or [`UISplitArrangement`](uisplitarrangement-swift.struct.md).

## Parameters

- `properties`: The view properties to set.
- `placement`: The placement of the view properties in the arrangement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/arrangement/setviewproperties(_:for:))*