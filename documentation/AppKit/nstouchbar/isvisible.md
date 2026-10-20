# isVisible

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that Indicates whether the Touch Bar is eligible for display.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
var isVisible: Bool { get }
```

```objc
@property (readonly, getter=isVisible) BOOL visible;
```

#### Discussion

A value of [`true`](../../Swift/true.md) indicates that the bar is attached to an eligible bar provider and that its items are displayable, assuming adequate geometric space. A *bar provider* is an object that conforms to the [`NSTouchBarProvider`](../nstouchbarprovider.md) protocol. For more on bar providers, read [Bar objects](../nstouchbar.md#Bar-objects).

This property is key–value observable.

## See Also

### Observing bar status
- [var itemIdentifiers: [NSTouchBarItem.Identifier]](./itemidentifiers.md)
  The list of identifiers for the current items in the Touch Bar.
- [func item(forIdentifier: NSTouchBarItem.Identifier) -> NSTouchBarItem?](./item%28foridentifier%29.md)
  Returns the Touch Bar item that corresponds to a given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbar/isvisible)*