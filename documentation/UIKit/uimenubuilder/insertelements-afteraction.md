# insertElements(_:afterAction:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Insert elements after an identified action.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
func insertElements(_ insertedElements: [UIMenuElement], afterAction siblingIdentifier: UIAction.Identifier)
```

## Parameters

- `insertedElements`: The elements to insert.
- `siblingIdentifier`: The identifier of the action to insert elements after.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/insertelements(_:afteraction:))*