# accessibilityRotor(_:entries:entryLabel:)

**Framework**: MusicKit  
**Kind**: method

Create an Accessibility Rotor with the specified user-visible label and entries.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func accessibilityRotor<L, EntryModel>(_ rotorLabel: L, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View where L : StringProtocol, EntryModel : Identifiable
```

#### Discussion

An Accessibility Rotor is a shortcut for Accessibility users to quickly navigate to specific elements of the user interface, and optionally specific ranges of text within those elements.

Using this modifier requires that the Rotor be attached to a `ScrollView`, or an Accessibility Element directly within a `ScrollView`, such as a `ForEach`.

In the following example, a Message application creates a Rotor allowing users to navigate to specifically the messages originating from VIPs.

```swift
// `messages` is a list of `Identifiable` `Message`s that have a
// `subject`.
// `vipMesages` is a filtered version of that list containing only
// messages from VIPs.

ScrollView {
    LazyVStack {
        ForEach(messages) { message in
            MessageView(message)
        }
    }
}
.accessibilityElement(children: .contain)
.accessibilityRotor("VIPs", entries: vipMessages, label: \.subject)
```

## Parameters

- `rotorLabel`: Localized label identifying this Rotor to the user.
- `entries`: An array of identifiable values that will be   used to generate the entries of the Rotor. The identifiers   of the   values must match up with identifiers in a    or explicit   calls within the  .   When the user navigates to entries from this Rotor, SwiftUI will   automatically scroll them into place as needed.
- `entry`: Key path on the   type that can be   used to get a user-visible label for every Rotor entry. This is used   on macOS when the user opens the list of entries for the Rotor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/accessibilityrotor(_:entries:entrylabel:)-7anr5)*