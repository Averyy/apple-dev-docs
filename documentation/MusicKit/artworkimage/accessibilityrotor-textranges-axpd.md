# accessibilityRotor(_:textRanges:)

**Framework**: MusicKit  
**Kind**: method

Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.

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
func accessibilityRotor(_ label: Text, textRanges: [Range<String.Index>]) -> some View
```

#### Discussion

An Accessibility Rotor is a shortcut for Accessibility users to quickly navigate to specific elements of the user interface, and optionally specific ranges of text within those elements.

In the following example, a Message application adds a Rotor allowing the user to navigate through all the ranges of text containing email addresses.

```swift
extension Message {
    // Ranges of special areas in the `content` text. Calculated
    // when `content` is set and then cached so that we don't have
    // to re-compute them.
    var emailAddressRanges: [Range<String.Index>]
}

struct MessageContentView: View {
    TextEditor(.constant(message.content))
        .accessibilityRotor("Email Addresses",
            textRanges: message.emailAddressRanges)
}
```

## Parameters

- `label`: Localized label identifying this Rotor to the user.
- `textRanges`: An array of ranges that will be used to generate   the entries of the Rotor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/accessibilityrotor(_:textranges:)-axpd)*