# delegate

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The delegate object for this instance.

**Availability**:
- iOS 2.0+ - Deprecated in 27.3
- iPadOS 2.0+ - Deprecated in 27.3
- Mac Catalyst 13.1+ - Deprecated in 27.3
- macOS 10.2+ - Deprecated in 27.3
- tvOS 9.0+ - Deprecated in 27.3
- visionOS 1.0+ - Deprecated in 27.3

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