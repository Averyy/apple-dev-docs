# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a view representing the body of a control group.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@ContentBuilder
@MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

#### Discussion

This method will be called for each instance of [`ControlGroup`](../controlgroup.md) created within a view hierarchy where this style is the current `ControlGroupStyle`.

## Parameters

- `configuration`: The properties of the control group instance being created.

## See Also

### Creating custom control group styles
- [ControlGroupStyle.Configuration](./configuration.md)
  The properties of a `ControlGroup` instance being created.
- [associatedtype Body : View](./body.md)
  A view representing the body of a control group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroupstyle/makebody(configuration:))*