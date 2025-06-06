# accessibilityRotor(_:entries:)

**Framework**: RealityKit  
**Kind**: method

Create an Accessibility Rotor replacing the specified system-provided Rotor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func accessibilityRotor<Content>(_ systemRotor: AccessibilitySystemRotor, @AccessibilityRotorContentBuilder entries: @escaping () -> Content) -> some View where Content : AccessibilityRotorContent
```

#### Discussion

An Accessibility Rotor is a shortcut for Accessibility users to quickly navigate to specific elements of the user interface, and optionally specific ranges of text within those elements. Replacing system Rotors this way is useful when the System Rotor does not automatically pick up elements that aren’t on-screen, such as elements far down in a `LazyVStack` or `List`.

In the following example, a Message application adds a Rotor allowing the user to navigate through all the ranges of text containing headings.

```None
extension Message {
    // Ranges of special areas in the `content` text. Calculated
    // when `content` is set and then cached so that we don't have
    // to re-compute them.
    var contentHeadingRanges: [Range<String.Index>]
}

struct MessageContentView: View {
    TextEditor(.constant(message.content))
        .accessibilityRotor(.heading) {
            ForEach(range in message.contentHeadingRanges) {
                AccessibilityRotorEntry(textRange: range)
            }
        }
}
```

## Parameters

- `systemRotor`: The system-provided Rotor that will be overridden   by this custom Rotor.
- `entries`: Content used to generate Rotor entries. This can   include AccessibilityRotorEntry structs, as well as constructs such   as if and ForEach.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/accessibilityrotor(_:entries:)-46w1w)*