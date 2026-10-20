# preferredMediaSelection

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The default media selections for this asset’s media selection groups.

**Availability**:
- iOS 9.0+ - Deprecated in 16.0
- iPadOS 9.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 2.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`preferredMediaSelection`](../avpartialasyncproperty/preferredmediaselection.md) asynchronously instead.

## Declaration

```swift
var preferredMediaSelection: AVMediaSelection { get }
```

```objc
@property (nonatomic, readonly) AVMediaSelection * preferredMediaSelection;
```

#### Discussion

Provides an instance of [`AVMediaSelection`](../avmediaselection.md) with the default selections for each of the assets media selection groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/preferredmediaselection)*