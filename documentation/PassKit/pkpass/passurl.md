# passURL

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The URL that opens the pass in the Wallet app.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
var passURL: URL? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSURL * passURL;
```

## Discussion

Use the [`openURL(_:)`](../../UIKit/uiapplication/openurl%28_%29.md) method to open the pass in the Wallet app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/passurl)*