# shared()

**Framework**: Media Player  
**Kind**: method

Returns the current content manager instance.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func shared() -> Self
```

#### Return Value

The current content manager.

#### Discussion

Call this method to create a new content manager. Set the [`dataSource`](mpplayablecontentmanager/datasource.md) and [`delegate`](mpplayablecontentmanager/delegate.md) immediately after creating the content manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/shared())*