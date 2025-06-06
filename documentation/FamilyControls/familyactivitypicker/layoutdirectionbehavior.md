# layoutDirectionBehavior(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the behavior of this view for different layout directions.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func layoutDirectionBehavior(_ behavior: LayoutDirectionBehavior) -> some View
```

#### Return Value

A view that conditionally mirrors its contents horizontally in a given layout direction.

#### Discussion

Use `layoutDirectionBehavior(_:)` when you need the system to horizontally mirror the contents of the view when presented in a layout direction.

To override the layout direction for a specific view, use the `View/environment(_:_:)` view modifier to explicitly override the `EnvironmentValues/layoutDirection` environment value for the view.

## Parameters

- `behavior`: A LayoutDirectionBehavior value that indicates   whether this view should mirror in a particular layout direction. By   default, views will adjust their layouts automatically in a   right-to-left context and do not need to be mirrored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/layoutdirectionbehavior(_:))*