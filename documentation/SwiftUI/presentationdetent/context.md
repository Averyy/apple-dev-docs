# PresentationDetent.Context

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Information that you use to calculate the presentation’s height.

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
@dynamicMemberLookup
struct Context
```

## Topics

### Getting the height
- [var maxDetentValue: CGFloat](./context/maxdetentvalue.md)
  The height that the presentation appears in.
### Supporting types
- [subscript<T>(dynamicMember _: KeyPath<EnvironmentValues, T>) -> T](./context/subscript%28dynamicmember%29.md)
  Returns the value specified by the keyPath from the environment.

## See Also

### Creating custom detents
- [static func custom<D>(D.Type) -> PresentationDetent](./custom%28_%29.md)
  A custom detent with a calculated height.
- [static func fraction(CGFloat) -> PresentationDetent](./fraction%28_%29.md)
  A custom detent with the specified fractional height.
- [static func height(CGFloat) -> PresentationDetent](./height%28_%29.md)
  A custom detent with the specified height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationdetent/context)*