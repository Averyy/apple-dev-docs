# insertElements(_:atStartOfMenu:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Insert elements at the start of an identified parent menu.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
func insertElements(_ childElements: [UIMenuElement], atStartOfMenu parentIdentifier: UIMenu.Identifier)
```

## Parameters

- `childElements`: The child elements to insert.
- `parentIdentifier`: The identifier of the parent menu to insert elements at the start of.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/insertelements(_:atstartofmenu:))*