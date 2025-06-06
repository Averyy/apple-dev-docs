# touchBar(_:makeItemForIdentifier:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate object for the bar item for the specified bar and item identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
optional func touchBar(_ touchBar: NSTouchBar, makeItemForIdentifier identifier: NSTouchBarItem.Identifier) -> NSTouchBarItem?
```

#### Return Value

A fully initialized bar item for the specified bar and identifier.

#### Discussion

When the system needs to populate a bar’s items array, the system calls this delegate method to retrieve an item if that item can’t be found in the bar’s private array or in the bar’s [`templateItems`](nstouchbar/templateitems.md) property.

## Parameters

- `touchBar`: The bar that’s requesting the bar item.
- `identifier`: The item identifier associated with the item being requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbardelegate/touchbar(_:makeitemforidentifier:))*