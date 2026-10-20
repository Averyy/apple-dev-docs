# delegate

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The delegate object for this instance.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.2+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use nw_browser_t in Network framework instead

## Declaration

```swift
unowned(unsafe) var delegate: (any NetServiceBrowserDelegate)? { get set }
```

```objc
@property (assign, nullable) id<NSNetServiceBrowserDelegate> delegate;
```

## See Also

### Configuring Network Service Browsers
- [var includesPeerToPeer: Bool](./includespeertopeer.md)
  Whether to browse over peer-to-peer Bluetooth and Wi-Fi, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowser/delegate)*