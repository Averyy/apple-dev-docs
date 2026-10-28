# buildPartialBlock(first:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func buildPartialBlock<K>(first: K) -> K where Value == K.Value, K : KeyframeTrackContent
```

**Other overloads**:

```swift
static func buildPartialBlock<Content>(first: Content) -> Content where Value == Content.Value, Content : Keyframes
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyframesbuilder/buildpartialblock(first:)-6va20)*