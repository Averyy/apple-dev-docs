# remove(menu:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Removes a menu from the menu system.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func remove(menu removedIdentifier: UIMenu.Identifier)
```

#### Discussion

Use this method to remove menus ([`UIMenu`](uimenu.md) objects) from a menu system.

## Parameters

- `removedIdentifier`: The identifier of the menu element to remove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/remove(menu:))*