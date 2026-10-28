# label

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

A string used to name your effect.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var label: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * label;
```

## Discussion

The name of the effect isn’t used directly by GLKit, but is printed when, for example, you log the object to the console via the [`NSLog(_:_:)`](../../Foundation/nslog%28_,_%29.md) function in Swift, or the [`NSLog`](../../Foundation/nslog.md) function in Objective-C.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkbaseeffect/label)*