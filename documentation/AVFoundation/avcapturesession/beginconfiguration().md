# beginConfiguration()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Marks the beginning of changes to a running capture session’s configuration to perform in a single atomic update.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func beginConfiguration()
```

```objc
- (void) beginConfiguration;
```

## Mentions

- [Setting up a capture session](../setting-up-a-capture-session.md)

#### Discussion

Call this method and [`commitConfiguration()`](./commitconfiguration%28%29.md) to batch multiple configuration operations on a running session into an atomic update.

After you call this method, you can add or remove outputs, alter the [`sessionPreset`](./sessionpreset.md), or configure individual capture input or output properties. The session configuration doesn’t change until you invoke [`commitConfiguration()`](./commitconfiguration%28%29.md), at which the system updates all settings. You can nest [`beginConfiguration()`](./beginconfiguration%28%29.md) and [`commitConfiguration()`](./commitconfiguration%28%29.md) pairs, and the system applies the changes when you call the outermost commit.

## See Also

### Configuring a session
- [func commitConfiguration()](./commitconfiguration%28%29.md)
  Commits one or more changes to a running capture session’s configuration in a single atomic update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/beginconfiguration())*