# accessibilityLinkedGroup(id:in:)

**Framework**: FamilyControls  
**Kind**: method

Links multiple accessibility elements so that the user can quickly navigate from one element to another, even when the elements are not near each other in the accessibility hierarchy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func accessibilityLinkedGroup<ID>(id: ID, in namespace: Namespace.ID) -> some View where ID : Hashable
```

#### Discussion

This can be useful to allow quickly jumping between content in a list and the same content shown in a detail view, for example. All elements marked with `accessibilityLinkedGroup` with the same namespace and identifier will be linked together.

## Parameters

- `id`: A hashable identifier used to separate sets of linked elements   within the same namespace. Elements with matching   and    will be linked together.
- `namespace`: The namespace to use to organize linked accessibility   elements. All elements marked with   in this   namespace and with the specified   will be linked together.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/accessibilitylinkedgroup(id:in:))*