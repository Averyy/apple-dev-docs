---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockanimatedbutton/init(contentview:highlightoptions:handlesselection:)"
framework: "CareKit/CareKitUI"
---

# init(contentView:highlightOptions:handlesSelection:)

**Framework**: CareKit/CareKitUI  
**Kind**: init  
**Role**: Initializer

Create an animated button with injected content. The content will automatically be constrained to the button’s `layoutMarginGuide`.

## Declaration

```swift
@MainActor
init(contentView: Content?, highlightOptions: Set<HighlightOption> = [], handlesSelection: Bool = true)
```

## Parameters

- `contentView`: The content to be constrained to the button’s `layoutMarginGuide`.
- `highlightOptions`: Options for displaying the highlighted state. Supplying no options cause the button to show no highlighted state
- `handlesSelection`: Automatically sets the selected state when the button is tapped.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockanimatedbutton/init(contentview:highlightoptions:handlesselection:))*