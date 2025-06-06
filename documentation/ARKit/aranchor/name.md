# name

**Framework**: ARKit  
**Kind**: property

A descriptive name for the anchor.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var name: String? { get }
```

## Mentions

- [Managing Session Life Cycle and Tracking Quality](managing-session-life-cycle-and-tracking-quality.md)

#### Discussion

To name an anchor, create one with the [`init(name:transform:)`](aranchor/init(name:transform:).md) initializer. This property is `nil` for anchors created otherwise.

ARKit does not display the name to users, but your app can use it to identify anchors for debugging.

## See Also

- [init(transform: simd_float4x4)](aranchor/init(transform:).md)
  Creates a new anchor object with the specified transform.
- [init(name: String, transform: simd_float4x4)](aranchor/init(name:transform:).md)
  Creates a new anchor object with the specified transform and a descriptive name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/aranchor/name)*