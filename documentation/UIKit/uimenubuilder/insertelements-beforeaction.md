# insertElements(_:beforeAction:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Insert elements before an identified action.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
func insertElements(_ insertedElements: [UIMenuElement], beforeAction siblingIdentifier: UIAction.Identifier)
```

## Parameters

- `insertedElements`: The elements to insert.
- `siblingIdentifier`: The identifier of the action to insert elements before.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/insertelements(_:beforeaction:))*