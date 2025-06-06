# AccessibilityRotorEntry

**Framework**: SwiftUI  
**Kind**: struct

A struct representing an entry in an Accessibility Rotor.

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
struct AccessibilityRotorEntry<ID> where ID : Hashable
```

#### Overview

An Accessibility Rotor is a shortcut for Accessibility users to quickly navigate to specific elements of the user interface, and optionally specific ranges of text within those elements.

An entry in a Rotor may contain a label to identify the entry to the user, and identifier used to determine which Accessibility element the Rotor entry should navigate to, as well as an optional range used for entries that navigate to a specific position in the text of their associated Accessibility element. An entry can also specify a handler to be called before the entry is navigated to, to do any manual work needed to bring the Accessibility element on-screen.

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
    // Not all the `MessageView`s are generated at once, but the model
    // knows about all the messages.
    ForEach(messages) { message in
        // If the Message is from a VIP, make a Rotor entry for it.
        if message.isVIP {
            AccessibilityRotorEntry(message.subject, id: message.id)
        }
    }
}
```

An entry may also be created using an optional namespace, for situations where there are multiple Accessibility elements within a ForEach iteration or where a `ScrollView` is not present. In this case, the `prepare` closure may be needed in order to scroll the element into position using `ScrollViewReader`. The same namespace should be passed to calls to `accessibilityRotorEntry(id:in:)` to tag the Accessibility elements associated with this entry.

In the following example, a Message application creates a Rotor allowing users to navigate to specifically the messages originating from VIPs. The Rotor entries are associated with the content text of the message, which is one of the two views within the ForEach that generate Accessibility elements. That view is tagged with `accessibilityRotorEntry(id:in:)` so that it can be found by the `AccessibilityRotorEntry`, and `ScrollViewReader` is used with the `prepare` closure to scroll it into position.

```swift
struct MessageListView: View {
    @Namespace var namespace

    var body: some View {
        ScrollViewReader { scroller in
             ScrollView {
                LazyVStack {
                    ForEach(allMessages) { message in
                        VStack {
                            Text(message.subject)
                            // Tag this `Text` as an element associated
                            // with a Rotor entry.
                            Text(message.content)
                                .accessibilityRotorEntry(
                                    "\(message.id)_content",
                                    in: namespace
                                )
                        }
                    }
                }
            }
            .accessibilityElement(children: .contain)
            .accessibilityRotor("VIP Messages") {
                ForEach(vipMessages) { vipMessage in
                    // The Rotor entry points to a specific ID we
                    // defined within a given `ForEach` iteration,
                    // not to the entire `ForEach` iteration.
                    AccessibilityRotorEntry(vipMessage.subject,
                        id: "\(vipMessage.id)_content", in: namespace)
                    {
                        // But the ID we give to `ScrollViewReader`
                        // matches the one used in the `ForEach`, which
                        // is the identifier for the whole iteration
                        // and what `ScrollViewReader` requires.
                        scroller.scrollTo(vipMessage.id)
                    }
                }
            }
        }
    }
}
```

## Topics

### Creating a rotor entry
- [init(_:textRange:prepare:)](accessibilityrotorentry/init(_:textrange:prepare:).md)
  Create a Rotor entry with a specific label and range. This Rotor entry will be associated with the Accessibility element that owns the Rotor.
- [init(_:id:textRange:prepare:)](accessibilityrotorentry/init(_:id:textrange:prepare:).md)
  Create a Rotor entry with a specific label and identifier, with an optional range.
### Creating an identified rotor entry in a namespace
- [init(_:id:in:textRange:prepare:)](accessibilityrotorentry/init(_:id:in:textrange:prepare:).md)
  Create a Rotor entry with a specific label, identifier and namespace, and with an optional range.
- [init<L>(L, ID, in: Namespace.ID, textRange: Range<String.Index>?, prepare: () -> Void)](accessibilityrotorentry/init(_:_:in:textrange:prepare:).md)
  Create a Rotor entry with a specific label, identifier and namespace, and with an optional range.

## Relationships

### Conforms To
- [AccessibilityRotorContent](accessibilityrotorcontent.md)
- [Copyable](../Swift/Copyable.md)

## See Also

- [protocol AccessibilityRotorContent](accessibilityrotorcontent.md)
  Content within an accessibility rotor.
- [struct AccessibilityRotorContentBuilder](accessibilityrotorcontentbuilder.md)
  Result builder you use to generate rotor entry content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityrotorentry)*