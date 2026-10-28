# buildFinalResult(_:)

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
static func buildFinalResult<Content>(_ component: Content) -> KeyframeTrack<Value, Value, Content> where Value == Content.Value, Content : KeyframeTrackContent
```

**Other overloads**:

```swift
static func buildFinalResult<Content>(_ component: Content) -> Content where Value == Content.Value, Content : Keyframes
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyframesbuilder/buildfinalresult(_:)-161lq)*