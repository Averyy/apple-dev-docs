# accessibilityRotor(_:textRanges:)

**Framework**: Assignables  
**Kind**: method

Create an Accessibility Rotor replacing the specified system-provided Rotor. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.

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
func accessibilityRotor(_ systemRotor: AccessibilitySystemRotor, textRanges: [Range<String.Index>]) -> some View
```

#### Discussion

An Accessibility Rotor is a shortcut for Accessibility users to quickly navigate to specific elements of the user interface, and optionally specific ranges of text within those elements.

In the following example, a Message application adds a Rotor allowing the user to navigate through all the ranges of text containing headings.

```None
extension Message {
    // Ranges of special areas in the `content` text. Calculated when
    // `content` is set and then cached so that we don't have to
    // re-compute them.
    var headingRanges: [Range<String.Index>]
}

struct MessageContentView: View {
    TextEditor(.constant(message.content))
        .accessibilityRotor(
            .heading,
            textRanges: message.headingRanges
        )
}
```

## Parameters

- `systemRotor`: The system-provided Rotor that will be overridden   by this custom Rotor.
- `textRanges`: An array of ranges that will be used to generate   the entries of the Rotor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/accessibilityrotor(_:textranges:)-3zz9h)*