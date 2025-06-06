# focusSystem(for:)

**Framework**: UIKit  
**Kind**: method

Retrieves the focus system for the specified environment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class func focusSystem(for environment: any UIFocusEnvironment) -> UIFocusSystem?
```

#### Discussion

This method returns `nil` if focus interaction isn’t supported or if the environment isn’t associated with a focus system.

## Parameters

- `environment`: The environment that the focus system contains.

## See Also

- [init?(for: any UIFocusEnvironment)](uifocussystem/init(for:).md)
  Retrieves a focus system object that contains the state information for the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocussystem/focussystem(for:))*