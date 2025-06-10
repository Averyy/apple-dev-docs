# Mirror.AncestorRepresentation.customized(_:)

**Framework**: Swift  
**Kind**: case

Uses the nearest ancestor’s implementation of `customMirror` to create a mirror for that ancestor.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case customized(() -> Mirror)
```

#### Discussion

Other classes derived from such an ancestor are given a default mirror. The payload for this option should always be `{ super.customMirror }`:

```swift
var customMirror: Mirror {
    return Mirror(
        self,
        children: ["someProperty": self.someProperty],
        ancestorRepresentation: .customized({ super.customMirror })) // <==
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mirror/ancestorrepresentation/customized(_:))*