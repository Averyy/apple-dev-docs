# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates a view that represents the body of a disclosure group.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@ViewBuilder
@MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

#### Discussion

SwiftUI calls this method for each instance of [`DisclosureGroup`](disclosuregroup.md) that you create within a view hierarchy where this style is the current [`DisclosureGroupStyle`](disclosuregroupstyle.md).

## Parameters

- `configuration`: The properties of the instance being created.

## See Also

- [struct DisclosureGroupStyleConfiguration](disclosuregroupstyleconfiguration.md)
  The properties of a disclosure group instance.
- [DisclosureGroupStyle.Configuration](disclosuregroupstyle/configuration.md)
  The properties of a disclosure group instance.
- [associatedtype Body : View](disclosuregroupstyle/body.md)
  A view that represents the body of a disclosure group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/disclosuregroupstyle/makebody(configuration:))*