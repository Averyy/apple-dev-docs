# associatedKind(_:)

**Framework**: SwiftUI  
**Kind**: method

Tells the system that a relevance-based widget can replace a timeline-based widget.

**Availability**:
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func associatedKind(_ associatedKind: String?) -> some WidgetConfiguration
```

#### Discussion

If you offer a timeline-based widget and a widget that uses relevance clues, a person could pin the timeline widget to the Smart Stack, and several instances of the relevance-based widget could appear in the Smart Stack, causing the stack to run out of space. To allow the Smart Stack to display the most relevant widgets by replacing the timeline-based widget with your widgets that use relevance clues, associate your timeline-based widget with relevance widget configuration using `associatedKind(_:)`.

> **Note**: Use this modifier for a widget you configure with a `RelevanceConfiguration` and provide an associated timeline-based widget. The system ignores associations with other relevance-based widgets and if your configuration doesn’t conform to `RelevanceConfiguration`.

For more information about widgets that appear in the Smart Stack on Apple Watch, refer to doc:Widget-Suggestions-In-Smart-Stacks.

- parameter: associatedKind: The string that identifies the associated timeline-based widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetconfiguration/associatedkind(_:))*