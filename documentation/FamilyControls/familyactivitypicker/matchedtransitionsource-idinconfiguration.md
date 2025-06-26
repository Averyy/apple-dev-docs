# matchedTransitionSource(id:in:configuration:)

**Framework**: FamilyControls  
**Kind**: method

Identifies this view as the source of a navigation transition, such as a zoom transition.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func matchedTransitionSource(id: some Hashable, in namespace: Namespace.ID, configuration: (EmptyMatchedTransitionSourceConfiguration) -> some MatchedTransitionSourceConfiguration) -> some View
```

#### Discussion

The appearance of the source can be configured using the `configuration` trailing closure. Any modifiers applied will be smoothly interpolated when a zoom transition originates from this matched transition source.

```swift
MyView()
    .matchedTransitionSource(id: someID, in: someNamespace) { source in
        source
            .cornerRadius(8.0)
    }
```

## Parameters

- `id`: The identifier, often derived from the identifier of   the data being displayed by the view.
- `namespace`: The namespace in which defines the  . New   namespaces are created by adding an   variable   to a   type and reading its value in the view’s body   method.
- `configuration`: A closure that you can use to apply styling to the source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/matchedtransitionsource(id:in:configuration:))*