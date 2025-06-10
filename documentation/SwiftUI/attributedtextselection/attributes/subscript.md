# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript

Returns a sequence which iterates of the values of a single attribute.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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