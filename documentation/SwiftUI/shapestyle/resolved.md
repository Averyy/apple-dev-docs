# Resolved

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type of shape style this will resolve to.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
associatedtype Resolved : ShapeStyle = Never
```

#### Discussion

When you create a custom shape style, Swift infers this type from your implementation of the required `resolve` function.

## See Also

### Resolving a shape style in an environment
- [func resolve(in: EnvironmentValues) -> Self.Resolved](./resolve%28in%29.md)
  Evaluate to a resolved shape style given the current `environment`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/resolved)*