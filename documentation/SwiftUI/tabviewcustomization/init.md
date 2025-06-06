# init()

**Framework**: SwiftUI  
**Kind**: init

Creates an empty tab sidebar customization.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init()
```

#### Discussion

To set this customization on a tab view, use the [`tabViewCustomization(_:)`](view/tabviewcustomization(_:).md) modifier.

With an empty customization, tabs will be visible according to the default builder visibilities, and sections will be ordered in the order declared in the tab view’s tab builder.

You can specify a default visibility for the tab in the tab bar and sidebar by attaching [`defaultVisibility(_:for:)`](tabcontent/defaultvisibility(_:for:).md) to the tab.

You can change the default section order by changing the order in the builder. If there’s an existing persisted customization, reset the order by calling [`resetTabOrder()`](tabviewcustomization/sectioncustomization/resettaborder().md) when you change the order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabviewcustomization/init())*