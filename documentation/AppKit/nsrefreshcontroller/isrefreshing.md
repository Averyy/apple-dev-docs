# isRefreshing

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether a refresh operation is in progress.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var isRefreshing: Bool { get }
```

#### Discussion

The default value of this property is `NO`. When the user triggers a refresh, this property automatically becomes `YES`. Call [`endRefreshing()`](nsrefreshcontroller/endrefreshing().md) when your refresh operation completes to reset this property to `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrefreshcontroller/isrefreshing)*