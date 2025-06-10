# accessibilityRotor(_:entries:)

**Framework**: SwiftUI  
**Kind**: method

Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func accessibilityRotor<Content>(_ label: LocalizedStringResource, @AccessibilityRotorContentBuilder entries: @escaping () -> Content) -> some View where Content : AccessibilityRotorContent
```

#### Discussion

An Accessibility Rotor is a shortcut for Accessibility users to quickly navigate to specific elements of the user interface, and optionally specific ranges of text within those elements.

In the following example, a Message application creates a Rotor allowing users to navigate to specifically the messages originating from VIPs.

```swift
// `messages` is a list of `Identifiable` `Message`s.

ScrollView {
    LazyVStack {
        ForEach(messages) { message in
            MessageView(message)
        }
    }
}
.accessibilityElement(children: .contain)
.accessibilityRotor("VIPs") {
    // Not all the MessageViews are generated at once, the model
    // knows about all the messages.
    ForEach(messages) { message in
        // If the Message is from a VIP, make a Rotor entry for it.
        if message.isVIP {
            AccessibilityRotorEntry(message.subject, id: message.id)
        }
    }
}
```

## Parameters

- `label`: Localized label identifying this Rotor to the user.
- `entries`: Content used to generate Rotor entries. This can   include AccessibilityRotorEntry structs, as well as constructs such   as if and ForEach.

## See Also

- [func accessibilityRotor(_:entries:entryID:entryLabel:)](view/accessibilityrotor(_:entries:entryid:entrylabel:).md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor(_:entries:entryLabel:)](view/accessibilityrotor(_:entries:entrylabel:).md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor(_:textRanges:)](view/accessibilityrotor(_:textranges:).md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilityrotor(_:entries:))*