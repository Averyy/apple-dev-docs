# clear

**Framework**: SwiftUI  
**Kind**: property

The clear variant of glass.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static var clear: Glass { get }
```

#### Discussion

When using clear glass, ensure content remains legible by adding a dimming layer or other treatment beneath the glass.

For example, you could add a transparent black color beneath your glass to ensure content remains legible above the glass.

```swift
Label("Flag", systemImage: "flag.fill")
    .padding()
    .glassEffect(.clear)
    .background(.black.opacity(0.3))
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/glass/clear)*