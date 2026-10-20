# Previews

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type to preview.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.0+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.0
- tvOS 13.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: Use #Preview instead.

## Declaration

```swift
associatedtype Previews : View
```

#### Discussion

When you create a preview, Swift infers this type from your implementation of the required [`previews`](./previews-swift.type.property.md) property.

## See Also

### Creating a preview
- [static var previews: Self.Previews](./previews-swift.type.property.md)
  A collection of views to preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewprovider/previews-swift.associatedtype)*