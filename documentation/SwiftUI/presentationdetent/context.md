# PresentationDetent.Context

**Framework**: SwiftUI  
**Kind**: struct

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
- [var maxDetentValue: CGFloat](presentationdetent/context/maxdetentvalue.md)
  The height that the presentation appears in.
### Supporting types
- [subscript<T>(dynamicMember _: KeyPath<EnvironmentValues, T>) -> T](presentationdetent/context/subscript(dynamicmember:).md)
  Returns the value specified by the keyPath from the environment.

## See Also

- [static func custom<D>(D.Type) -> PresentationDetent](presentationdetent/custom(_:).md)
  A custom detent with a calculated height.
- [static func fraction(CGFloat) -> PresentationDetent](presentationdetent/fraction(_:).md)
  A custom detent with the specified fractional height.
- [static func height(CGFloat) -> PresentationDetent](presentationdetent/height(_:).md)
  A custom detent with the specified height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationdetent/context)*