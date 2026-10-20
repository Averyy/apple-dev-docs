# snapshot()

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Renders the view’s scene into a new image object.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func snapshot() -> UIImage
```

*macOS*

```swift
func snapshot() -> NSImage
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (UIImage *) snapshot;
```

*macOS*

```objc
- (NSImage *) snapshot;
```

#### Return Value

An image object depicting the view in its current state.

#### Discussion

This method is thread-safe and may be called at any time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/snapshot())*