# defaultViewProperties

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The default view properties for a view controller placed in the arrangement.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
var defaultViewProperties: Self.ViewProperties { get }
```

#### Discussion

Use these default view properties as a starting point to configure an arrangement.

For more information on configuring arrangements with view properties, refer to specific implementations such as [`UIOverlayArrangement`](uioverlayarrangement-swift.struct.md) or [`UISplitArrangement`](uisplitarrangement-swift.struct.md).

## See Also

- [associatedtype ViewProperties](uiarrangementviewcontroller/arrangement/viewproperties.md)
  Properties you use to customize how an arrangement presents views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/arrangement/defaultviewproperties)*