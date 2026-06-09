# accessibilityIdentifier(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

Uses the string you specify to identify the view. Use this value for testing. It isn’t visible to the user.

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
nonisolated
func accessibilityIdentifier(_ identifier: String, isEnabled: Bool = true) -> some TabContent<Self.TabValue>
```

## Parameters

- `identifier`: The accessibility identifier to apply.
- `isEnabled`: If true the accessibility identifier is applied; otherwise the accessibility identifier is unchanged.

## See Also

- [func accessibilityHint(_:isEnabled:)](tabcontent/accessibilityhint(_:isenabled:).md)
  Communicates to the user what happens after selecting the tab.
- [func accessibilityInputLabels(_:isEnabled:)](tabcontent/accessibilityinputlabels(_:isenabled:).md)
  Sets alternate input labels with which users identify a tab.
- [func accessibilityLabel(_:isEnabled:)](tabcontent/accessibilitylabel(_:isenabled:).md)
  Adds a label to the tab that describes its contents.
- [func accessibilityValue(_:isEnabled:)](tabcontent/accessibilityvalue(_:isenabled:).md)
  Adds a textual description of the value that the tab contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/accessibilityidentifier(_:isenabled:))*