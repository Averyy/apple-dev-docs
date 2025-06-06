# init(root:_:)

**Framework**: System  
**Kind**: init

Create a file path from a root and a collection of components.

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
init<C>(root: FilePath.Root?, _ components: C) where C : Collection, C.Element == FilePath.Component
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/init(root:_:)-19uu0)*