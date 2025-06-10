# replace(action:with:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Replace an identified action with menu elements.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
func replace(action replacedIdentifier: UIAction.Identifier, with replacementElements: [UIMenuElement])
```

## Parameters

- `replacedIdentifier`: The identifier of the action to be replaced.
- `replacementElements`: The replacement elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/replace(action:with:))*