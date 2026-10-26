---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockresponsivelayout/init(defaultlayout:anysizeclassruleset:sizeclassspecificrulesets:)"
framework: "CareKit/CareKitUI"
---

# init(defaultLayout:anySizeClassRuleSet:sizeClassSpecificRuleSets:)

**Framework**: CareKit/CareKitUI  
**Kind**: init  
**Role**: Initializer

Initialize a `OCKResponsiveLayout` with default and specific size class rules.

## Declaration

```swift
init(defaultLayout: LayoutOption, anySizeClassRuleSet: [OCKResponsiveLayout.Rule<LayoutOption>], sizeClassSpecificRuleSets: [SizeClassRuleSet] = [])
```

## Parameters

- `defaultLayout`: The default layout rules for when no matching size class rule is provided, usually when layouts need to support dynamic type, but not size class
- `anySizeClassRuleSet`: Rule sets responsive to content size category but no specific size classes
- `sizeClassSpecificRuleSets`: Size class specific layout rule sets


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockresponsivelayout/init(defaultlayout:anysizeclassruleset:sizeclassspecificrulesets:))*