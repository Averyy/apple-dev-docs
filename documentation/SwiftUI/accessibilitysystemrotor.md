# AccessibilitySystemRotor

**Framework**: SwiftUI  
**Kind**: struct

Designates a Rotor that replaces one of the automatic, system-provided Rotors with a developer-provided Rotor.

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
struct AccessibilitySystemRotor
```

## Topics

### Iterating through text
- [static var textFields: AccessibilitySystemRotor](accessibilitysystemrotor/textfields.md)
  System Rotor allowing users to iterate through all text fields.
- [static var boldText: AccessibilitySystemRotor](accessibilitysystemrotor/boldtext.md)
  System Rotor allowing users to iterate through all the ranges of bolded text.
- [static var italicText: AccessibilitySystemRotor](accessibilitysystemrotor/italictext.md)
  System Rotor allowing users to iterate through all the ranges of italicized text.
- [static var underlineText: AccessibilitySystemRotor](accessibilitysystemrotor/underlinetext.md)
  System Rotor allowing users to iterate through all the ranges of underlined text.
- [static var misspelledWords: AccessibilitySystemRotor](accessibilitysystemrotor/misspelledwords.md)
  System Rotor allowing users to iterate through all the ranges of mis-spelled words.
### Iterating through headings
- [static var headings: AccessibilitySystemRotor](accessibilitysystemrotor/headings.md)
  System Rotor allowing users to iterate through all headings.
- [static func headings(level: AccessibilityHeadingLevel) -> AccessibilitySystemRotor](accessibilitysystemrotor/headings(level:).md)
  System Rotors allowing users to iterate through all headings, of various heading levels.
### Iterating through links
- [static var links: AccessibilitySystemRotor](accessibilitysystemrotor/links.md)
  System Rotor allowing users to iterate through all links.
- [static func links(visited: Bool) -> AccessibilitySystemRotor](accessibilitysystemrotor/links(visited:).md)
  System Rotors allowing users to iterate through links or visited links.
### Iterating through other elements
- [static var images: AccessibilitySystemRotor](accessibilitysystemrotor/images.md)
  System Rotor allowing users to iterate through all images.
- [static var landmarks: AccessibilitySystemRotor](accessibilitysystemrotor/landmarks.md)
  System Rotor allowing users to iterate through all landmarks.
- [static var lists: AccessibilitySystemRotor](accessibilitysystemrotor/lists.md)
  System Rotor allowing users to iterate through all lists.
- [static var tables: AccessibilitySystemRotor](accessibilitysystemrotor/tables.md)
  System Rotor allowing users to iterate through all tables.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilitysystemrotor)*