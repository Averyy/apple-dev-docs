# accessibilityRotor(_:entries:entryLabel:)

**Framework**: Assignables  
**Kind**: method

Create an Accessibility Rotor replacing the specified system-provided Rotor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func accessibilityRotor<EntryModel>(_ systemRotor: AccessibilitySystemRotor, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View where EntryModel : Identifiable
```

#### Discussion

An Accessibility Rotor is a shortcut for Accessibility users to quickly navigate to specific elements of the user interface, and optionally specific ranges of text within those elements.

Using this modifier requires that the Rotor be attached to a `ScrollView`, or an Accessibility Element directly within a `ScrollView`, such as a `ForEach`.

In the following example, a Message application creates a Rotor allowing users to navigate to the headings in its vertical stack of messages.

```None
// `messageListItems` is a list of `Identifiable` `MessageListItem`s
// that are either a `Message` or a heading, containing a `subject`.
// `headingMessageListItems` is a filtered list of
// `messageListItems` containing just the headings.
ScrollView {
    LazyVStack {
        ForEach(messageListItems) { messageListItem in
            switch messageListItem {
                case .heading(let subject):
                    Text(subject)
                case .message(let message):
                    MessageView(message)
            }
        }
    }
}
.accessibilityElement(children: .contain)
.accessibilityRotor(
    .heading, entries: headingMessageListItems, label: \.subject)
```

## Parameters

- `systemRotor`: The system-provided Rotor that will be overridden   by this custom Rotor.
- `entries`: An array of identifiable values that will be   used to generate the entries of the Rotor. The identifiers   of the   values must match up with identifiers in a    or explicit   calls within the  .   When the user navigates to entries from this Rotor, SwiftUI will   automatically scroll them into place as needed.
- `entryLabel`: Key path on the   type that can be   used to get a user-visible label for every Rotor entry. This is used   on macOS when the user opens the list of entries for the Rotor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/accessibilityrotor(_:entries:entrylabel:)-7ke8u)*