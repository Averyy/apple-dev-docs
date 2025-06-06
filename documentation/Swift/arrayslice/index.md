# ArraySlice.Index

**Framework**: Swift  
**Kind**: typealias

The index type for arrays, `Int`.

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
typealias Index = Int
```

#### Discussion

`ArraySlice` instances are not always indexed from zero. Use `startIndex` and `endIndex` as the bounds for any element access, instead of `0` and `count`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/arrayslice/index)*