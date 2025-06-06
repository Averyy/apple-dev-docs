# PreferenceKey

**Framework**: SwiftUI  
**Kind**: protocol

A named value produced by a view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol PreferenceKey
```

#### Overview

A view with multiple children automatically combines its values for a given preference into a single value visible to its ancestors.

## Topics

### Getting the default value
- [static var defaultValue: Self.Value](preferencekey/defaultvalue.md)
  The default value of the preference.
- [associatedtype Value](preferencekey/value.md)
  The type of value produced by this preference.
### Combining preferences
- [static func reduce(value: inout Self.Value, nextValue: () -> Self.Value)](preferencekey/reduce(value:nextvalue:).md)
  Combines a sequence of values by modifying the previously-accumulated value with the result of a closure that provides the next value.

## Relationships

### Conforming Types
- [PreferredColorSchemeKey](preferredcolorschemekey.md)
- [Text.LayoutKey](text/layoutkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/preferencekey)*