# isRefreshing

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether a refresh operation is in progress.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var isRefreshing: Bool { get }
```

```objc
@property (readonly) BOOL isRefreshing;
```

#### Discussion

The default value of this property is `NO`. When the user triggers a refresh, this property automatically becomes `YES`. Call [`endRefreshing()`](./endrefreshing%28%29.md) when your refresh operation completes to reset this property to `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrefreshcontroller/isrefreshing)*