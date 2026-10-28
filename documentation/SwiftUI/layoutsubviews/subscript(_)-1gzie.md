# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript  
**Role**: Instance Subscript

Gets the subview proxy at a specified index.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
subscript(index: Int) -> LayoutSubviews.Element { get }
```

**Other overloads**:

```swift
subscript(bounds: Range<Int>) -> LayoutSubviews { get }
```

```swift
subscript<S>(indices: S) -> LayoutSubviews where S : Sequence, S.Element == Int { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layoutsubviews/subscript(_:)-1gzie)*