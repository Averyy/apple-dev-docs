# append(_:)

**Framework**: System  
**Kind**: method

Append a `component` on to the end of this path.

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
mutating func append(_ component: FilePath.Component)
```

#### Discussion

Example:

```swift
var path: FilePath = "/tmp"
let sub: FilePath = "foo/./bar/../baz/."
for comp in sub.components.filter({ $0.kind != .currentDirectory }) {
  path.append(comp)
}
// path is "/tmp/foo/bar/../baz"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/append(_:)-8f41n)*