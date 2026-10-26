---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockresponsivelayout/sizeclassruleset"
framework: "CareKit/CareKitUI"
---

# OCKResponsiveLayout.SizeClassRuleSet

**Framework**: CareKit/CareKitUI  
**Kind**: struct  
**Role**: Structure

A set of `UIContentSizeCategory` specific rules for a given size class.

## Declaration

```swift
struct SizeClassRuleSet
```

## Topics

### Initializers
- [init(sizeClass: SizeClass, rules: [OCKResponsiveLayout<LayoutOption>.Rule<LayoutOption>])](./sizeclassruleset/init%28sizeclass,rules%29.md)
  Initialize a `SizeClassRuleSet` with a `UIUserInterfaceSizeClass` combination and `UIContentSizeCategory` specific rules.
- [init(sizeClasses: [SizeClass], rules: [OCKResponsiveLayout<LayoutOption>.Rule<LayoutOption>])](./sizeclassruleset/init%28sizeclasses,rules%29.md)
  Initialize a `SizeClassRuleSet` with a set of `UIUserInterfaceSizeClass` combinations and `UIContentSizeCategory` specific rules.
### Instance Properties
- [let rules: [OCKResponsiveLayout<LayoutOption>.Rule<LayoutOption>]](./sizeclassruleset/rules.md)
  A set of rules (combinations of `UIUserInterFaceSizeClass` combinations and user defined layouts.
- [let sizeClasses: [SizeClass]](./sizeclassruleset/sizeclasses.md)
  The valid size class combinations for this set of rules


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockresponsivelayout/sizeclassruleset)*