# Mirror.Child

**Framework**: Swift  
**Kind**: typealias

An element of the reflected instance’s structure.

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
typealias Child = (label: String?, value: Any)
```

#### Discussion

When the `label` component in not `nil`, it may represent the name of a stored property or an active `enum` case. If you pass strings to the `descendant(_:_:)` method, labels are used for lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mirror/child)*