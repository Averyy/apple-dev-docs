# accessibilityRotor(_:entries:entryID:entryLabel:)

**Framework**: RealityKit  
**Kind**: method

Create an Accessibility Rotor with the specified user-visible label and entries.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func accessibilityRotor<EntryModel, ID>(_ rotorLabel: Text, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View where ID : Hashable
```

#### Discussion

An Accessibility Rotor is a shortcut for Accessibility users to quickly navigate to specific elements of the user interface, and optionally specific ranges of text within those elements.

Using this modifier requires that the Rotor be attached to a `ScrollView`, or an Accessibility Element directly within a `ScrollView`, such as a `ForEach`. When the user navigates to entries from this Rotor, SwiftUI will automatically scroll them into place as needed.

In the following example, a Message application creates a Rotor allowing users to navigate to specifically the messages originating from VIPs.

```None
// `messages` is a list of `Message`s that have a `subject` and a
// `uuid`. `vipMessages` is a filtered version of that list
// containing only messages from VIPs.
ScrollView {
    LazyVStack {
        ForEach(messages) { message in
            MessageView(message)
        }
    }
}
.accessibilityElement(children: .contain)
.accessibilityRotor("VIPs", entries: vipMessages,
    id: \.uuid, label: \.subject)
```

## Parameters

- `rotorLabel`: Localized label identifying this Rotor to the user.
- `entries`: An array of values that will be used to generate   the entries of the Rotor.
- `entryID`: Key path on the entry type that can be used   to generate an identifier for the Entry. The identifiers   must match up with identifiers in   or explicit   calls   within the  .
- `entryLabel`: Key path on the entry type that can be   used to get a user-visible label for every Rotor entry. This is used   on macOS when the user opens the list of entries for the Rotor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3dplaceholdercontent/accessibilityrotor(_:entries:entryid:entrylabel:)-4szhk)*