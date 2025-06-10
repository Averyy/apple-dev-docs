# insertElements(_:beforeAction:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Insert elements before an identified action.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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