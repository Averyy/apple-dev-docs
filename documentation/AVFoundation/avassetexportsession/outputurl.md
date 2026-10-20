# outputURL

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A URL where an asset export session writes its output.

**Availability**:
- iOS 4.0+ - Deprecated in 27.0
- iPadOS 4.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.7+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use `export(to:as:isolation:)` instead.

## Declaration

```swift
var outputURL: URL? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSURL * outputURL;
```

#### Discussion

This property value is key-value observable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/outputurl)*