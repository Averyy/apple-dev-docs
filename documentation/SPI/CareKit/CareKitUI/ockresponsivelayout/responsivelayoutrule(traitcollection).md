---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockresponsivelayout/responsivelayoutrule(traitcollection:)"
framework: "CareKit/CareKitUI"
---

# responsiveLayoutRule(traitCollection:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Get a generic `LayoutOption` that has been mapped to a `UserInterfaceSizeClass` and `UIContentSizeCategory` for comparison provided by a given `UITraitCollection`.

## Declaration

```swift
func responsiveLayoutRule(traitCollection: UITraitCollection) -> LayoutOption
```

## Discussion

A UITraitCollection contains additional size and accessibility information beyond `UserInterfaceSizeClass` and `UIContentSizeCategory`. This class and method could be extended to respond to other changes beyond these two, however these are `Comparable` and provide a balance between convenient and flexibility. Consider creating additional factory methods instead of extending this method to respond to `contentSize` or `contentInsets` to maintain this convenience.

## Parameters

- `traitCollection`: The trait collection to extract device and accessility information.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockresponsivelayout/responsivelayoutrule(traitcollection:))*