# accessibilityRotor(_:entries:entryID:entryLabel:)

**Framework**: FamilyControls  
**Kind**: method

Create an Accessibility Rotor with the specified user-visible label and entries.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
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

```swift
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

## See Also

- [func accessibilityRotor<Content>(Text, entries: () -> Content) -> some View](familyactivitypicker/accessibilityrotor(_:entries:)-210yl.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<L, Content>(L, entries: () -> Content) -> some View](familyactivitypicker/accessibilityrotor(_:entries:)-234mz.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<Content>(LocalizedStringKey, entries: () -> Content) -> some View](familyactivitypicker/accessibilityrotor(_:entries:)-3nods.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<Content>(AccessibilitySystemRotor, entries: () -> Content) -> some View](familyactivitypicker/accessibilityrotor(_:entries:)-99hnz.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<L, EntryModel, ID>(L, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](familyactivitypicker/accessibilityrotor(_:entries:entryid:entrylabel:)-1hmpp.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel, ID>(LocalizedStringKey, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](familyactivitypicker/accessibilityrotor(_:entries:entryid:entrylabel:)-6bu1u.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel, ID>(AccessibilitySystemRotor, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](familyactivitypicker/accessibilityrotor(_:entries:entryid:entrylabel:)-f72f.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<EntryModel>(Text, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](familyactivitypicker/accessibilityrotor(_:entries:entrylabel:)-4lszi.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(LocalizedStringKey, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](familyactivitypicker/accessibilityrotor(_:entries:entrylabel:)-8vebh.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(AccessibilitySystemRotor, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](familyactivitypicker/accessibilityrotor(_:entries:entrylabel:)-8wmbn.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<L, EntryModel>(L, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](familyactivitypicker/accessibilityrotor(_:entries:entrylabel:)-976pf.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor(Text, textRanges: [Range<String.Index>]) -> some View](familyactivitypicker/accessibilityrotor(_:textranges:)-64gnn.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(AccessibilitySystemRotor, textRanges: [Range<String.Index>]) -> some View](familyactivitypicker/accessibilityrotor(_:textranges:)-66zli.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor<L>(L, textRanges: [Range<String.Index>]) -> some View](familyactivitypicker/accessibilityrotor(_:textranges:)-9swhk.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(LocalizedStringKey, textRanges: [Range<String.Index>]) -> some View](familyactivitypicker/accessibilityrotor(_:textranges:)-wfkm.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/accessibilityrotor(_:entries:entryid:entrylabel:)-2um65)*