# isVisible

**Framework**: AppKit  
**Kind**: property

A Boolean value that Indicates whether the Touch Bar is eligible for display.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var isVisible: Bool { get }
```

#### Discussion

A value of [`true`](https://developer.apple.com/documentation/swift/true) indicates that the bar is attached to an eligible bar provider and that its items are displayable, assuming adequate geometric space. A  is an object that conforms to the [`NSTouchBarProvider`](nstouchbarprovider.md) protocol. For more on bar providers, read [`Bar objects`](nstouchbar#Bar-objects.md).

This property is key–value observable.

## See Also

- [var itemIdentifiers: [NSTouchBarItem.Identifier]](nstouchbar/itemidentifiers.md)
  The list of identifiers for the current items in the Touch Bar.
- [func item(forIdentifier: NSTouchBarItem.Identifier) -> NSTouchBarItem?](nstouchbar/item(foridentifier:).md)
  Returns the Touch Bar item that corresponds to a given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbar/isvisible)*