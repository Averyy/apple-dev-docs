# accessibilityRotor(_:entries:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func accessibilityRotor<Content>(_ label: LocalizedStringResource, @AccessibilityRotorContentBuilder entries: @escaping () -> Content) -> some View where Content : AccessibilityRotorContent
```

#### Discussion

An Accessibility Rotor is a shortcut for Accessibility users to quickly navigate to specific elements of the user interface, and optionally specific ranges of text within those elements.

In the following example, a Message application creates a Rotor allowing users to navigate to specifically the messages originating from VIPs.

```None
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/accessibilityrotor(_:entries:)-8ti4h)*