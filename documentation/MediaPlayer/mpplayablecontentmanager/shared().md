# shared()

**Framework**: Media Player  
**Kind**: method  
**Role**: Type Method

Returns the current content manager instance.

**Availability**:
- iOS 7.1+ - Deprecated in 14.0
- iPadOS 7.1+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use CarPlay framework

## Declaration

```swift
class func shared() -> Self
```

```objc
+ (instancetype) sharedContentManager;
```

#### Return Value

The current content manager.

#### Discussion

Call this method to create a new content manager. Set the [`dataSource`](./datasource.md) and [`delegate`](./delegate.md) immediately after creating the content manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/shared())*