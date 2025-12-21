# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript

Returns a sequence which iterates of the values of a single attribute.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
subscript<K>(type: K.Type) -> some Sequence<Optional<K.Value>> where K : AttributedStringKey, K.Value : Sendable { get }
```

#### Overview

In the case of a range selection, the returned sequence is based on the runs of the specified attribute, not the runs over all attributes.

```swift
selection.attributes(in: text)[MyAttribute.self].contains(myValue)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextselection/attributes/subscript(_:))*