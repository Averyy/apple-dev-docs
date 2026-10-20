# flatMap(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Swift - Deprecated in 4.1 (renamed: compactMap(_:))

> **Deprecated**: Please use compactMap(_:) for the case where closure returns an optional value

## Declaration

```swift
func flatMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazymapsequence/iterator/flatmap(_:)-esus)*